# Detail Splines

**Detail splines** add surface details *on top of* an existing road network. Unlike a road spline, a detail
spline has **no lanes, sections or connections** — it only draws extra geometry, baked together with the road.
The network itself is always built from road splines; see [The Road Model](/concepts/RoadModel.md).

| Detail spline | Draws | Tool |
|---------------|-------|------|
| **Mark spline** | Stripe markings, chevron guide-islands, polygon stamps, closed-loop fill patterns | [Mark Spline Tool](/create-tools/MarkSplineTool.md) |
| **Sidewalk spline** | A raised sidewalk surface filling its outline, plus a curb around its boundary | [Sidewalk Spline Tool](/create-tools/SidewalkSplineTool.md) |

Both are *(Pro)*, live on the same **`AMetaRoad`** actor as the road splines, and bake into the same mesh.

![Mark and Sidewalk detail splines laying markings and a raised sidewalk on top of a road network](/img/details-splines.png)

## Selecting

A detail spline shows its nodes only while the **component itself** is selected — otherwise every detail spline
on the actor would spill its nodes at once. An unselected spline draws nothing but stays clickable.

| Click on | Selects |
|----------|---------|
| the filled body or outline | the **component** |
| a green dashed segment | that **segment** |
| a node | that **node** |

```{tip}
A node linked to *another spline's node* sits exactly on top of it, and the road's node wins the click. A ring
roughly 12 px across around that point stays clickable for the detail node — aim just off centre to grab it.
```

## The right-click menu

Detail splines replace the engine's spline menu with their own, so what you get differs from an ordinary
`USplineComponent`. What is offered depends on what is selected:

| Entry | On a node | On a segment | What it does |
|-------|:---------:|:------------:|--------------|
| **Spline Point Type** | ✔ | | One radio list — `Linear`, `Constant`, `Auto`, `Aligned`, `Broken`. Replaces the engine's separate point-type and tangent menus |
| **Magnetic Segment** | ✔ | ✔ | Checkable. Flags the segment *leaving* the selected node, or the selected segment itself |
| **Unlink** | ✔ | | Removes the anchor from the selected node(s) — they stop following and become freely draggable |
| **Add Spline Point Here** | | ✔ | Inserts a node at the cursor on that segment |
| **Delete / Duplicate Spline Point** | ✔ | | The usual node operations |
| **Closed Loop** | ✔ | ✔ | Closes or opens the spline |
| **Snap/Align**, **Visualize Roll and Scale**, **Spline Generation Panel**, **Reset to Default** | ✔ | ✔ | The standard engine entries, kept as they are |

```{note}
**Discontinuous Spline** is deliberately **not** offered — it has to stay on for magnetization to work.
```

![The right-click menu on a magnetic segment, showing Spline Point Type, Magnetic Segment and Unlink](/img/magnetic-context-menu.png)

## Magnetism

Nodes can **attach to road geometry**, so a detail spline stays glued to the road as you keep editing instead of
drifting when the road changes.

### What you see in the viewport

The whole feature shares one color: **green means magnetic**.

| Drawn as | Means |
|----------|-------|
| **Green dashed line** along a segment | The segment is flagged **Magnetic Segment** — whether or not it currently follows anything |
| **Green point** at a node | The node is **linked** and its target resolves |
| **Red point** at a node | The node is linked but its target is **gone** — the road it pointed at was deleted or renumbered |
| Marker in the **selection color** | That linked node is selected |

![A sidewalk spline with green dashed magnetic segments, green markers on its anchored nodes](/img/magnetic-visual-language.png)

### Linking a node

Select **exactly one** node and **drag it with the translate gizmo** — no modifier key.

1. Every valid target on the actor lights up: **lane corners** and the **nodes of other splines**.
2. The node snaps to the nearest target within **20 screen pixels**; the chosen one is drawn as a bold glyph
   hugging its lane, the rejected alternatives as thin grey ghosts.
3. **Drop on a target** to link. **Drop anywhere else** and the node stays where you left it, unlinked.

![Dragging a sidewalk node onto a lane corner, then reshaping the road so the node follows it](/img/magnetic-link.gif)

![Mid-drag: the available lane-corner targets lit up, the snapped one drawn as a bold glyph and the coincident alternatives as grey ghosts](/img/magnetic-snap-targets.png)

```{note}
`Alt`-drag is *not* the link gesture — it stays the engine's "duplicate this point". Linking needs **exactly one**
selected node; dragging a group that includes a linked node does nothing, because a linked node moves only when
its target does.
```

```{tip}
Up to four lane corners can land on the same point where two sections and two lanes meet. The one picked follows
the **cursor's quadrant** — nudge the cursor toward the lane you mean and watch which glyph goes bold.
```

A target another node already uses is **not offered**, and neither is one that would create a loop, so you cannot
link two nodes to the same corner or make two splines chase each other.

### The Selected Points panel

Select one or more nodes and the spline's **Selected Points** section carries the magnetism controls:

| Row | What it does |
|-----|--------------|
| **Node Link** | Read-only status of the anchor. Shows the target's name, `None` when unlinked, `Stale — target missing` in red when it no longer resolves, or `Multiple` across a mixed selection |
| **Break Link** | Removes the anchor. The node stays where it is and becomes freely draggable again |
| **Magnetic Segment** | Flags the segment **leaving** the selected node(s) as magnetic |
| **Tangent Mode** | `Auto` / `Aligned` / `Broken` for the selected node(s) — see [below](#point-types-and-tangent-modes) |

![The Selected Points section showing the Node Link status row, Break Link button, Magnetic Segment checkbox and Tangent Mode combo](/img/magnetic-selected-points.png)

### Magnetic segments and runs

Following the road is an explicit **per-segment opt-in**: tick **Magnetic Segment** on a node — or right-click the
segment itself — to mark the segment *leaving* that node. Off by default, so existing content is unaffected.

What actually follows the road is the **run** — a chain of consecutive magnetic segments whose interior nodes
carry no anchor. That lets you author "follow this curb from A to D" by anchoring only the two ends:

- Only the run's **two end nodes** need anchors, and they must sit on the **same** road curve.
- Interior nodes are **projected onto that curve**, so your point distribution survives and dragging one slides
  it *along* the target.
- An **anchored node always ends a run**, so anchoring a node mid-chain splits it into two independent runs.


![alt](/img/magnetic-segments.gif)

![A sidewalk spline whose run follows a lane edge straight through a curb cut, with no gap at the seam](/img/magnetic-run.png)

Two curves qualify as a target: a **lane edge** running along the road (identified road-wide, so a run can span
adjacent lanes and the center line), or a **cross-section** across the road at a lane start or end.

```{note}
If a run cannot resolve a target — nothing anchored, both ends on different curves, or a lane-width change that
splits the edge — its segments stay ordinary smooth segments and keep their green dashes, and the geometry
**drapes** over the surface instead. Visually close, but without the welded edge.
```

## Point types and tangent modes

The node's right-click menu carries a single **Spline Point Type** list, also available as a **Tangent Mode** row
in **Selected Points** for editing several nodes at once.

| Point type | Behavior |
|------------|----------|
| **Linear** | Straight segment, no tangents |
| **Constant** | Stepped segment |
| **Auto** *(default)* | Auto-smooth from the neighbouring points; dragging a handle gives a symmetric manual tangent |
| **Aligned** | Smooth, with independent tangent **lengths** that stay collinear |
| **Broken** | A corner — both tangents fully independent |

```{note}
A **magnetized** node is forced to **Broken**, since the fit against the target drives its tangents, so Auto and
Aligned are greyed out there.
```

## Component properties

| Property | Default | Description |
|----------|---------|-------------|
| `Sub Group` | *(empty)* | Which [bake sub-group](/concepts/Workflow.md#bake-spline-grouping) this spline belongs to. Match it to the road splines it should fuse with |
| `Chord Tolerance (cm²)` | 1.0 | How far a chord may sit from the true curve when sampled for the mesh; `1.0` means "within 1 cm". Drives both the spline's own sampling and the magnetized target curve, so a magnetized segment never comes out at a different density than its neighbours |

A **closed** detail spline also carries the road spline's **Landscape** group, but flattens the area *enclosed by
its loop* rather than a ribbon — an open one ignores it entirely. See [Landscape](/integrations/Landscape.md).

## Baking

Give a detail spline the same actor and the same `Sub Group` as the road it belongs to and the whole thing bakes
into one seamless unit; a different sub-group bakes into that sub-group's mesh instead. See
[Bake: spline grouping](/concepts/Workflow.md#bake-spline-grouping).

## See also

- [Mark Spline Tool](/create-tools/MarkSplineTool.md) *(Pro)* — draw a mark spline.
- [Sidewalk Spline Tool](/create-tools/SidewalkSplineTool.md) *(Pro)* — draw a sidewalk spline.
- [The Road Model](/concepts/RoadModel.md) — the road spline is the primary, network-building spline.
- [Baking](/baking/BakeStaticMesh.md) — generate the meshes.
