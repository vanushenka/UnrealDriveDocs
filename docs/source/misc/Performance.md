# Performance

```{note}
These settings live in **Edit → Project Settings → Plugins → MetaRoad Editor → Performance**, not in the
**Visibility** tile of the editor mode (see [Visibility](/misc/Visibility.md)).
```

The Schematic view draws the lane fills, the lane and section boundary lines, the crosswalk outlines and the detail
spline previews **every frame, for every open viewport**. On a city-sized network seen from a wide camera that is
thousands of lines a frame for a picture only a few pixels tall, and it is the main reason the viewport slows down as
the level grows.

MetaRoad therefore drops the schematic to a cheaper level as the camera moves away, and stops drawing it entirely past
a second threshold. This is a **view-only** system: it changes nothing about the road data, the
[baked meshes](/baking/BakeStaticMesh.md), the live Preview mesh or the
[Landscape deformation](/integrations/Landscape.md) — only how much of the editor overlay is drawn at a given zoom.

## The three detail levels

| Level | What is drawn |
|-------|---------------|
| **Full** | Everything — lane fills, lane and section boundary lines, the direction arrow of the selected spline, crosswalk outlines and center lines, detail spline outlines and the green magnetic dashes |
| **Simplified** | The filled surfaces only. The per-segment lines are dropped, which is where nearly all the cost is. Roads and detail splines stay **clickable**, because the fill itself carries the click target |
| **Culled** | Nothing. The component also stops producing click targets, so it cannot be picked in the viewport until you come back within range |

Each component is measured on its **own bounds**, so a road at the far end of the level drops out while the junction
under the camera keeps full detail. The level is decided per viewport and per frame — a perspective view and a Top view
open side by side can legitimately show the same road at different levels.

```{note}
There is no fade and no hysteresis: the level flips exactly when you cross the threshold. That is deliberate — the
level is a pure function of the camera, so it can only change when you move.
```

## Perspective and orthographic viewports are measured differently

Exactly one metric applies per projection, and the other pair of settings is ignored.

- **Perspective viewports** use the **distance in centimetres** from the camera to the *nearest point of the
  component's bounds* — not to its center, so a 2 km road whose far end is out of range still draws while its near end
  is under the camera. Driven by `Visualization Cull Distance` / `Visualization Simplify Distance`.
- **Orthographic viewports** (Top, Front, Side) use **world centimetres per screen pixel**. Zooming an orthographic
  viewport does not move the camera, so distance means nothing there; what changes is how much world one pixel covers,
  which equals the ortho width divided by the viewport width in pixels. Driven by
  `Visualization Cull World Per Pixel` / `Visualization Simplify World Per Pixel`.

```{tip}
Because the orthographic thresholds are per **pixel**, a larger or higher-resolution viewport shows more of the network
before it simplifies. At the default 30 cm/px, a 1920-pixel-wide Top view stays at full detail until it spans roughly
580 m of world.
```

## Settings

**Edit → Project Settings → Plugins → MetaRoad Editor → Performance**. They are project settings, shared by everyone
working on the project.

| Setting | Default | Description |
|---------|---------|-------------|
| `Enable View LOD` | on | Master switch. Clear it to restore the pre-3.1.0 behavior exactly: everything draws at full detail at any distance and nothing is ever culled. The four settings below are greyed out while it is off |
| `Visualization Cull Distance` | 150000 cm (1.5 km) | **Perspective only.** Beyond this camera distance the schematic is not drawn at all |
| `Visualization Simplify Distance` | 40000 cm (400 m) | **Perspective only.** Beyond this camera distance the schematic drops to the simplified level (fill only, no boundary lines) |
| `Visualization Cull World Per Pixel` | 120 | **Orthographic only.** Above this many world centimetres per screen pixel the schematic is not drawn at all |
| `Visualization Simplify World Per Pixel` | 30 | **Orthographic only.** Above this many world centimetres per screen pixel the schematic drops to the simplified level |

![The Performance category in Project Settings, Plugins, MetaRoad Editor](/img/performance-settings.png)

Set them by feel rather than by arithmetic: zoom out until the viewport looks emptier than you want, then raise the
matching threshold (distance for a perspective view, world-per-pixel for a Top view) until the schematic comes back at
the zoom you actually work at. Keep each *simplify* value below its *cull* value — the simplified level is what keeps a
large network readable in the range where the lines would be sub-pixel anyway.

## What it applies to

The view LOD is applied by the schematic drawing itself, so it covers:

- **Road splines** — lane fills, lane and section boundary lines, and the direction arrow of the selected spline.
- **Crosswalks** — the outline and the orange center line drop at the simplified level; the semi-transparent stripe
  fill stays until the component is culled.
- **Mark and Sidewalk detail spline previews** *(Pro)* — the outline, the curb-cut windows and the green magnetic
  dashes. The outline is only dropped when a filled shape will still be drawn in its place, so a spline that has
  nothing to fill (an open mark stripe, for example) keeps its line right up to the cull threshold.

It applies in the **level viewport only**. Asset and Blueprint editor previews, the
[Road Profile](/profiles/RoadProfile.md) preview and its thumbnail, Play In Editor and packaged builds always draw at
full detail — there is nothing to gain from culling a 128×128 thumbnail, and plenty to lose.

Nothing generated is affected: baked static meshes, the live Preview mesh and the deformed Landscape render through the
normal engine culling, exactly as any other mesh in the level.

## My roads disappear when I zoom out

That is the cull threshold, and it is expected. Pick whichever fits:

- **Zoom back in.** The schematic returns as soon as you cross the threshold — nothing was deleted, and the roads are
  still selectable from the World Outliner while they are culled.
- **Push the threshold out** — raise `Visualization Cull Distance` for perspective viewports, or
  `Visualization Cull World Per Pixel` for Top/Front/Side viewports.
- **Turn the system off** — clear `Enable View LOD`. The viewport then behaves exactly as it did before 3.1.0, at the
  frame cost that motivated the feature.

```{important}
**Road Always Visible** (in the [Visibility](/misc/Visibility.md) panel) does **not** bypass this. That toggle only
controls whether roads are decluttered outside the Meta Road mode; distance culling still applies, inside the mode and
out.
```

## See also

- [Visibility](/misc/Visibility.md) — the editor-mode visibility and debug-draw toggles, including **Road Always Visible**.
- [The Meta Road Editor Mode](/editor-mode/MetaRoadEditorMode.md) — the Schematic and Preview views this LOD applies to.
- [Baking](/baking/BakeStaticMesh.md) — the generated meshes, which are unaffected by these settings.
