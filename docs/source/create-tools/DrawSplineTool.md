# Draw Spline Tool

```{note}
This is the **Spline** tile in the **Create** palette of the Meta Road editor mode
(see [The Meta Road Editor Mode](/editor-mode/MetaRoadEditorMode.md)).
```

![The Spline tool active in the Create palette](/img/spline-mode.png)

The **Draw Spline Tool** lets you "draw" a `URoadSplineComponent` the way you would in a 2D vector editor. There are two
drawing modes, chosen automatically by where you start:

- **Drawing from Profile** — start anywhere except on a lane connection.
- **Drawing from Lane Successor Connection** — start on an existing lane connection.

## Drawing from Profile

If you start drawing from any point other than a **Lane Successor Connection**, the **Drawing from Profile** mode is
selected. Pick the starting lane layout from the **Draw Profile** dropdown:

![Drawing a road from a Road Profile](/img/draw-spline-profile.gif)

A new road profile can be added in [Profiles](/profiles/RoadProfile.md).

## Start Drawing from Lane Successor Connection

If you start drawing from a [Lane Successor Connection](/concepts/Junctions.md), the **Drawing from Lane Successor
Connection** mode is selected. Profiles are not available here; instead you set the number of lanes on the left and
right of the source road by clicking the on-screen lane discs:

![Drawing a road starting from a lane connection](/img/draw-spline-conn.gif)

## Stop Drawing from Lane Predecessor Connection

You can finish a spline at a [Lane Predecessor Connection](/concepts/Junctions.md) — the drawing completes and you
choose how to create the `URoadSplineComponent` (or cancel):

![Finishing a spline at a lane predecessor connection](/img/draw-spline-preds.gif)

## Finishing Spline Drawing

Once the spline is drawn, there are two ways to create it:

- **Create a new actor** and add a `URoadSplineComponent` to it.
- **Add to the selected actor** — a `URoadSplineComponent` is added to a selected actor that already contains at least
  one (this is how you build a junction inside a single actor).

![Choosing to create a new actor or add to the selected actor](/img/draw-spline-finish.png)

## Properties

| Property | Default | Description |
|----------|---------|-------------|
| `Draw Profile` | `2_Lanes+Borders` | The [Road Profile](/profiles/RoadProfile.md) a new road starts with (Profile mode; disabled when drawing from a connection) |
| `Loop` | off | Draw a **closed-loop** road — see [Closed-Loop Splines](/concepts/ClosedLoopSpline.md) |
| `Looped Road Zone` | — | Surface zone that fills the loop interior (when `Loop` is on) |
| `Click Offset` | 20 | Offset above the hit surface, cm |
| `Up Vector Mode` | Use Hit Normal | How the road's up direction is derived at each point |
| `World Objects` / `Custom Plane` / `Ground Planes` | on / off / on | Which surfaces a click raycasts against |
| `Create Blueprint` / `Blueprint To Create` | off | Optionally output a Blueprint instead of a level actor |

## Next steps

- Configure lanes in [Section Mode](/editing/SectionMode.md) and shape the reference line in
  [Spline Mode](/editing/SplineMode.md).
- Wire roads into junctions — see [Intersections and Junctions](/concepts/Junctions.md) or the
  [Intersection Tool](/create-tools/IntersectionTool.md) *(Pro)*.
- [Bake](/baking/BakeStaticMesh.md) to generate the mesh.
