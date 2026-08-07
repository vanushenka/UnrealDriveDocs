# Sidewalk Spline Tool (Pro)

```{note}
This is the **Sidewalk** tile in the **Create** palette of the Meta Road editor mode
(see [The Meta Road Editor Mode](/editor-mode/MetaRoadEditorMode.md)). *(Pro feature.)*
```

![The Sidewalk tool active in the Create palette](/img/sidewalk-mode.png)

Draws a **sidewalk spline** — a closed [detail spline](/concepts/DetailSplines.md) that fills its outline with a
raised **sidewalk surface** and sweeps a **curb** along its boundary. Added to the selected road actor and baked
together with the road.

## Drawing a sidewalk

Select an actor containing a road spline, activate the **Sidewalk** tile, then:

1. **Click** to append points around the island outline — at least 3. The loop closes automatically.
2. **Click-drag** to reposition the last point.
3. **Accept** to commit, or **Cancel** to discard.

![Drawing a sidewalk island outline, which fills as a raised surface with a curb around it](/img/sidewalk-life.gif)

```{tip}
Link the boundary nodes onto the road's lane edge and toggle **Magnetic Segment** so the sidewalk hugs the curb
line exactly as the road curves — see [Detail Splines → Magnetism](/concepts/DetailSplines.md#magnetism).
```

## Properties

**Component-wide**, in the component's Details panel:

| Property | Default | Description |
|----------|---------|-------------|
| `Sidewalk Zone` | `Sidewalk` | The [sidewalk Road Zone](/concepts/RoadZones.md) filling the area. Its material, default height and curb configuration drive **both** the fill and the boundary curb |
| `Texture` | — | UV placement of the fill: `Angle` / `Scale` / `Shift` — see [Per-shape Texture group](/baking/Texturing.md#per-shape-texture-group) |
| `Chord Tolerance (cm²)` / `Sub Group` | 1.0 / *(empty)* | Shared with every detail spline — see [Detail Splines](/concepts/DetailSplines.md#component-properties) |

![The sidewalk properties](/img/sidewalk-details.png)

**Per-point**, in the spline's **Selected Points** section:

| Property | Default | Description |
|----------|---------|-------------|
| `Override Height` / `Height` | off / 15 | Override the surface height at this node, cm. The height ramps between neighbouring nodes |
| `Override Curb Profile` | off | Override the [Curb Profile](/profiles/CurbProfile.md) for this node's boundary segment |
| `Curb Cut` / `Curb Cut Offset` | off / 0 | Drop the curb to road level around this node — see [Curb cuts on a node](#curb-cuts-on-a-node). The offset slides the ramp along the boundary, cm |
| `Tangent Mode` | `Auto` | See [Point types and tangent modes](/concepts/DetailSplines.md#point-types-and-tangent-modes) |

![The sidewalk per-point properties in the Selected Points section](/img/sidewalk-details2.png)

## Curb cuts on a node

Turning **Curb Cut** on lowers the curb and the surface behind it into a ramp — the dropped curb where a sidewalk
meets a crossing or a driveway.

| Property | Default | Description |
|----------|---------|-------------|
| `Is Cross` | off | Crossing-style cut: full strength throughout, using the *A* shape. `Width B` and `Falloff B` are then ignored |
| `Width A` / `Falloff A` | 200 / 50 cm | The fully-lowered width at the curb, and the ramp added on each side of it |
| `Width B` / `Falloff B` | 200 / 0 cm | The same at the far edge of the cut, so it can taper inward |
| `Depth` | 200 cm | How far the cut reaches inward from the boundary |
| `Mesh Density` | 4 | Topology density of the ramp [1–10] |
| `Smooth` | off | Rounded rather than straight ramps |

![alt](/img/sidewalk-curb-cut.png)  

```{note}
This is the same payload as the [Curb Cut attribute](/attributes/CurbCutAttribute.md), so the ramp is identical
however it is authored. `Depth` replaces the attribute's `Alpha` on any ring host, which has no lane width for the
cut to be a fraction of. Like every curb cut it needs
[`Surface Density Mode`](/baking/Triangulation.md#surface-density) to be something other than `None`.
```

```{note}
**Changed in 3.2.0.** The ramp now carries across the seam into whatever the spline abuts — a road's own sidewalk
lane ramps down with it instead of standing at full height beside it. Nothing to author; it applies to existing
curb cuts on the next rebuild.
```

## Tool settings

While the tool is active, its panel carries `Sidewalk Zone` and `Texture` for the spline you are drawing, plus:

| Property | Default | Description |
|----------|---------|-------------|
| `Tangent Type` | `Broken` | Tangent style given to every node you place: `Broken`, `Linear` or `Auto` |
| `World Objects` / `Ground Plane` / `Click Offset` | on / on / 5 | Raycast clicks against world geometry, fall back to the Z = 0 plane, and lift the point above the hit surface |

## Landscape

A sidewalk spline is always closed, so the **Landscape** group always applies: assign a Landscape and the terrain
under the island levels to it. See [Landscape](/integrations/Landscape.md).

## Baking

The surface and its curb bake into the mesh of the component's `Sub Group` — keep it in the **same actor and
sub-group** as the road it borders so everything fuses into one unit.

```{note}
A free-standing island (no magnetized segments) has its curb ring **welded** into the road surface, so the
boundary no longer cracks against its own fill.
```

## Next steps

- [Detail Splines](/concepts/DetailSplines.md) — anchor nodes to the road and use magnetic segments.
- [Curb Cut Attribute](/attributes/CurbCutAttribute.md) — the same ramp authored along a sidewalk lane.
- [Bake](/baking/BakeStaticMesh.md) to generate the sidewalk and curb together with the road.
