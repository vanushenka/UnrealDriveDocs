# Section Mode

```{note}
This is the **Section** tile in the **Edit** palette of the Meta Road editor mode
(see [The Meta Road Editor Mode](/editor-mode/MetaRoadEditorMode.md)).
```

![Section sub-mode active in the Meta Road palette](/img/section-mode2.png)

**Section Mode** edits the [Road Lanes](/concepts/RoadModel.md#road-lanes) and
[Road Sections](/concepts/RoadModel.md#lane-sections) of the selected road.

## Road Section Editing

### Selecting a section

Click a section in the viewport. The selected section is highlighted, a move **handle** appears at its start, and a
viewport overlay shows its **S** (arc-length) offset. The Details **Selection** panel then shows the section's
properties:

![The selected road section and its Selection panel](/img/section-mode.png)

| Property | Meaning |
|----------|---------|
| **Side** | `Both` / `Left` / `Right` — which side(s) this section governs (enables [asymmetric layouts](/concepts/RoadModel.md#asymmetric-lane-sections)) |
| **SOffset** | Arc-length position where the section starts |
| **SOffset End Cached** | Computed end of the section (read-only) |
| **Label** | Optional name for the section |
| **Skip Landscape** | Exclude this section from landscape deformation |
| **Section Index** | Position in the layout (read-only) |
| **Attributes** | Section-level attributes (e.g. a road **Mark**) |

Drag the section handle in the viewport to move its boundary along the road:

![Resizing a road section by dragging its handle](/img/section-resize.gif)

### Adding and removing sections

Add (split) and delete **Road Sections** from the right-click context menu — you need a new section wherever the lane
count changes (for example before a ramp):

![Adding and removing road sections via the context menu](/img/section-split.gif)

```{note}
**Delete Section** also refreshes the [detail splines](/concepts/DetailSplines.md) *(Pro)* attached to this road: their
linked nodes re-pin and their magnetic segments re-follow the renumbered sections straight away, instead of staying
attached to geometry that has moved.
```

### Splitting a spline

**Split Spline** — in the same right-click menu, just below the two section splits — cuts the selected **road spline**
in two at the point you clicked. Use it when a road has grown too long to manage comfortably, or when you want to give
one half a different [Sub Group](/concepts/Workflow.md#bake-spline-grouping), profile or landscape target.

- The **first half** keeps the original component and its **Predecessor** connection, together with every section and
  lane before the cut.
- The **second half** becomes a **new road spline component on the same actor**. It takes the geometry, the sections
  and lanes after the cut — re-based so the cut sits at `S = 0` — the matching part of the
  [center-line offset curve](/editing/OffsetMode.md), the **Successor** connection, and the connections of the lanes
  that moved with it.
- The **cut itself is left unconnected**: the two halves are separate roads until you wire them together in
  [Spline Mode](/editing/SplineMode.md).
- The new second half becomes the **selected spline**, so you can carry on editing it.

A section boundary is created at the cut if there is not one there already, so no section ends up split between the
two halves.

```{important}
**Closed-loop splines cannot be split.** On a ring road the command simply does nothing (a warning goes to the Output
Log) — clear **Closed Loop** on the spline first if you need to cut it.
```

```{note}
Cutting between two control points inserts a new control point at the cut and recomputes the tangents of its two
neighbours, so a hand-tuned curve can shift slightly right there. Cut at an existing spline node to leave the curve
untouched.
```

```{tip}
Only the road layout travels across the cut. The road spline's own component settings — **Sub Group**, **Material
Priority**, **Skip Procedural Generation** and the whole **Landscape** group — start at their defaults on the new half,
so set them again if the road used them. A **Sub Group** left at its default would otherwise bake the two halves as
separate meshes.
```

## Road Lane Editing

### Selecting a lane

Click a lane in the viewport; it is highlighted (orange) with a move gizmo. The Details **Selection** panel shows the
lane's properties:

![The selected road lane and its Selection panel](/img/lane-selection2.png)

| Property | Meaning |
|----------|---------|
| **Road Zone** | The lane's surface — a [Road Zone](/concepts/RoadZones.md) (a Zone Type + optional material/decal/priority overrides) |
| **Zone Type** | Which [Zone Type](/concepts/RoadZones.md) the lane uses (Driving / Sidewalk / Tram / …) — sets the default material and behavior |
| **Direction** | `Default` / `Invert` — per-lane traffic direction |
| **Override Material / Decal / Priority** | Per-lane overrides of the zone's defaults |
| **Invert UV0**, **Skip Procedural Generation** | Per-lane mesh flags |
| **String / Float / Zone Tags** | Arbitrary per-lane metadata |

The surface-type system (Zone Types, Road Zones, materials, project settings) is described in
[Road Zones and Zone Types](/concepts/RoadZones.md).

### Selecting multiple lanes

![Ctrl+clicking to multi-select several lanes across sections](/img/multy-lane-selection.gif)

You can select **several lanes at once**. Hold **Ctrl** and click lanes to toggle each one in or out of the selection —
the set may **span different sections**. A plain (non-`Ctrl`) click clears the set and selects a single lane again. The
last lane you click is the **primary** one: it carries the move gizmo and drives the **Road Zone** picker.

With more than one lane selected, the **Selection** panel becomes a **multi-edit**:

- Editing any property writes it to **every** selected lane at once.
- Where the selected lanes disagree on a value, the field shows **`Multiple Values`**.

The right-click context menu also acts on the whole selection:

- **Delete Lane** — removes all selected lanes.
- **Reverse Direction** — flips the [traffic direction](/concepts/RoadModel.md#lane-direction) of all selected lanes.

### Adding and removing lanes

Add and delete **Road Lanes** from the right-click context menu:

![Adding and removing road lanes via the context menu](/img/lane-add.gif)

```{note}
**Add Lane**, **Delete Lane** and **Reverse Direction** re-anchor the [detail splines](/concepts/DetailSplines.md)
*(Pro)* attached to this road as soon as you use them — adding or removing a lane renumbers the lanes outside it, and
every Mark or Sidewalk spline linked to the road re-pins its nodes and re-magnetizes its segments against the new
numbering instead of keeping a stale attachment.
```

## See also

- [Road Lanes](/concepts/RoadModel.md#road-lanes) and [Lane Sections](/concepts/RoadModel.md#lane-sections) — the data model this mode edits.
- [Road Zones and Zone Types](/concepts/RoadZones.md) — the lane surface types you assign here.
- [Width Mode](/editing/WidthMode.md) and [Attribute Mode](/editing/AttributeMode.md) — other per-lane editing.
- [Detail Splines](/concepts/DetailSplines.md) *(Pro)* — Mark and Sidewalk splines that anchor to the lanes and
  sections you edit here.
