# Cross Section Attribute

Shapes the road **across** its width: sinks the driving surface toward the edge of the driveable area — a gutter,
so water runs off the lane instead of standing on it. Keys blend **smoothly** along the road.

![Alt](/img/edge-profile.png)

```{important}
Two prerequisites, both in the road's [Triangulation](/baking/Triangulation.md#edge-profile) settings:
`Edge Profile` must be **on**, and `Surface Density Mode` must not be `None`. Without interior vertices to bend,
the gutter comes out as one straight wedge whatever you set here.
```

## Where it can be added

The **section center line only** — select the section, then add the attribute. It is not offered on an individual
lane: the profile describes the whole cross-section, and two lanes must not disagree about a shared vertex.

## Properties

| Property | Default | Description |
|----------|---------|-------------|
| `Depth` | 30 cm | How far the surface is lowered at the edge [0–50 cm]. `0` = flat, no gutter |
| `Falloff Width` | 150 cm | How far the drop reaches inward [1–1000 cm]. Beyond it the surface is flat |
| `Exponent` | 2.0 | Shape of the falloff [0.05–5] |

```{image} /img/cross-section-exponent.svg
:align: center
:width: 470px
:alt: Three edge profiles sharing one Depth and Falloff Width, drawn at Exponent 2, 1 and 0.5
```

Everything outside the driving surface — a shoulder, a sidewalk — rides down as a flat plateau at the full
`Depth`, so a curb standing on it keeps its own height.

```{tip}
Keep `Target Edge Length` comfortably below `Falloff Width` — say 50 against 150. The falloff needs several
vertices across it, or every `Exponent` looks the same.
```

## See also

- [Attribute Mode](/editing/AttributeMode.md) — add and edit this attribute along a road.
- [Triangulation](/baking/Triangulation.md#edge-profile) — the `Edge Profile` switch and surface density.
- [Curb Cut Attribute](/attributes/CurbCutAttribute.md) *(Pro)* — lowers a sidewalk at a crossing; also needs surface density.
- [Sidewalk Height Attribute](/attributes/SidewalkHeightAttribute.md) — varies a sidewalk's height along its length, rather than across the road.
