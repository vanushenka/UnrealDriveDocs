# Quick Start: Build a T-Junction with the Intersection Tool

This is **part 3 of the Quick Start**. Here you build the same kind of T-junction as
[part 2](/getting-started/QuickStartTJunctionManual.md), but let the **[Intersection Tool](/create-tools/IntersectionTool.md)**
*(Pro)* wire it for you — it creates the junction splines and connects all the lanes automatically.

```{container} qs-nav
**Quick Start series:** 1. [Create a Road](/getting-started/QuickStart.md) → 2. [Build a T-Junction Manually](/getting-started/QuickStartTJunctionManual.md) → **3. Build a T-Junction with the Intersection Tool** *(you are here)*
```

```{note}
**Prerequisite:** the [Intersection Tool](/create-tools/IntersectionTool.md) is a **Pro** feature.
```

## How the tool thinks

The Intersection Tool joins **road ends** — it connects the endpoints of the roads you pick into one junction. So for a
T-junction you provide **three road arms** whose ends meet at the junction point (the two halves of the main road plus
the branch), and let the tool stitch them.

## 1. Draw the three arms

Using the **Spline** tile in the **Create** palette ([Draw Spline Tool](/create-tools/DrawSplineTool.md)), draw the
three road arms so their ends come together at the junction point:

- the two halves of the main road (left arm and right arm), and
- the branch (the stem of the "T").

The arms may be in **any actors** — the tool doesn't require them to share one, unlike the manual method.

<!-- ![Drawing the three road arms so they meet at a point](/img/qs-tj-auto-arms.gif) -->

## 2. Run the Intersection Tool

Activate the **Intersection** tile in the **Create** palette, then **click the end** of each arm that should join the
junction. Selected endpoints are highlighted.

<!-- ![Selecting the three arm ends with the Intersection Tool](/img/qs-tj-auto-select.gif) -->

## 3. Let it build the junction

Once all three ends are selected, the tool creates a **new actor** containing the connecting junction splines and wires
up all the `URoadConnection` / `ULaneConnection` links automatically — no manual connecting in Spline Mode needed.

Optionally set **turn directions** (straight / left / right / U-turn) per entering lane; these drive lane connectivity
and AI navigation. See [Intersection Tool → Turn Directions](/create-tools/IntersectionTool.md#turn-directions).

## 4. Bake

Open the **Bake** palette → **Bake Selected** on the junction actor to generate its mesh. The junction actor's splines
already share one actor and group, so it bakes as a single seamless mesh. See [Baking](/baking/BakeStaticMesh.md).

```{note}
Bake the junction actor **separately** from the approach-road actors — each is its own generation unit
([Spline grouping](/concepts/Workflow.md#bake-spline-grouping)).
```

<!-- ![The baked junction mesh](/img/qs-tj-auto-baked.png) -->

## Next steps

- Add markings and objects along your roads with [Attributes](/concepts/Attributes.md).
- Place a [Roundabout](/create-tools/RoundaboutTool.md) *(Pro)*.
- Export everything to `.fbx` with [FBX Export](/baking/FbxExport.md).
