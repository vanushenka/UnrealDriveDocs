# Detail Splines

Besides road splines, MetaRoad has **detail splines** — supplementary authoring splines that add surface
details *on top of* an existing road network. Unlike a road spline (`URoadSplineComponent`), a detail spline has
**no lanes, sections, or connections**; it only draws extra geometry that is baked together with the road. The
road network itself is always built from road splines — see [The Road Model](/concepts/RoadModel.md) and
[The MetaRoad Workflow](/concepts/Workflow.md#create-roads-are-connected-splines).

There are two detail-spline types, both *(Pro)*:

| Detail spline | Component | Draws | Tool |
|---------------|-----------|-------|------|
| **Mark spline** | `UMarkSplineComponent` | Chevron guide-islands, stripe markings (a [Mark Profile](/profiles/MarkProfile.md)), and — when closed — a filled marking island | [Mark Spline Tool](/create-tools/MarkSplineTool.md) |
| **Sidewalk spline** | `USidewalkSplineComponent` | A raised **sidewalk surface** filling its outline, plus a **curb** swept along its boundary | [Sidewalk Spline Tool](/create-tools/SidewalkSplineTool.md) |

Both live on the same **`AMetaRoad`** actor as the road splines and contribute their geometry to the mesh at
[bake](/baking/BakeStaticMesh.md) time.

<!-- TODO 🖼 illustration: a road with a Mark chevron island and a Sidewalk running alongside it, each highlighted as a separate detail spline -->

## Magnetism

Both types share a common base (`UMagneticSplineComponent`) that lets their nodes **magnetically attach to road
geometry**, so a detail spline stays glued to the road as you keep editing instead of drifting when the road
changes.

- **Anchoring (linking).** Select a node, then **hold `Space` and drag** it onto a road target — a lane corner or
  another spline node on the same actor — to **link** it. A linked node then **rigidly follows** that target: move or
  reshape the road and the detail spline's node moves with it. Release `Space` while dragging to cancel. Linked nodes
  draw a marker (accent = resolved, red = the target was deleted). The **Break Link** button (or **Unlink** in the
  node's right-click menu) in the spline's **Selected Points** section frees a node again.

<!-- TODO 🎞 gif: Space-dragging a sidewalk node onto a lane corner, then reshaping the road so the node follows -->

- **Magnetic segments.** Toggle **Magnetic Segment** on a node to mark the *segment leaving it* as magnetic. A
  magnetic segment is drawn as a **green dashed** line and tries to follow the road edge: when **both** of its ends
  are anchored to the **same** road curve, its shape snaps onto that edge and the baked mesh routes along it;
  otherwise it stays an ordinary smooth segment. This is what lets a sidewalk edge or a marking hug a curved lane
  boundary exactly. The green dash highlights in the selection colour when the segment is selected, and clicking it
  selects that segment.

## Baking

Detail splines are baked together with the road surface. Keep them in the **same actor and `SubGroup`** as the
related road so everything fuses into one seamless unit — see
[Bake: spline grouping](/concepts/Workflow.md#bake-spline-grouping).

## See also

- [Mark Spline Tool](/create-tools/MarkSplineTool.md) *(Pro)* — draw a mark spline.
- [Sidewalk Spline Tool](/create-tools/SidewalkSplineTool.md) *(Pro)* — draw a sidewalk spline.
- [The Road Model](/concepts/RoadModel.md) — the road spline is the primary, network-building spline.
- [Baking](/baking/BakeStaticMesh.md) — generate the meshes.
