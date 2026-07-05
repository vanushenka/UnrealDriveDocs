# Quick Start: Create a Road

This is **part 1 of the Quick Start**. You will build your first road end to end — draw it, give it lanes, preview it,
and bake it into a mesh — touching all three pillars of the workflow: **Create → Edit → Bake**
(see [The MetaRoad Workflow](/concepts/Workflow.md)).

```{container} qs-nav
**Quick Start series:** **1. Create a Road** *(you are here)* → 2. [Build a T-Junction Manually](/getting-started/QuickStartTJunctionManual.md) → 3. [Build a T-Junction with the Intersection Tool](/getting-started/QuickStartTJunctionAuto.md)
```

```{note}
**Prerequisite:** the MetaRoad plugin is installed and enabled — see [Installation](/introduction/Installation.md).
A landscape or any surface to draw on is helpful but not required.
```

## 1. Enter the Meta Road editor mode

In the level editor, open the **editor mode** dropdown (top-left toolbar) and choose **Meta Road**. The mode panel
appears with its tile palette; the **Create** category is selected by default. See
[The Meta Road Editor Mode](/editor-mode/MetaRoadEditorMode.md).

<!-- TODO 📷 screenshot: choosing "Meta Road" from the mode dropdown -->

## 2. Draw a road (Create)

In the **Create** palette, click the **Spline** tile to activate the Draw Spline tool. Click in the viewport to place
road points; each click adds a point and the road preview follows. Press **Enter/Accept** to finish. A new `AMetaRoad`
actor containing your road spline is created. Full details: [Draw Spline Tool](/create-tools/DrawSplineTool.md).

<!-- TODO 🎞 gif: drawing a road spline with the Spline tool and accepting -->

## 3. Add lanes (Edit)

With the road selected, open the **Edit** palette and click the **Section** tile. Use the viewport handles and the
context menu to add lanes and lane sections, and the **Selection** panel to tune lane properties. See
[Section Mode](/editing/SectionMode.md). You can also adjust the reference-line shape in
[Spline Mode](/editing/SplineMode.md), the center-line offset in [Offset Mode](/editing/OffsetMode.md), and per-lane
width in [Width Mode](/editing/WidthMode.md).

<!-- TODO 🎞 gif: adding lanes in Section mode -->

## 4. Preview the result

At the top of the panel, switch the view toggle from **Schematic** to **Preview**. You now see a live, non-destructive
preview of the generated road mesh that updates as you keep editing — nothing has been written to disk yet.

<!-- TODO 🎞 gif: toggling to Preview to see the generated mesh -->

## 5. Bake the mesh

Open the **Bake** palette and click the **Bake** tile, then **Bake Selected** (or **Bake All**). Baking runs in the
background with a progress notification; when it finishes, a generated actor named `<YourActor>_Gen` appears in the
level, holding the baked static/spline meshes. Full details: [Baking](/baking/BakeStaticMesh.md).

<!-- TODO 📷 screenshot: the _Gen actor and its baked meshes in the level -->

```{tip}
**Grouping tip.** Each road actor bakes as its own mesh. If you later join roads at a junction, keep their splines in
the **same actor and the same SubGroup** so they fuse into one seamless mesh — see
[Spline grouping](/concepts/Workflow.md#bake-spline-grouping).
```

## Next steps

- **Continue the Quick Start → [2. Build a T-Junction Manually](/getting-started/QuickStartTJunctionManual.md).**
- Add **markings, guardrails, and more** with [Attributes](/concepts/Attributes.md).
- Export to `.fbx` with [FBX Export](/baking/FbxExport.md).
- Understand the underlying data with [The Road Model](/concepts/RoadModel.md).
