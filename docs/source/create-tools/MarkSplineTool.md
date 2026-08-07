# Mark Spline Tool (Pro)

```{note}
This is the **Mark** tile in the **Create** palette of the Meta Road editor mode
(see [The Meta Road Editor Mode](/editor-mode/MetaRoadEditorMode.md)). *(Pro feature.)*
```

![Mark tool active in the Create palette](/img/chevron-mode.png)

Draws a **mark spline** — a [detail spline](/concepts/DetailSplines.md) for road markings, added to the selected
road actor and baked together with the road. One spline can carry all five marking features at once.

## Drawing a mark spline

Select an actor containing a road spline, activate the **Mark** tile, then:

1. **Click** to append a point; **click-drag** to reposition the last one.
2. **Accept** to commit, or **Cancel** to discard.

![Drawing a mark spline outline](/img/chevron-life.gif)

The preview shows the real marking, not a sketch — the stripe, the stamps, the pattern lines and the chevron
islands are all built as you draw.

```{tip}
Link the outline nodes to the road and toggle **Magnetic Segment** so the marking follows the road edge as you
keep editing — see [Detail Splines → Magnetism](/concepts/DetailSplines.md#magnetism).
```

## Where a setting lives

Every marking feature is one **property group**, and the same group appears in up to three places:

| Source | Where | Scope |
|--------|-------|-------|
| **Tool** | the Mark tool's panel while you draw | Seeds the component you are about to create |
| **Component** | the mark spline's **Details** panel | The whole spline |
| **Node** | the spline's **Selected Points** section | Overrides the group for the selected node(s) only |

A node override is an `Override …` checkbox plus its own copy of the group: tick it and that node stops following
the component. Three of the five features can be overridden per node:

| Feature | Tool | Component | Per node |
|---------|:----:|:---------:|:--------:|
| [Mark Profile](#mark-profile) — the stripe | ✔ | ✔ | ✔ |
| [Chevron guide-islands](#chevron-guide-islands) | ✔ | ✔ | ✔ |
| [Polygon stamps](#polygon-stamps) | ✔ | ✔ | ✔ |
| [Looped zone fill](#looped-zone-fill) | ✔ | ✔ | — |
| [Fill pattern](#fill-pattern) | ✔ | ✔ | — |

## Mark Profile

The stripe swept along the spline — a solid or dashed line following a [Mark Profile](/profiles/MarkProfile.md).

![A mark spline sweeping a stripe along a lane edge, with a second stripe in another profile after an override node](/img/mark-profile-result.png)

| Property | Default | Description |
|----------|---------|-------------|
| `Profile Source` | `Use Preset` | `Use Preset` takes the stripe from the road's own preset; `Use Custom` uses the `Profile` below |
| `Profile` | — | The [Mark Profile](/profiles/MarkProfile.md) asset — type, width, dash pattern and default material |
| `Override Material` | off | Replace the profile's material for this stripe only |

**Per node:** `Override Mark Profile` replaces the whole group for the stripe segment **leaving** that node.

```{tip}
Because the material override sits on the *stripe*, one spline can sweep the same profile in two colors — switch
it at a node instead of splitting the spline.
```

![The Mark Profile group in all three places: the Mark tool panel, the component Details panel and a node's Override Mark Profile](/img/mark-profile-sources.png)

## Chevron guide-islands

The striped "V" islands painted where traffic flows split or merge. Each interior node with **Draw Chevron
Marking** on becomes the apex of a wedge filled with chevron bands.

![A chevron guide island painted at a gore point where an off-ramp splits from the main road](/img/mark-chevron-result.png)


| Property | Default | Description |
|----------|---------|-------------|
| `Section Size` / `Section Interval` | 100 / 200 | Depth of one chevron band and the gap between bands, cm |
| `Road Zone` | `Marking` | Surface zone of the chevron polygons, carrying its own material and UV-density overrides |
| `Texture` | — | `Angle` / `Scale` / `Shift` — see [Per-shape Texture group](/baking/Texturing.md#per-shape-texture-group) |

**Per node:** `Draw Chevron Marking` turns the island on, `Size (cm)` and `Offset (cm)` set its length along the
wedge bisector and where it starts, `Reverse Direction` flips which end the chevrons point at, and
`Override Chevron Profile` replaces the whole group above for this island.

```{note}
The tool has an extra **`Draw`** master toggle that the component does not: it turns chevrons on for every node
you place and greys out the rest of the group while off. If you draw a spline and get no chevrons, this is why.
```

![The Chevron Profile group in all three places: the Mark tool panel with its Draw master toggle, the component Details panel and a node's Override Chevron Profile](/img/mark-chevron-sources.png)  

```{important}
**Breaking change in 3.1.0.** The flat chevron properties were folded into this group without redirects, so saved
`Section Size`, `Section Interval`, `Road Zone` and `Texture` values **reset to their defaults** on the first
load, and the `Road Zone` default changed from `Driving` to `Marking`.
```

## Polygon stamps

A [Polygon Profile](/profiles/PolygonProfile.md) shape repeated along the spline, oriented to the tangent — turn
arrows, repeated hatching and the like.

![Turn arrows stamped along a lane at a fixed interval, each oriented to the spline tangent](/img/mark-polygon-result.png)

| Property | Default | Description |
|----------|---------|-------------|
| `Profile` | — | The [Polygon Profile](/profiles/PolygonProfile.md) asset stamped along the spline |
| `Interval` | 500 | Spacing between consecutive stamps, cm |

**Per node:** `Override Polygon Profile` replaces the shape and spacing for the segment **leaving** that node.
Spacing is measured as one continuous march along the whole spline, so an override changes the shape from that
node onward without restarting the phase or double-stamping.

```{note}
**New in 3.2.0.** Stamps carry their [holes](/profiles/PolygonProfile.md#holes) into the mesh, so a stamp can be a
ring or a stencil. Placed over a road lane, it shows the road surface through them.
```

![The Polygon Profile group in all three places: the Mark tool panel, the component Details panel and a node's Override Polygon Profile](/img/mark-polygon-sources.png)

## Looped zone fill

Fills the area enclosed by a **closed** spline with a surface zone — a marking island.

![A closed mark spline filled solid as a painted island between two diverging lanes](/img/mark-looped-zone-result.png)

| Property | Default | Description |
|----------|---------|-------------|
| `Draw Looped Zone` | off | Fill the enclosed area. Needs a closed loop |
| `Looped Road Zone` | `Driving` | The surface zone that fills it |
| `Texture` | — | `Angle` / `Scale` / `Shift` of the fill's UVs |

**No per-node override** — the fill belongs to the whole loop.

![The Looped Road Zone group in the Mark tool panel and in the component Details panel](/img/mark-looped-zone-sources.png)

## Fill pattern

Paints a repeating *marking* over the area enclosed by a closed spline — a box junction, or the diagonal hatching
of a guide island. The lines are ordinary mark stripes, each swept with a Mark Profile.

It is independent of the looped zone fill: that lays down a surface *zone*, this paints a *marking*. Use either,
both or neither.

![The two patterns side by side: a yellow waffle box junction over an intersection, and a diagonally hatched guide island](/img/mark-fill-pattern-result.png)

| Property | Default | Description |
|----------|---------|-------------|
| `Pattern` | `None` | `Waffle (Box Junction)` — two perpendicular families of lines; `Diagonal Hatch (Guide Island)` — one family |
| `Mark` | — | The [Mark Profile group](#mark-profile) swept along every line. **Nothing draws until this is set** |
| `Cell Size (cm)` | 200 | Distance between consecutive parallel lines |
| `Orientation` / `Angle (deg)` | `World Axes` / 0 | What the angle is measured from, and the rotation on top. A guide island is conventionally `Loop Axis` + 45°; a junction box `World Axes` + 0° |
| `Shift (cm)` / `Inset (cm)` | (0, 0) / 0 | Phase shift of the grid, and clearance between the line ends and the boundary |

**No per-node override** — the pattern belongs to the whole loop.

![The Fill Pattern group in the Mark tool panel and in the component Details panel](/img/mark-fill-pattern-sources.png)

## Drawing settings

These exist only on the tool, and shape the spline as you place it:

| Property | Default | Description |
|----------|---------|-------------|
| `Tangent Type` | `Broken` | Tangent style given to every node you place: `Broken`, `Linear` or `Auto` |
| `Closed Loop` | off | Close the drawn spline. Required by the looped fill and the fill pattern |
| `World Objects` / `Ground Plane` / `Click Offset` | on / on / 5 | Raycast clicks against world geometry, fall back to the Z = 0 plane, and lift the point above the hit surface |

Edits update the live preview immediately, so you can retune everything before you Accept.

The spline also carries `Sub Group` and `Chord Tolerance (cm²)`, shared with every detail spline — see
[Detail Splines](/concepts/DetailSplines.md#component-properties). A node's `Tangent Mode` and its magnetism rows
live in the same **Selected Points** section as the overrides above.

## Landscape

A **closed** mark spline flattens the area enclosed by its loop — an open one ignores the Landscape group
entirely. See [Landscape](/integrations/Landscape.md).

## Baking

A mark spline bakes into the road mesh, not one of its own — into the mesh of its `Sub Group`. Keep it in the
**same actor and sub-group** as the road it belongs to so everything fuses into one unit.

## Next steps

- [Detail Splines](/concepts/DetailSplines.md) — anchor nodes to the road and use magnetic segments.
- [Mark Profile](/profiles/MarkProfile.md) — the stripe shapes a mark spline can sweep.
- [Polygon Profile](/profiles/PolygonProfile.md) — the shapes a mark spline can stamp.
- [Bake](/baking/BakeStaticMesh.md) to generate the marking mesh together with the road.
