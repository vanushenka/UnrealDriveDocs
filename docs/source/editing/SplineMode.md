# Spline Mode

```{note}
This is the **Spline** tile in the **Edit** palette of the Meta Road editor mode
(see [The Meta Road Editor Mode](/editor-mode/MetaRoadEditorMode.md)). Unlike the other edit sub-modes, the spline
editor is **also available outside the Meta Road mode** — just select an `AMetaRoad` in the level.
```

![Spline sub-mode active in the Meta Road palette](/img/spline-mode2.png)

**Spline Mode** lets you edit a `URoadSplineComponent` like an ordinary Unreal spline — create and delete nodes and
edit tangents. This is the editing mode for the [Road Reference Line](/concepts/RoadModel.md#road-reference-line). The
spline is drawn pink in this mode.

![Editing a road spline's nodes and tangents in the viewport](/img/spline-edit.gif)

## Selection

In the **Details** panel, the **Selection** group edits the selected **spline node**:

![The Details Selection group for a selected spline node](/img/spline-selection.png)

## Arc node

You can also assign a node the **Arc** type for circular-arc segments:

![Setting a spline node to the Arc type for a circular segment](/img/spline-arc.gif)

## Connections

You manage the road's endpoint connections in this mode (see
[Intersections and Junctions](/concepts/Junctions.md)):

![Editing a road's endpoint connections in Spline Mode](/img/spline-conn.gif)

## See also

- [Road Reference Line](/concepts/RoadModel.md#road-reference-line) — the data this mode edits.
- [Intersections and Junctions](/concepts/Junctions.md) — the endpoint connections you wire here.
- [Draw Spline Tool](/create-tools/DrawSplineTool.md) — create new road splines.
