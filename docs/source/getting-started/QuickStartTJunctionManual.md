# Quick Start: Build a T-Junction Manually

This is **part 2 of the Quick Start**. Here you turn a straight road into a **T-shaped junction** by hand — drawing a
branch road and joining it to a through road. Doing it manually shows how junctions actually work before you let the
[Intersection Tool](/getting-started/QuickStartTJunctionAuto.md) automate it.

```{container} qs-nav
**Quick Start series:** 1. [Create a Road](/getting-started/QuickStart.md) → **2. Build a T-Junction Manually** *(you are here)* → 3. [Build a T-Junction with the Intersection Tool](/getting-started/QuickStartTJunctionAuto.md)
```

```{note}
**Prerequisite:** you can already create a road — see [part 1](/getting-started/QuickStart.md). Start from a straight
**through road** (the top bar of the "T").
```

## The one rule that makes a junction work

A junction becomes a single **seamless mesh** only when all of its splines live in the **same `AMetaRoad` actor and the
same `SubGroup`** — the bake then triangulates them together and fills the junction surface. If the branch is in a
different actor/group, it is baked separately and you get seams. Keep this in mind for every step below; the full
explanation is in [Spline grouping](/concepts/Workflow.md#bake-spline-grouping).

## 1. Select the through road

Select the `AMetaRoad` actor of your through road so the branch you draw next can be added **into the same actor**.

## 2. Draw the branch into the same actor

Activate the **Spline** tile in the **Create** palette and draw the branch (the stem of the "T") so its end meets the
side of the through road. When you finish, choose **“Add spline to the selected actor”** (not “Create a new actor”) so
the branch joins the through road's actor. See [Draw Spline Tool](/create-tools/DrawSplineTool.md).

```{tip}
**Draw straight into the connection.** If you begin (or end) the branch **on a lane connection** of the through
road, the Draw Spline Tool uses its *Drawing from Lane Successor Connection* mode and matches the lane count for you —
the lane-level connection is wired automatically. See
[Draw Spline Tool → Start Drawing from Lane Successor Connection](/create-tools/DrawSplineTool.md#start-drawing-from-lane-successor-connection).
```

<!-- ![Drawing the branch into the through-road actor so its end meets the road](/img/qs-tj-manual-branch.gif) -->

## 3. Connect the lanes

Switch to the **Spline** tile in the **Edit** palette ([Spline Mode](/editing/SplineMode.md)). Here you manage the
endpoint **connections** between the branch and the through road — link the branch's end connection to the through road
so the lanes are joined (see [Intersections and Junctions](/concepts/Junctions.md)). If you
drew straight into a lane connection in step 2, this is already done.

<!-- ![Connecting the branch endpoint to the through road in Spline Mode](/img/qs-tj-manual-connect.gif) -->

## 4. Check the group

Make sure the through road and the branch share the same **`SubGroup`** (the default empty group is fine as long as they
are in one actor). You can confirm/set it in the spline's **Details → SubGroup** row.

## 5. Preview and tidy up

Switch the view toggle to **Preview**. The junction surface now fills in where the splines meet. Use
[Section Mode](/editing/SectionMode.md) and [Width Mode](/editing/WidthMode.md) to tidy the lanes and widths around the
junction.

<!-- ![Preview showing the filled T-junction surface](/img/qs-tj-manual-preview.gif) -->

## 6. Bake

Open the **Bake** palette → **Bake Selected** on the junction actor. Because all its splines share one actor and group,
the T-junction bakes as a single seamless mesh (`<YourActor>_Gen`). See [Baking](/baking/BakeStaticMesh.md).

<!-- ![The baked seamless T-junction mesh](/img/qs-tj-manual-baked.png) -->

## Next steps

- Let MetaRoad do steps 2–3 for you → **[3. Build a T-Junction with the Intersection Tool](/getting-started/QuickStartTJunctionAuto.md)**.
