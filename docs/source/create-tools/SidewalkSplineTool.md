# Sidewalk Spline Tool (Pro)

```{note}
This is the **Sidewalk** tile in the **Create** palette of the Meta Road editor mode
(see [The Meta Road Editor Mode](/editor-mode/MetaRoadEditorMode.md)). *(Pro feature.)*
```

<!-- TODO 📷 screenshot: Sidewalk tool active in the Create palette → /img/sidewalk-mode.png -->

The **Sidewalk Spline Tool** draws a **sidewalk spline** (`USidewalkSplineComponent`) — a closed
[detail spline](/concepts/DetailSplines.md) that fills its outline with a raised **sidewalk surface** and sweeps a
**curb** along its boundary. It is added to the selected road actor and participates in
[baking](/baking/BakeStaticMesh.md) together with the road surface. (It is essentially a "looped mark spline
without chevrons".)

## Requirements

Select one actor that contains a `URoadSplineComponent` before activating the tool.

## Drawing a sidewalk

1. Select the road actor and activate the **Sidewalk** tile.
2. **Click** in the viewport to append points around the island outline (at least 3). A sidewalk spline is always
   a **closed loop** — the outline closes automatically.
3. **Click-drag** to reposition the last point.
4. **Accept** to commit the `USidewalkSplineComponent` to the selected actor, or **Cancel** to discard.

<!-- TODO 🎞 gif: drawing a sidewalk island outline → /img/sidewalk-life.gif -->

```{tip}
Link the boundary nodes onto the road's lane edge (select a node, then hold `Space` and drag) and toggle **Magnetic Segment** so the sidewalk hugs the
curb line exactly as the road curves — see [Detail Splines → Magnetism](/concepts/DetailSplines.md#magnetism).
```

## Properties

**Component-wide** (the component's **Details** panel):

| Property | Default | Description |
|----------|---------|-------------|
| `Sidewalk Zone` | `Sidewalk` | The [sidewalk Road Zone](/concepts/RoadZones.md) filling the enclosed area — its surface material, default height, and curb configuration (curb profile/material) drive both the fill and the boundary curb |

**Per-point** (in the spline's **Selected Points** section — select one or more points first):

| Property | Default | Description |
|----------|---------|-------------|
| `Override Height` / `Height` | off / 15 | Override the sidewalk surface height at this node, cm (otherwise the zone's default) |
| `Override Curb Profile` / `Curb Profile` | off / — | Override the [Curb Profile](/profiles/CurbProfile.md) for this node's boundary segment |

The **Node Link**, **Break Link**, and **Magnetic Segment** rows in the same section control the spline's
magnetism — see [Detail Splines](/concepts/DetailSplines.md).

<!-- TODO 📷 screenshot: the sidewalk per-point properties in the Selected Points section → /img/sidewalk-details.png -->

## Next steps

- [Detail Splines](/concepts/DetailSplines.md) — anchor nodes to the road and use magnetic segments.
- [Bake](/baking/BakeStaticMesh.md) to generate the sidewalk surface and curb together with the road.
