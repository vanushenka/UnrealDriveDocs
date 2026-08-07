# Visibility

```{note}
This is the **Visibility** tile in the **Misc** palette of the Meta Road editor mode
(see [The Meta Road Editor Mode](/editor-mode/MetaRoadEditorMode.md)).
```

The **Visibility** panel holds editor-only visibility and debug-draw settings for MetaRoad. They affect only the editor
viewport, not the baked meshes.

![The Visibility tile panel with its editor visibility and debug-draw toggles](/img/misc-visibility.png)

<!-- RE-CAPTURE /img/misc-visibility.png: it predates the Road Always Visible toggle. -->

| Setting | Description |
|---------|-------------|
| **Tiles Visibility** | Show/hide tile-map renders (`UTileMapWindowComponent`) — see [Tile Window](/integrations/TileWindow.md) |
| **Road Always Visible** | Keep every road spline and every Mark/Sidewalk spline drawn in the level viewport even while the Meta Road mode is **not** active — see [Road always visible](#road-always-visible) below |
| **Draw Boundaries** | Draw the triangulation boundaries of roads (debug) |
| **Show Wireframe** | Draw roads in wireframe (debug) |
| **Unhide All Splines** | Un-hide every road spline hidden for the current actor |

You can hide an individual selected road spline and later restore all of them with **Unhide All Splines** — handy when
working on a busy junction.

## Road always visible

Outside the Meta Road mode the level viewport is decluttered: only the road splines and detail splines you have
**selected** draw their schematic. Inside the mode everything draws.

**Road Always Visible** switches that decluttering off, so the whole network stays on screen while you work with other
Unreal tools — placing props, painting landscape, wiring Blueprints — without having to select the road actors first.

What it does and does not cover:

- **No effect inside the Meta Road mode** — everything is drawn there anyway.
- Covers road splines and both detail splines ([Mark and Sidewalk](/concepts/DetailSplines.md)).
- Does **not** cover crosswalk components: they still draw only while selected or while the mode is active.
- Does **not** bypass the distance culling described below.
- The toggle is a per-user editor preference and is remembered between sessions.

```{note}
The decluttering itself only ever applies to the main level viewport. In asset and Blueprint editor preview scenes,
thumbnails, Play In Editor and packaged games these components are never decluttered, so this setting changes nothing
there.
```

## Distance culling

```{important}
**Road Always Visible does not override the view-LOD culling.** If your roads disappear when you zoom out, that is the
distance/zoom culling of the schematic view, not this toggle. Its thresholds and its master switch live in
**Project Settings → Plugins → Meta Road Editor → Performance**, not in this panel — see
[Performance](/misc/Performance.md).
```

## See also

- [Performance](/misc/Performance.md) — the view-LOD thresholds that hide the schematic at a distance.
- [Tile Window](/integrations/TileWindow.md) — the tile-map renders toggled by **Tiles Visibility**.
- [Detail Splines](/concepts/DetailSplines.md) — the Mark and Sidewalk splines covered by **Road Always Visible**.
- [The Meta Road Editor Mode](/editor-mode/MetaRoadEditorMode.md) — the mode and palette this tile belongs to.
