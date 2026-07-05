# The Meta Road Editor Mode

MetaRoad ships its own Unreal **editor mode**, shown as **Meta Road** in the level-editor mode dropdown. It is the
**single entry point** for all road authoring — drawing roads, editing them, previewing, and baking all happen here.
There is no separate "road" toolset in Modeling Mode any more.

![alt text](/img/meta-road-editor-mode.png)

## The tile palette

The mode's panel is an integrated **tile palette** at the top, split into four categories. Selecting a category shows
its tiles; selecting a tile activates that tool or editing sub-mode and shows its panel below.

<!-- TODO 📷 screenshot: the palette showing the Create / Edit / Bake / Misc category tabs and their tiles -->

The categories, in order (**Create** is the default when the mode opens):

### Create — make road geometry

![alt text](/img/create-panel.png)

Interactive tools that place new roads. (All except **Spline** are Pro.)

| Tile | Creates |
|------|---------|
| **Spline** | A new road spline (`URoadSplineComponent`) drawn on a surface — see [Draw Spline Tool](/create-tools/DrawSplineTool.md) |
| **Roundabout** *(Pro)* | A circular roundabout road — see [Roundabout Tool](/create-tools/RoundaboutTool.md) |
| **Intersection** *(Pro)* | A junction linking several roads — see [Intersection Tool](/create-tools/IntersectionTool.md) |
| **Crosswalk** *(Pro)* | A pedestrian crossing on the selected road — see [Crosswalk Tool](/create-tools/DrawCrosswalkTool.md) |
| **Chevron** *(Pro)* | A chevron guide-island marking — see [Chevron Marking Tool](/create-tools/ChevronMarkingTool.md) |

### Edit — shape the selected road

![alt text](/img/edite-panel.png)

Sub-modes for editing a selected road. Each swaps in a viewport editor and a Details "Selection" panel.

| Tile | Edits |
|------|-------|
| **Spline** | The reference line: nodes, tangents, arc nodes, endpoint connections — see [Spline Mode](/editing/SplineMode.md) |
| **Section** | Lanes and lane sections — see [Section Mode](/editing/SectionMode.md) |
| **Offset** | The center-line offset curve — see [Offset Mode](/editing/OffsetMode.md) |
| **Width** | Per-lane width curves — see [Width Mode](/editing/WidthMode.md) |
| **Attribute** | Lane attributes (markings, guardrails, …) — see [Attribute Mode](/editing/AttributeMode.md) |
| **Preset** | Stage mesh-build settings/presets against the live preview — see [Preset Mode](/editing/PresetMode.md) |

### Bake — generate output

![alt text](/img/bake-panel.png)

| Tile | Does |
|------|------|
| **Bake** | Generate or clear road mesh assets/actors (Bake / Clear, Selected / All) — see [Baking](/baking/BakeStaticMesh.md) |
| **Export** | Export road meshes to `.fbx` files — see [FBX Export](/baking/FbxExport.md) |

### Misc

![alt text](/img/misc-panel.png)

| Tile | Does |
|------|------|
| **Visibility** | Editor visibility settings (tile renders, unhide splines, debug draw) — see [Visibility](/misc/Visibility.md) |

## Schematic vs Preview

At the top of the panel a toggle switches the viewport between two views:

- **Schematic** — the editable lane graph drawn by the editing sub-modes. This is where you author.
- **Preview** — a live, non-destructive preview of the generated road mesh. Nothing is written to disk; it rebuilds as
  you edit. Two icon buttons appear next to the toggle **while you are in Preview view**:
  - **Build status** — reflects the live preview build: a spinning throbber while it computes, then a green **success**,
    a yellow **warning** or a red **error** icon when it finishes. It is **hidden while the preview is idle**. Click it
    to open the **Output Log** and read the full build messages.
  - **Update / Stop** — normally a **refresh** icon that rebuilds the preview from the current spline data and build
    settings. While a build is running it turns into a red **stop** icon that cancels the in-progress build. It is
    disabled when there is no active preview to rebuild.

![alt text](/img/schematic-vs-preview.png)

## Editing splines outside the mode

The default **Spline** editor is always active, even when you are **not** in the Meta Road mode: select an `AMetaRoad`
in the level and you can edit its road spline's points/tangents directly. The other Edit sub-modes
(Section / Offset / Width / Attribute) require the Meta Road mode to be active.

## AMetaRoad-only

Road splines are only picked up by the build/preview/bake pipeline when they live on an **`AMetaRoad`** actor; splines
on other actors are ignored. The Create tools always produce `AMetaRoad` actors for you. See
[The MetaRoad Workflow](/concepts/Workflow.md) for the full picture.
