# Sidewalk Height Attribute

Adjusts the **Z-height of sidewalk mesh vertices** at positions along the lane — for ramps or sloped curb approaches.
It modifies existing mesh vertices; it does **not** add geometry, so it works best when keys are not placed too close
together. Can only be added to **sidewalk lanes** (`FRoadZoneSidewalk`). Keys use **cubic interpolation**.

## Properties

| Property | Range | Description |
|----------|-------|-------------|
| `Height` | −100 … +100 cm | Z-offset applied to sidewalk vertices at this key position. |

![A sidewalk ramp created by adjusting vertex height along the lane](/img/sidewalk-height-attribute.gif)

## See also

- [Attribute Mode](/editing/AttributeMode.md) — add and edit this attribute along a lane.
- [Attributes](/concepts/Attributes.md) — how attributes evaluate and are stored.
- [Curb Cut Attribute](/attributes/CurbCutAttribute.md) — related sidewalk shaping.
