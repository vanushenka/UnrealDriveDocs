# Landscape Attribute (Pro)

Controls how the Unreal Engine **landscape deforms** along the road. Add it to the **center lane (lane index 0)** of a
`URoadSplineComponent` that has a landscape assigned. Only one Landscape Attribute is allowed per lane section. Keys use
**cubic interpolation**, so height and falloff transition smoothly.

## Properties

| Property | Default | Description |
|----------|---------|-------------|
| `LayerFactor` | 1.0 | Landscape layer blend weight at this key [0–1]. |
| `SideFalloff` | 1000 | Distance [cm] over which the landscape modification fades out laterally. |
| `SideOffset` | 0 | Lateral offset of the deformation zone from the reference line. |
| `HeightOffset` | 50 | Z-height offset applied to landscape vertices under the road. |

![The landscape deforming along a road](/img/landscape-attribute.gif)

## See also

- [Attribute Mode](/editing/AttributeMode.md) — add and edit this attribute along a lane.
- [Attributes](/concepts/Attributes.md) — how attributes evaluate and are stored.
- [Landscape](/integrations/Landscape.md) — the landscape integration this attribute drives.
