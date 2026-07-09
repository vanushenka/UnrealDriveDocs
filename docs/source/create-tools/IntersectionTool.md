# Intersection Tool (Pro)

```{note}
This is the **Intersection** tile in the **Create** palette of the Meta Road editor mode
(see [The Meta Road Editor Mode](/editor-mode/MetaRoadEditorMode.md)). *(Pro feature.)*
```

![Intersection tool active in the Create palette](/img/intersection-mode.png)

This tool automates the creation of most standard intersections — it speeds up the common cases. For complex or
non-standard junctions and interchanges, build them by hand with the
[Draw Spline Tool](/create-tools/DrawSplineTool.md) instead.

## Supported Intersection Types

The tool handles the most common intersection topologies out of the box:

- **T-junction** — three road ends meeting at a point
- **X-junction (cross-intersection)** — four road ends meeting at a point
- **Multi-lane** — roads with different lane counts on each arm; the tool matches lanes automatically

For grade-separated interchanges, roundabouts, or other unusual topologies, use the
[Draw Spline Tool](/create-tools/DrawSplineTool.md) and connect the lanes manually in
[Spline Mode](/editing/SplineMode.md).

## Workflow

To generate an intersection:

1. Activate the **Intersection** tile in the **Create** palette. Any current selection is cleared — you do **not**
   pre-select the roads.
2. **Click the beginning or end** of each `URoadSplineComponent` that should join the intersection. Selected endpoints
   are highlighted, and the splines may belong to **any actors** in the level.
3. Once all arms are selected, the tool creates a **new actor** containing the connecting junction splines and wires up
   all `URoadConnection` and `ULaneConnection` links automatically.

![Selecting road ends to build an intersection](/img/intersection-create.gif)

## Turn Directions

**Right-click** a driving lane's direction marker to open the **Traffic Direction** menu and choose which movements that
entering lane allows:

- **Default**, **No Entry**
- **Forward** (straight), **Turn Left**, **Turn Right**
- **Forward + Left**, **Forward + Right**, **Any Direction**

These settings drive how MetaRoad routes lane connectivity through the junction, and feed AI navigation (ZoneGraph) so it
generates the correct traversal lanes:

![Setting per-lane turn directions from the right-click menu](/img/intersection-turn.gif)

## Properties

Solver options in the tool's **Details** panel:

| Property | Default | Description |
|----------|---------|-------------|
| `Find Forward Splines` | on | Generate the straight-through connecting splines |
| `Find Turn Splines` | on | Generate the left/right turning connecting splines |
| `Forward Indent` | 600 | Indent applied to the generated forward splines, cm |
| `Allow Forward Pass` / `Allow Reverse Pass` *(advanced)* | on | Solver passes that search for connecting splines |

## Next steps

- After generation, switch to [Section Mode](/editing/SectionMode.md) to fine-tune the lane layout inside the junction
  splines.
- For complex lane-drop or merge scenarios, add asymmetric lane sections to the approach splines before running the tool
  (see [Asymmetric Lane Sections](/concepts/RoadModel.md#asymmetric-lane-sections)).
- To generate the mesh, **bake** the junction actor separately from the approach-road actors (see
  [Baking](/baking/BakeStaticMesh.md)). Keep the junction's splines in one actor and `SubGroup` so they fuse into a
  seamless mesh — see [Spline grouping](/concepts/Workflow.md#bake-spline-grouping).
