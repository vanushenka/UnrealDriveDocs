# Curb Cut Attribute (Pro)

Creates **curb cuts** (dropped curbs) on sidewalks — the lowered ramp where a sidewalk meets a crossing or driveway.
It reshapes the sidewalk's curb procedurally at each key position. Can only be added to **sidewalk lanes**.

## Properties

| Property | Default | Description |
|----------|---------|-------------|
| `bIsCross` | off | Symmetric "cross" cut. When on, only the *begin* width/falloff are used and `WidthB` / `FalloffB` / `Alpha` are ignored. |
| `WidthA` | 200 cm | Width of the cut at its begin. |
| `FalloffA` | 50 cm | Falloff (blend distance) at the begin. |
| `WidthB` | 200 cm | Width of the cut at its end (when `bIsCross` is off). |
| `FalloffB` | 0 cm | Falloff at the end (when `bIsCross` is off). |
| `Alpha` | 0.5 | Lateral position of the cut's end across the lane width [0.1 = inner edge … 0.5 = center … 1.0 = outer edge] (when `bIsCross` is off). |
| `MeshDensity` | 4 | Subdivision density of the generated cut mesh [1–10]. |
| `bSmooth` | off | Smooth (rounded) rather than sharp transition. |

![A curb cut (dropped curb) generated on a sidewalk](/img/curb-cut.gif)

## See also

- [Attribute Mode](/editing/AttributeMode.md) — add and edit this attribute along a lane.
- [Attributes](/concepts/Attributes.md) — how attributes evaluate and are stored.
- [Sidewalk Height Attribute](/attributes/SidewalkHeightAttribute.md) — related sidewalk shaping.
