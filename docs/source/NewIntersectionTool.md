# New Intersection Tool (Pro)

This tool automates the creation of most types of standard intersections. You can still create any intersections and interchanges using the [Draw Spline Tool](DrawSplineTool.md). This tool's purpose is to speed up the creation process. For particularly complex and non-standard intersections, you may have to create them entirely manually using the [Draw Spline Tool](DrawSplineTool.md).   

## Supported Intersection Types

The tool handles the most common intersection topologies out of the box:

- **T-junction** — three road ends meeting at a point
- **X-junction (cross-intersection)** — four road ends meeting at a point
- **Multi-lane** — roads with different lane counts on each arm; the tool matches lanes automatically

For grade-separated interchanges, roundabouts, or other unusual topologies, use the [Draw Spline Tool](DrawSplineTool.md) and connect the lanes manually in [Spline Mode](EditorModes.md#spline-mode).

## Workflow

To generate an intersection:

1. Switch to **New Intersection Tool** mode.
2. Click the **beginning** or **end** of each `URoadSplineComponent` that should join the intersection. Selected endpoints are highlighted. The selected splines may belong to **any actors** in the level.
3. Once all arms are selected, the tool creates a **new Actor** containing the connecting junction splines and wires up all `URoadConnection` and `ULaneConnection` objects automatically.

To start generating an intersection, simply switch to the **New Intersection Tool** mode and start selecting the beginnings or ends of the **URoadSplineComponents** for which you want to create an intersection:  
![alt text](img/intersection-create.gif)  

## Turn Directions

For each lane entering the intersection, you can set the possible directions of traffic movement (straight, left turn, right turn, U-turn). These settings affect how MetaRoad routes lane connectivity through the junction and are used by AI navigation (ZoneGraph) to generate correct traversal lanes:  
![alt text](img/intersection-turn.gif)  

## Tips

- After generation, switch to [Section Mode](EditorModes.md#section-mode) to fine-tune the lane layout inside the junction splines.
- For complex lane-drop or merge scenarios at the junction, add asymmetric lane sections to the approach splines before running the tool (see [Asymmetric Lane Sections](RoadModel.md#asymmetric-lane-sections)).
- For procedural mesh generation, run the **Build Mesh Tool** on the new junction actor separately from the approach road actors (see [Procedure Generation Tool](ProcedureGenerationTool.md)).
