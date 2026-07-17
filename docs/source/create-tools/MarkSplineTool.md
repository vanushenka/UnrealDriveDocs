# Mark Spline Tool (Pro)

```{note}
This is the **Mark** tile in the **Create** palette of the Meta Road editor mode
(see [The Meta Road Editor Mode](/editor-mode/MetaRoadEditorMode.md)). *(Pro feature.)*
```

![Mark tool active in the Create palette](/img/chevron-mode.png)

The **Mark Spline Tool** draws a **mark spline** (`UMarkSplineComponent`) — a [detail spline](/concepts/DetailSplines.md)
for road markings, added to the selected road actor. A mark spline can draw:

- **chevron guide-island markings** — the striped "V" islands painted at gore points where traffic flows split or
  merge (for example at off-ramps);
- a **stripe** following a [Mark Profile](/profiles/MarkProfile.md);
- a filled **marking island** when the spline is a closed loop.

It participates in [baking](/baking/BakeStaticMesh.md) together with the road surface.

## Requirements

Select one actor that contains a `URoadSplineComponent` before activating the tool.

## Drawing a mark spline

1. Select the road actor and activate the **Mark** tile.
2. **Click** in the viewport to append a **sharp (linear) point** to the outline. A live preview renders as you go.
3. **Click-drag** to reposition the last point.
4. **Accept** to commit the `UMarkSplineComponent` to the selected actor, or **Cancel** to discard.

![Drawing a mark spline outline](/img/chevron-life.gif)

At each interior point with **Draw Chevron Marking** on, the point is the apex of a wedge between the two tangent
directions; the wedge is filled with chevron V-bands. Open-spline endpoints are skipped. Enable the closed-loop
option to fill the enclosed area as a marking island instead.

```{tip}
Link the outline nodes to the road (select a node, then hold `Space` and drag onto a lane corner) and toggle **Magnetic Segment** so the marking
follows the road edge as you keep editing — see [Detail Splines → Magnetism](/concepts/DetailSplines.md#magnetism).
```

## Properties

**Component-wide** (the component's **Details** panel):

| Property | Default | Description |
|----------|---------|-------------|
| `Chevron Section Size` | 100 | Depth of one chevron band (the "V") along the wedge bisector, cm |
| `Chevron Section Interval` | 200 | Gap between consecutive chevron bands, cm |
| `Chevron Road Zone` | `Driving` | Road surface type (material/color) applied to the chevron polygons |
| `Chevron Texture Angle` | 0° | UV texture rotation for the chevrons, in degrees |
| `Chevron Texture Scale` | 1.0 | UV texture scale for the chevrons |
| `Mark Profile` | — | Base [Mark Profile](/profiles/MarkProfile.md) (stripe type/dimensions/material) for the spline |
| `Draw Looped Zone` | off | Fill the enclosed area when the spline is closed (needs a closed loop + valid zone) |
| `Looped Road Zone` | `Driving` | Surface zone that fills the closed-loop marking island |
| `Looped Road Zone Tex Angle` / `Tex Scale` | 0° / 1.0 | UV texture rotation/scale for the looped fill |

**Per-point** (in the spline's **Selected Points** section — select one or more points first):

| Property | Default | Description |
|----------|---------|-------------|
| `Draw Chevron Marking` | off | Generate a chevron island at the selected point(s) |
| `Size (cm)` | 1000 | Island length along the wedge bisector — drives how many chevron bands fill the island |
| `Offset (cm)` | 0 | Distance from the node where the chevrons start; shifts the whole `Size` region away from the node (drawn region = `[Offset, Offset + Size]`) |
| `Reverse Direction` | off | Flip the chevron pointing direction — toward the node apex (off) or the wide end of the island (on) |
| `Override Mark Profile` / `Mark Profile` | off / — | Override the base Mark Profile for this node's stripe segment |

The **Node Link**, **Break Link**, and **Magnetic Segment** rows in the same section control the spline's
magnetism — see [Detail Splines](/concepts/DetailSplines.md).

![The mark per-point properties in the Selected Points section](/img/chevron-deatils.png)

<!-- TODO 📷 screenshot: a mark spline drawing a stripe along a lane (Mark Profile) -->
<!-- TODO 📷 screenshot: a closed mark spline filled as a marking island -->

## Next steps

- [Detail Splines](/concepts/DetailSplines.md) — anchor nodes to the road and use magnetic segments.
- [Bake](/baking/BakeStaticMesh.md) to generate the marking mesh together with the road.
