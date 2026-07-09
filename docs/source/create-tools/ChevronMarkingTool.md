# Chevron Marking Tool (Pro)

```{note}
This is the **Chevron** tile in the **Create** palette of the Meta Road editor mode
(see [The Meta Road Editor Mode](/editor-mode/MetaRoadEditorMode.md)). *(Pro feature.)*
```

![Chevron Marking tool active in the Create palette](/img/chevron-mode.png)

The **Chevron Marking Tool** draws **chevron guide-island markings** — the striped "V" islands painted at gore points
where traffic flows split or merge (for example at off-ramps). The marking is a spline-driven
`UChevronMarkingComponent` added to the selected road actor, and it participates in
[baking](/baking/BakeStaticMesh.md) together with the road surface.

## Requirements

Select one actor that contains a `URoadSplineComponent` before activating the tool.

## Drawing a chevron island

1. Select the road actor and activate the **Chevron** tile.
2. **Click** in the viewport to append a **sharp (linear) point** to the island outline. A live preview of the
   chevrons renders as you go.
3. **Click-drag** to reposition the last point.
4. **Accept** to commit the `UChevronMarkingComponent` to the selected actor, or **Cancel** to discard.

![Drawing a chevron guide-island outline](/img/chevron-life.gif)

At each interior point of the spline, the point is the apex of a wedge between the two tangent directions; the wedge is
filled with chevron V-bands pointing outward. Open-spline endpoints are skipped.

## Properties

**Component-wide** (the component's **Details** panel):

| Property | Default | Description |
|----------|---------|-------------|
| `Section Size` | 100 | Depth of one chevron band (the "V") along the wedge bisector, cm |
| `Section Interval` | 200 | Gap between consecutive chevron bands, cm |
| `Road Zone` | — | Road surface type (material/color) applied to the marking |
| `Texture Angle` | 0° | UV texture rotation, in degrees |
| `Texture Scale` | 1.0 | UV texture scale multiplier |

**Per-point** (in the spline's **Selected Points** section — select one or more points first):

| Property | Default | Description |
|----------|---------|-------------|
| `Draw Chevron Marking` | off | Generate a chevron island at the selected point(s) |
| `Size (cm)` | 1000 | Island length along the wedge bisector, in cm — drives how many chevron bands fill the island |
| `Offset (cm)` | 0 | Distance from the node where the chevrons start; shifts the whole `Size` region away from the node (drawn region = `[Offset, Offset + Size]`) |
| `Reverse Direction` | off | Flip the chevron pointing direction — toward the node apex (off) or the wide end of the island (on) |

![The chevron per-point properties in the Selected Points section](/img/chevron-deatils.png)

## Next steps

- [Bake](/baking/BakeStaticMesh.md) to generate the marking mesh together with the road.
