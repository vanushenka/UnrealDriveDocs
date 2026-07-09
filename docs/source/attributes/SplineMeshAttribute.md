# Spline Mesh Attribute

```{note}
Inherited from **[Generate Attributes](/attributes/GenerateAttributes.md)** — shares its anchor, alignment, and per-key
transform channels.
```

Sweeps a **`Static Mesh`** into a `USplineMeshComponent` along the lane at the `LengthOfSegment` interval — ideal for
guardrails, barriers, and curbs that must bend with the road. Add it and place keys with
[Attribute Mode](/editing/AttributeMode.md).

![A spline-mesh guardrail generated along a road lane](/img/spline-attribute.gif)

## Create new Attribute

Create a new attribute from the **Content Browser** under the **Meta Road** category:

![Creating a new attribute from the Content Browser Meta Road category](/img/create-new-attribute.png)

In the **Pick Parent Class** dialog choose `RoadLaneAttributeSplineMeshDescriptor`:

![Choosing RoadLaneAttributeSplineMeshDescriptor as the parent class](/img/create-splinemesh-attribute.png)

## Properties

| Property | Description |
|----------|-------------|
| `StaticMesh` | The mesh swept into a `USplineMeshComponent` along each segment. |
| `BodyInstance` | Collision settings applied to the generated spline mesh. |
| `LengthOfSegment` | Target arc-length [cm] of each generated segment (segment density). |
| `Sampler` | How the lane is subdivided — **By Length of Segment** or **Between Keys**. |

For the shared per-key transform channels (`Alpha`, `Scale`, `Offset`, `Roll`, width overrides) and `Alignment`, see
[How a Generate Attribute follows the lane](/attributes/GenerateAttributes.md#how-a-generate-attribute-follows-the-lane).

![The Spline Mesh attribute's property panel](/img/entry-spline.png)

## Drag and Drop

Drag a Spline Mesh attribute profile from the Content Browser onto a road lane to add it directly:

![Dragging a Spline Mesh attribute profile onto a road lane](/img/grag-and-drop-attribute-splinemesh.gif)

## Examples

Sample assets: `/MetaRoad/MetaRoad/Profiles/SplineMeshes`.

## See also

- [Generate Attributes](/attributes/GenerateAttributes.md) — the base family (anchor / alignment / per-key transform channels).
- [Attribute Profile](/profiles/AttributeProfile.md) — how attribute assets are created in the Content Browser.
- [Attribute Mode](/editing/AttributeMode.md) — add the attribute and place keys along a lane.
