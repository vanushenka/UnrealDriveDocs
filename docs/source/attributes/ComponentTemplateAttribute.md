# Component Template Attribute

```{note}
Inherited from **[Generate Attributes](/attributes/GenerateAttributes.md)** — shares its anchor, alignment, and per-key
transform channels.
```

Places any **`USceneComponent`** repeatedly along the lane at the `LengthOfSegment` interval — convenient for repeating
props such as traffic cones, flagpoles, lamp posts, and power lines. Add it and place keys with
[Attribute Mode](/editing/AttributeMode.md).

![Scene components repeated along a road lane](/img/component-attribute.gif)

## Create new Attribute

Create a new attribute from the **Content Browser** under the **Meta Road** category:

![Creating a new attribute from the Content Browser Meta Road category](/img/create-new-attribute.png)

In the **Pick Parent Class** dialog choose **RoadLaneAttributeComponentTemplateDescriptor**:

![Choosing RoadLaneAttributeComponentTemplateDescriptor as the parent class](/img/create-component-attribute.png)

## Properties

| Property | Description |
|----------|-------------|
| `ComponentTemplate` | The `USceneComponent` subclass instantiated once per segment. If it is a `USplineMeshComponent`, the segment's spline params are applied to it. |
| `ComponentToSegmentAlign` | Placement point within the segment [0 = start, 0.5 = mid, 1 = end]. |
| `LengthOfSegment` | Target arc-length [cm] of each generated segment (segment density). |
| `Sampler` | How the lane is subdivided — **By Length of Segment** or **Between Keys** (one component per key interval). |

For the shared per-key transform channels (`Alpha`, `Scale`, `Offset`, `Roll`, width overrides) and `Alignment`, see
[How a Generate Attribute follows the lane](/attributes/GenerateAttributes.md#how-a-generate-attribute-follows-the-lane).

![The Component Template attribute's property panel](/img/entry-component.png)

## Drag and Drop

Drag a Component Template attribute profile from the Content Browser onto a road lane to add it directly:

![Dragging a Component Template attribute profile onto a road lane](/img/grag-and-drop-attribute-component.gif)

## Examples

Sample assets: `/MetaRoad/MetaRoad/Profiles/Componets`.

## See also

- [Generate Attributes](/attributes/GenerateAttributes.md) — the base family (anchor / alignment / per-key transform channels).
- [Attribute Profile](/profiles/AttributeProfile.md) — how attribute assets are created in the Content Browser.
- [Attribute Mode](/editing/AttributeMode.md) — add the attribute and place keys along a lane.
