# The MetaRoad Workflow

The mental model for MetaRoad, in three steps. Read this first — everything else in the docs is a detail of one of them.

## Create → Edit → Bake

All road authoring happens in one editor mode, **Meta Road** (see
[The Meta Road Editor Mode](/editor-mode/MetaRoadEditorMode.md)), and always follows the same loop. It is
**iterative** — you can step back from Bake or Edit at any time (dashed arrows):

```{image} /img/workflow-create-edit-bake.svg
:align: center
:width: 300px
:alt: Create, Edit and Bake form an iterative loop
```

- **Create** — lay down road geometry (splines). See [below](#create-roads-are-connected-splines).
- **Edit** — shape the road's data model (lanes, sections, offset, width, attributes). See
  [below](#edit-the-road-data-model).
- **Bake** — generate the final meshes into a `_Gen` actor. See [below](#bake-spline-grouping).

While in Create/Edit you work in the **Schematic** view; flip to **Preview** any time for a live, non-destructive preview
of the baked mesh — nothing is written to disk until you Bake.

<!-- TODO 🎞 gif: toggling the view between Schematic and Preview on the same road -->

## Create: roads are connected splines

Everything on the road side is **road splines** (`URoadSplineComponent`) — a straight road, an intersection, a
roundabout, a bridge, or a whole interchange is just a set of splines. Splines must live on an **`AMetaRoad`** actor
(the pipeline ignores splines on other actors; the Create tools make the actor for you). Splines **link end-to-end
through connections** to form junctions and let lanes flow between roads — the Create tools wire these for you (full
model: [Intersections and Junctions](/concepts/Junctions.md)).

Three tools create splines:

- **[Draw Spline Tool](/create-tools/DrawSplineTool.md)** — the universal way; draw any spline and connect them by hand.
  Complex or non-standard interchanges are built here.
- **[Intersection Tool](/create-tools/IntersectionTool.md)** *(Pro)* — a shortcut that generates and connects junction
  splines from road ends.
- **[Roundabout Tool](/create-tools/RoundaboutTool.md)** *(Pro)* — a shortcut for a circular road.

The Pro tools are just faster ways to produce ordinary splines — there is no special "intersection" or "roundabout"
object underneath.

<!-- TODO 🖼 illustration: real road elements (straight road, T-junction, roundabout, overpass) each shown as a set of connected/highlighted splines — a hand-drawn concept figure -->

## Edit: the road data model

Each spline owns a small **data model** — its lane layout along the spline, in the road's local **S-R-H** frame
(S = along the road, R = sideways, H = up): a **reference line**, **lanes** (width, type/zone, direction), **lane
sections** (the layout can change along the road and may be asymmetric), a **center-line offset**, per-lane
**attributes**, and endpoint **connections**. The baked mesh — and everything downstream (ZoneGraph, FBX) — is
generated **from this model**, so understanding it is what lets you build correct networks. Full reference:
[The Road Model](/concepts/RoadModel.md).

The **Edit** palette is where you edit it — one sub-mode per part:

| Edit sub-mode | Data-model part |
|---------------|-----------------|
| [Spline](/editing/SplineMode.md) | Reference line — nodes, tangents, arcs, endpoint connections |
| [Section](/editing/SectionMode.md) | Lanes and lane sections |
| [Offset](/editing/OffsetMode.md) | Center-line offset |
| [Width](/editing/WidthMode.md) | Per-lane width |
| [Attribute](/editing/AttributeMode.md) | Lane attributes |

## Bake: spline grouping

Baking turns your splines into meshes inside a generated `_Gen` actor (see [Baking](/baking/BakeStaticMesh.md)).

```{important}
**A generation unit = `AMetaRoad actor` + `SubGroup`.** That pair *is* the group MetaRoad bakes together into one
mesh. Splines in the **same actor _and_ the same `SubGroup`** are fused into one seamless mesh; a **different actor
_or_ a different `SubGroup`** produces a separate mesh.
```

Grouping decides the **mesh**. The **lane graph** — which lanes flow into which at a junction — is a separate thing,
wired by [connections](/concepts/Junctions.md).

```{image} /img/workflow-spline-grouping.svg
:align: center
:width: 600px
:alt: Each (AMetaRoad actor, SubGroup) is one generation unit that bakes into one mesh
```

- **Keep a junction in one actor and sub-group** so its surfaces stitch into one mesh (split across actors/sub-groups → seams).
- **Split the levels of a grade-separated (multi-level) junction** into different sub-groups or actors — the crossing roads sit at different heights and must **not** fuse into one surface.
- **Don't put too much in one sub-group** — one unit becomes one static mesh; give each junction (plus its approaches) its
  own sub-group so Unreal can cull, LOD, and collide efficiently.

Examples:  

A **flat T-junction** (panels **Splines → Bad → Good**). **Bad:** the splines are split across sub-groups/actors, so the junction bakes in disconnected pieces with seams. **Good:** they share one actor + sub-group and bake as one seamless surface:

![Flat junction — one actor + sub-group is correct; split is wrong](/img/bake-groupes2.png)  

A **multi-level crossing** (panels **Splines → Bad → Good**). **Bad:** both roads share one actor + sub-group, so the crossing is wrongly fused into a distorted surface. **Good:** the levels are split into separate sub-groups/actors and each bakes cleanly:

![Multi-level junction — split is correct; one group is wrong](/img/bake-groupes.png)

And this is **too much in one group** (panels **Splines → Bad**): with every spline of a whole network in one actor + sub-group, the bake fuses the entire layout — even the area enclosed by the loop — into one big, poorly-controlled mesh. Don't do this; give each junction (plus its approaches) its own sub-group:

![A whole network in one actor + sub-group bakes into one big, poorly-controlled mesh (bad)](/img/bake-groupes3.png)

## Attributes and profiles

**Attributes** are the extensibility layer: a typed curve of *keys* placed along a lane (by arc-length `SOffset`) that
adds markings, guardrails, speed limits, landscape deformation, or your own custom data and geometry — new attribute
types plug into the pipeline automatically. See [Attributes](/concepts/Attributes.md); you place them with the
[Attribute sub-mode](/editing/AttributeMode.md).

**Profiles** are reusable Content-Browser assets (road / mark / attribute / polygon shapes) you reference from roads and
attributes — see [Profiles](/profiles/Profiles.md). **Presets** are saved **build settings** that control how a road
bakes — see [Preset Mode](/editing/PresetMode.md).

## Where to go next

- New here? Do the [Quick Start](/getting-started/QuickStart.md).
- The data model in depth: [The Road Model](/concepts/RoadModel.md).
- Output: [Baking](/baking/BakeStaticMesh.md) and [FBX Export](/baking/FbxExport.md).
