# Draw Crosswalk Tool (Pro)

```{note}
This is the **Crosswalk** tile in the **Create** palette of the Meta Road editor mode
(see [The Meta Road Editor Mode](/editor-mode/MetaRoadEditorMode.md)). *(Pro feature.)*
```

![Crosswalk tool active in the Create palette](/img/crosswalk-mode.png)

The **Draw Crosswalk Tool** lets you place pedestrian crosswalks on road actors with a single click-drag gesture. Each
crosswalk is stored as a `UCrosswalkComponent` attached to the selected actor and participates in
[baking](/baking/BakeStaticMesh.md) together with the road surface.

## Requirements

Exactly one actor containing at least one `URoadSplineComponent` must be selected before activating the tool.

## Drawing a crosswalk

1. Select an actor that contains a `URoadSplineComponent`.
2. Activate the **Crosswalk** tile in the **Create** palette.
3. **Press and hold LMB** at the start of the crosswalk — the tool raycasts against world geometry (or falls back to
   Z=0 if nothing is hit).
4. **Drag** to set the length and direction — a live stripe preview updates in the viewport.
5. **Release LMB** to place the crosswalk. The tool stays active, so you can place more without re-activating it.

![Click-dragging to place a pedestrian crosswalk](/img/crosswalk-life.gif)

After placement, select the `UCrosswalkComponent` in the **Details** panel to edit its properties, or drag the
start/end handles directly in the viewport.

## Properties

After placement, edit the `UCrosswalkComponent` in the **Details** panel (all lengths in cm):

| Property | Default | Description |
|----------|---------|-------------|
| `EndPos` | (400, 0, 0) | End of the crosswalk center line, in local component space. Drag the end handle in the viewport or set it here |
| `StartWidth` | 300 | Crosswalk width at the start (origin) end |
| `EndWidth` | 300 | Crosswalk width at the `EndPos` end — the width is interpolated along the center line |
| `StripeLength` | 40 | Length of each stripe along the center line |
| `StripeInterval` | 40 | Gap between consecutive stripes |
| `Rotation` | 0° | Rotation of each stripe around its own center (clamped to ±45°) |
| `bRectangularStripes` | `false` | `true` — each stripe is a uniform-width rectangle; `false` — a trapezoid (width interpolated at the stripe edges) |
| `RoadZone` | — | Road surface type (material/color) applied to the generated stripe polygons |
| `TextureAngle` | 0° | UV texture rotation, in degrees |
| `TextureScale` | 1.0 | UV texture scale multiplier |

<!-- TODO 📷 screenshot: the UCrosswalkComponent Details panel with the stripe properties -->

## Next steps

- Add road markings and objects along the road with [Attributes](/concepts/Attributes.md).
- [Bake](/baking/BakeStaticMesh.md) to generate the crosswalk mesh together with the road.
