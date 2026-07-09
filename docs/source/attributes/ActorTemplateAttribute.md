# Actor Template Attribute

```{note}
Inherited from **[Generate Attributes](/attributes/GenerateAttributes.md)** — shares its anchor, alignment, and per-key
transform channels.
```

Spawns any **`AActor`** repeatedly along the lane at the `LengthOfSegment` interval — for street furniture, signs,
lights, or any prop actor that should repeat along the road. Add it and place keys with
[Attribute Mode](/editing/AttributeMode.md).

![Actors spawned repeatedly along a road lane](/img/actor-attribute.gif)

## Create new Attribute

Create a new attribute from the **Content Browser** under the **Meta Road** category:

![Creating a new attribute from the Content Browser Meta Road category](/img/create-new-attribute.png)

In the **Pick Parent Class** dialog choose `RoadLaneAttributeActortTemplateDescriptor`:

![Choosing RoadLaneAttributeActortTemplateDescriptor as the parent class](/img/create-actor-attribute.png)

## Properties

| Property | Description |
|----------|-------------|
| `Actor` | The `AActor` subclass spawned once per segment and attached to the road actor. |
| `ActorToSegmentAlign` | Placement point within the segment [0 = start, 0.5 = mid, 1 = end]. |
| `LengthOfSegment` | Target arc-length [cm] of each generated segment (segment density). |
| `Sampler` | How the lane is subdivided — **By Length of Segment** or **Between Keys** (one actor per key interval). |

For the shared per-key transform channels (`Alpha`, `Scale`, `Offset`, `Roll`, width overrides) and `Alignment`, see
[How a Generate Attribute follows the lane](/attributes/GenerateAttributes.md#how-a-generate-attribute-follows-the-lane).

![The Actor Template attribute's property panel](/img/entry-actor.png)

## Drag and Drop

Drag an Actor Template attribute profile from the Content Browser onto a road lane to add it directly:

![Dragging an Actor Template attribute profile onto a road lane](/img/grag-and-drop-attribute-actor.gif)

## Examples

Sample assets: `/MetaRoad/MetaRoad/Profiles/Actors`.

## See also

- [Generate Attributes](/attributes/GenerateAttributes.md) — the base family (anchor / alignment / per-key transform channels).
- [Attribute Profile](/profiles/AttributeProfile.md) — how attribute assets are created in the Content Browser.
- [Attribute Mode](/editing/AttributeMode.md) — add the attribute and place keys along a lane.
