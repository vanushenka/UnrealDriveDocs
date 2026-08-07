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

They all derive from the **Generate** base class, so they share the anchor, alignment and per-key
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

## Build your own

Subclassing **Generate** in Blueprint is the primary way to build a custom attribute — the pipeline hands you one
road-aware segment at a time and you emit whatever geometry you like. See
**[Generate Attributes — Blueprint API](/attributes/GenerateBlueprintAPI.md)**.

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
