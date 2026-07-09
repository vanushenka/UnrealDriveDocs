# Generate Attributes

**Generate Attributes** generate geometry that follows a road lane — guardrails, barriers, fences, trees, lamp posts,
power lines, and (with lofting) bridges and interchanges. Like all [attributes](/concepts/Attributes.md) they are
driven by keys placed along the lane; between keys the generated geometry follows the lane and blends the per-key
transform smoothly.

You create a Generate Attribute as an **[Attribute Profile](/profiles/AttributeProfile.md)** asset — pick one of
the types below — then add it to a lane and place keys with the [Attribute sub-mode](/editing/AttributeMode.md).

## Types

- **[Spline Mesh](/attributes/SplineMeshAttribute.md)** — sweep a static mesh into a spline mesh along the lane.
- **[Component Template](/attributes/ComponentTemplateAttribute.md)** — repeat a scene component along the lane.
- **[Actor Template](/attributes/ActorTemplateAttribute.md)** — spawn an actor repeatedly along the lane.
- **[Lofting](/attributes/LoftingAttribute.md)** *(Pro)* — extrude 2D cross-sections into a continuous surface (bridges, tunnels, decks).

They all derive from the **[Generate](#the-generate-base-class)** base class, so they share the anchor, alignment and per-key
transform described below.

## How a Generate Attribute follows the lane

Each key positions the generated geometry with an **anchor** on the road surface plus a transform. Between keys the
geometry is subdivided into small segments (roughly `LengthOfSegment` cm apart) and the transform is interpolated, so
the run bends and twists smoothly with the road.

**Alignment** decides where the anchor sits across the lane:

- `Auto` — anchor at the geometric **center** of the lane/zone (`Alpha` is ignored).
- `Fixed` — anchor placed by **`Alpha`**: `0` = inner edge, `0.5` = center, `1` = outer edge.

Per-key transform channels:

| Field | Interp | Purpose |
|-------|--------|---------|
| `Alpha` | cubic | Anchor position across the lane (only in `Fixed` alignment) |
| `Scale` | cubic | Cross-section scale — X = lateral, Y = vertical |
| `Offset` | cubic | Cross-section offset [cm] — X = R-axis (lateral), Y = H-axis (height) |
| `Roll` | cubic | Rotation around the road tangent (S-axis) [degrees] |
| `bIsReverse` | stepped | Mirror the cross-section along X (left ↔ right) |
| `bSkipSegment` | stepped | Skip this key's segment (leave a gap) |
| `Alignment` | stepped | `Auto` or `Fixed` (see above) |
| `OverrideLeftWidth` / `OverrideRightWidth` | stepped | Enable a manual width override |
| `LeftWidth` / `RightWidth` | stepped | Override [cm]: distance from the anchor to each boundary |

## Create new Attribute

Create a new attribute from the **Content Browser** under the **Meta Road** category:

![Creating a new attribute from the Content Browser Meta Road category](/img/create-new-attribute.png)

In the **Pick Parent Class** dialog choose `RoadLaneAttributeGenerateDescriptor`:

![Choosing RoadLaneAttributeGenerateDescriptor as the parent class](/img/curve-create.png)

## The Generate base class

`URoadLaneAttributeGenerateDescriptor` (Blueprint/C++ display name **Generate**) is the base class of every Generate
Attribute. It generates nothing by itself — the plugin's mesh pipeline (`FSplineMeshOp`) reads the lane's keys, walks
the anchor path, and calls a single method — **`GenerateAsset()`** — **once per segment**. You override that method to
emit whatever geometry you want. Subclassing **Generate** in **Blueprint** and overriding `GenerateAsset()` is the
primary way to build your own **custom attribute** — no C++ required. Use it directly when the [types](#types) above
don't fit.

![The Generate Attribute Blueprint, overriding the GenerateAsset event](/img/generate-attribute-api.png)

### What `GenerateAsset` receives

The event fires once for every segment the pipeline produced along the lane:

| Parameter | Type | Meaning |
|-----------|------|---------|
| `SplineMeshParams` | `FReferenceSplineMeshParams` | The road-aware geometry of **this one segment** (detailed below). |
| `TargetActor` | `AActor` | The road actor to attach your generated components / actors to. |
| `bIsPreview` | `bool` | `true` during a live in-editor preview build, `false` for the final bake. Keep preview work cheap — skip collision and expensive setup. |

`GenerateAsset()` is a `const` Blueprint event: it doesn't return anything and shouldn't mutate the descriptor — it
**builds** geometry onto `TargetActor` (add a component, spawn an actor) each time it is called.

### `FReferenceSplineMeshParams` — one segment

`FReferenceSplineMeshParams` is everything you need to place geometry for a single segment. The pipeline has already
resolved the anchor (Alignment / Alpha), the lane width, and the per-key transform channels into a plain **Hermite
spline segment** plus the lane widths at each end:

| Field | Meaning |
|-------|---------|
| `StartPos` / `EndPos` | Segment endpoints, in the road actor's local space. |
| `StartTangent` / `EndTangent` | Hermite tangents — the segment curves smoothly between them. |
| `StartScale` / `EndScale` · `StartRoll` / `EndRoll` · `StartOffset` / `EndOffset` | The per-key `Scale` / `Roll` / `Offset` transform, resolved for this segment. |
| `StartLeftWidth` / `StartRightWidth` · `EndLeftWidth` / `EndRightWidth` | Distance [cm] from the anchor to the left / right lane boundary at each end — use these to size geometry to the lane. |

It **extends** `FSplineMeshParams`, so it drops straight into a `USplineMeshComponent` (its `SplineParams`) — that is
exactly how the built-in [Spline Mesh](/attributes/SplineMeshAttribute.md) type works.

```{image} /img/generate-segment.svg
:align: center
:width: 620px
:alt: One segment is a Hermite spline (StartPos/EndPos plus tangents) carrying the lane widths at each end; the two helper functions sample a transform and the widths at any point along it.
```

### Two Blueprint helpers

Because a segment is a curved span, you rarely want the raw endpoints — you want a point *along* it. Two static
Blueprint-callable helpers on the base class do the math for you (both take `Alpha` in `[MinT, MaxT]`, default `0..1`):

- **`CalcSliceTransformAtSplineOffset(SplineMeshParams, Alpha)`** → `FTransform` — the world transform at fractional
  position `Alpha` along the segment (`0` = start, `0.5` = middle, `1` = end). It applies the same offset / roll / scale
  blending as a spline mesh, so a mesh or actor placed there sits flush with the road. This is how the
  [Component](/attributes/ComponentTemplateAttribute.md) and [Actor](/attributes/ActorTemplateAttribute.md) types place
  their object (via `ComponentToSegmentAlign` / `ActorToSegmentAlign`).
- **`CalcWidthsAtSplineOffset(SplineMeshParams, Alpha)`** → `FVector2D(LeftWidth, RightWidth)` — the interpolated lane
  half-widths at that same point. Use it to stretch geometry across the lane or to place objects at the lane edges.

### Build your own generate type

1. **Create the asset** — an [Attribute Profile](/profiles/AttributeProfile.md) with **RoadLaneAttributeGenerateDescriptor**
   (**Generate**) as the parent class, as shown in [Create new Attribute](#create-new-attribute) above.
2. **Set the descriptor defaults**: `LengthOfSegment` (segment density), `Sampler` — **By Length of Segment** for a
   continuous run, **Between Keys** for exactly one object per key interval (point objects) — `bAlignWorldUpVector`
   (vertical props like poles and signs), `bReversSplineDirection`, and the `AttributeValueTemplate` (default Alignment
   / Alpha).
3. **Override the `GenerateAsset` event** in the Blueprint graph. For each call: get a placement transform with
   `CalcSliceTransformAtSplineOffset`, size it to the lane with `CalcWidthsAtSplineOffset`, then spawn your actor / add
   your component and attach it under `TargetActor`. Branch on `bIsPreview` to keep the preview lightweight.
4. **Use it** — add the profile to a lane and place keys in the [Attribute sub-mode](/editing/AttributeMode.md).

## Drag and Drop

Drag a Generate attribute profile from the Content Browser onto a road lane to add it directly:

![Dragging a custom Generate attribute profile onto a road lane](/img/grag-and-drop-attribute-custom.gif)

## Examples

Custom Generate Attribute examples ship at **`/MetaRoad/MetaRoad/Profiles/Custom`**:

- **`CustomSample`** — a minimal Generate subclass that overrides `GenerateAsset()`.
- **`BridgeBeam`** — repeats a bridge-beam actor along the lane and computes each beam's size.

![A custom Generate Attribute building geometry along a road lane](/img/custom-attribute.gif)

## See also

- [Attribute Profile](/profiles/AttributeProfile.md) — creating Generate-attribute assets.
- [Attribute Mode](/editing/AttributeMode.md) — adding attributes and placing keys.
