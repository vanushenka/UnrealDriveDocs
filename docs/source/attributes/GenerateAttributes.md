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
the anchor path, splits it into segments, and calls your **Blueprint events** so you can emit whatever geometry you
want. Subclassing **Generate** in **Blueprint** is the primary way to build your own **custom attribute** — no C++
required. Use it directly when the [types](#types) above don't fit.

![The Generate Attribute Blueprint, overriding the GenerateAsset event](/img/generate-attribute-api.png)

### The generation lifecycle

Three events fire, in this order:

| Event | Fires | Use it to |
|-------|-------|-----------|
| **`BeginGenerateAsset`** | once per output actor | Prepare the actor — typically create the one component that all segments will share. |
| **`GenerateAsset`** | once per segment | Emit the geometry for that segment. |
| **`EndGenerateAsset`** | once per output actor | Finalize what `BeginGenerateAsset` created (rebuild an instanced-mesh tree, bounds, …). |

```{image} /img/generate-lifecycle.svg
:align: center
:width: 620px
:alt: BeginGenerateAsset fires once per output actor, GenerateAsset once per segment, EndGenerateAsset once at the end; all three reach the same generated component through the Get Or Add Generated Component node.
```

"Once per output actor" is exact: a road split into several [sub-groups](/concepts/Workflow.md) bakes into several
meshes but still into a **single** `_Gen` actor, and the Begin/End pair fires once for it — not once per sub-group. In
the live preview each build target is its own actor, so the pair fires once per preview rebuild.

```{important}
The descriptor is a **shared default object** — one instance for the whole editor, used by every road at once. A
Blueprint variable set on it would be overwritten by the next road, so **never store the component you created in a
variable**. Hand it from `BeginGenerateAsset` to `GenerateAsset` with
[Get Or Add Generated Component](#creating-components-that-persist) instead: it identifies the component by a tag on
the actor, which is per-actor state and therefore safe.
```

### What `GenerateAsset` receives

The event fires once for every segment the pipeline produced along the lane:

| Parameter | Type | Meaning |
|-----------|------|---------|
| `SplineMeshParams` | `FReferenceSplineMeshParams` | The road-aware geometry of **this one segment** (detailed below). |
| `TargetActor` | `AActor` | The **output** actor to build on — the generated `_Gen` actor when baking, a temporary actor in the live preview. Not the road actor itself. |
| `bIsPreview` | `bool` | `true` during a live in-editor preview build, `false` for the final bake. Keep preview work cheap — skip collision and expensive setup. |

`BeginGenerateAsset` and `EndGenerateAsset` receive the same `TargetActor` and `bIsPreview`, just without the segment.

`GenerateAsset()` is a `const` Blueprint event: it doesn't return anything and shouldn't mutate the descriptor — it
**builds** geometry onto `TargetActor` each time it is called, either by
[creating a component](#creating-components-that-persist) or by spawning an actor and attaching it.

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

### Placing geometry along a segment

Because a segment is a curved span, you rarely want the raw endpoints — you want a point *along* it. Two static
Blueprint-callable helpers on the base class do the math for you (both take `Alpha` in `[MinT, MaxT]`, default `0..1`):

- **`CalcSliceTransformAtSplineOffset(SplineMeshParams, Alpha)`** → `FTransform` — the world transform at fractional
  position `Alpha` along the segment (`0` = start, `0.5` = middle, `1` = end). It applies the same offset / roll / scale
  blending as a spline mesh, so a mesh or actor placed there sits flush with the road. This is how the
  [Component](/attributes/ComponentTemplateAttribute.md) and [Actor](/attributes/ActorTemplateAttribute.md) types place
  their object (via `ComponentToSegmentAlign` / `ActorToSegmentAlign`).
- **`CalcWidthsAtSplineOffset(SplineMeshParams, Alpha)`** → `FVector2D(LeftWidth, RightWidth)` — the interpolated lane
  half-widths at that same point. Use it to stretch geometry across the lane or to place objects at the lane edges.

### Creating components that persist

```{warning}
**Do not use Unreal's built-in "Add Component" node here.** A component added that way is marked as
*construction-script created*. The generated actor has no construction script to recreate it, so Unreal deletes it
again at the first opportunity — moving the actor, editing any property, reloading the level, undoing, or pressing
Play. The symptom is confusing: the component renders, never appears in the actor's Details panel, and then silently
disappears.
```

Use these nodes instead. They set the component up the same way the built-in attribute types do, so it shows up in the
Details panel, survives every rebuild, is saved with the level, and exists in Play:

| Node | Behaviour | Use in |
|------|-----------|--------|
| **`Get Or Add Generated Component`** | Creates the component on the first call, finds it on every later one. The `Was Created` output tells you which happened. | One component shared by the whole run: created in `BeginGenerateAsset`, fetched back in `GenerateAsset`. |
| **`Add Generated Component`** | Always creates another component. | One component **per segment**, from `GenerateAsset` — what the built-in [Spline Mesh](/attributes/SplineMeshAttribute.md) type does. |
| **`Get Default Component`** | Finds only, never creates — returns nothing if it does not exist yet. | Branching on "did I already prepare this actor?" |

All of them take the **Target Actor** and the **Component Class** you want. The two that create also take the event's
**Is Preview** pin — preview components are made without collision, so previews stay cheap.

They identify the component by a **tag** they put on it. The two creating nodes expose that tag on a `Tag` pin in
their advanced (collapsed) section, and you normally leave it alone: when empty it defaults to your descriptor's own
class, which is unique per attribute. Set it explicitly only when **one** descriptor creates **several** components
and has to tell them apart — for example posts and rails. `Get Default Component` always looks up that default tag.

```{note}
`Add Generated Component` exists because `Get Or Add Generated Component` cannot make one component per segment: the
tag is the component's identity, and `GenerateAsset` has no segment number to build a unique tag from, so it would
keep handing you the first segment's component.

If a single descriptor uses **both** patterns — a shared component plus per-segment ones — give at least one of them
an explicit `Tag`, otherwise they share the default tag and a lookup may return the wrong one.
```

### Build your own generate type

1. **Create the asset** — an [Attribute Profile](/profiles/AttributeProfile.md) with **RoadLaneAttributeGenerateDescriptor**
   (**Generate**) as the parent class, as shown in [Create new Attribute](#create-new-attribute) above.
2. **Set the descriptor defaults**: `LengthOfSegment` (segment density), `Sampler` — **By Length of Segment** for a
   continuous run, **Between Keys** for exactly one object per key interval (point objects) — `bAlignWorldUpVector`
   (vertical props like poles and signs), `bReversSplineDirection`, and the `AttributeValueTemplate` (default Alignment
   / Alpha).
3. **Override the events** in the Blueprint graph, picking the pattern that fits:

   - *One component per segment* — override `GenerateAsset` only. Per call: place it with
     `CalcSliceTransformAtSplineOffset`, size it to the lane with `CalcWidthsAtSplineOffset`, and create it with
     **`Add Generated Component`**.
   - *One shared component* (instanced meshes, a single procedural mesh) — create it in `BeginGenerateAsset` with
     **`Get Or Add Generated Component`**, feed it from `GenerateAsset` with the same node, and finalize it in
     `EndGenerateAsset`.

   Branch on `bIsPreview` to keep the preview lightweight, and do one-time setup (assigning the mesh, materials) under
   the `Was Created` output so it does not run for every segment.
4. **Use it** — add the profile to a lane and place keys in the [Attribute sub-mode](/editing/AttributeMode.md).

For example, an attribute that scatters an instanced mesh along the lane is three nodes: `Get Or Add Generated
Component` (class = `InstancedStaticMeshComponent`) in `BeginGenerateAsset`, with the mesh assigned under
`Was Created`; the same node in `GenerateAsset` followed by **Add Instance** fed from
`CalcSliceTransformAtSplineOffset`; and, for a hierarchical instanced mesh, **Build Tree If Outdated** in
`EndGenerateAsset`.

## Drag and Drop

Drag a Generate attribute profile from the Content Browser onto a road lane to add it directly:

![Dragging a custom Generate attribute profile onto a road lane](/img/grag-and-drop-attribute-custom.gif)

## Examples

Custom Generate Attribute examples ship at **`/MetaRoad/MetaRoad/Profiles/Custom`**:

- **`CustomSample`** — a minimal Generate subclass that overrides `GenerateAsset()`.
- **`BridgeBeam`** — repeats a bridge-beam actor along the lane and computes each beam's size.
- **`InstancedMeshSample`** — the shared-component pattern: one instanced-mesh component built in
  `BeginGenerateAsset`, one instance added per segment.

![A custom Generate Attribute building geometry along a road lane](/img/custom-attribute.gif)

## See also

- [Attribute Profile](/profiles/AttributeProfile.md) — creating Generate-attribute assets.
- [Attribute Mode](/editing/AttributeMode.md) — adding attributes and placing keys.
