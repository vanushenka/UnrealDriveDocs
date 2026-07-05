# Polygon Attribute (Pro)

Places custom **2D polygon shapes** on a lane at specific arc-length positions — stop lines, arrows, hatching, or any
surface overlay that doesn't fit the standard marking system. Each key references a
[Polygon Profile](/profiles/PolygonProfile.md) asset. Keys use **stepped** evaluation.

## Properties

| Property | Description |
|----------|-------------|
| `Profile` | The [Polygon Profile](/profiles/PolygonProfile.md) asset containing the polygon shapes. |
| `Alpha` | Lateral position [0.1–1.0] within the lane width where the polygon anchor is placed (0.1 = inner edge, 0.5 = center, 1.0 = outer edge). |

![A 2D polygon overlay placed on a lane](/img/polygone-attributr.gif)

## Drag and Drop

Drag a Polygon Profile from the Content Browser onto a lane to add a Polygon key at the nearest point:

![Dragging a Polygon Profile onto a road lane](/img/grag-and-drop-poly.gif)

## See also

- [Attribute Mode](/editing/AttributeMode.md) — add and edit this attribute along a lane.
- [Attributes](/concepts/Attributes.md) — how attributes evaluate and are stored.
- [Polygon Profile](/profiles/PolygonProfile.md) — the reusable 2D polygon shapes this attribute places.
