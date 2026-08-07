# PCG

*(Pro)*

MetaRoad exposes its road network to Unreal's **Procedural Content Generation** framework through a single
node, **Get Road Lane Data**. Point it at your road actors and it hands PCG one spline per lane, which you can
then scatter along, sample, or use as a boundary — so props, foliage, barriers and crowds can be generated
from the road layout instead of being placed by hand.

```{note}
The whole PCG module is part of the **Pro** edition. The Free edition ships without it, and without the
engine's PCG plugin dependency.
```

## Get Road Lane Data

Add the node to a PCG graph (search for *GetRoadLaneData*). Like the engine's own *Get Spline Data*, it takes
its actors from the node's **Actor Selector** settings, then collects every road spline on them and outputs
**one spline per matching lane**.

### Output

| Setting | Default | Meaning |
|---------|---------|---------|
| `Output Type` | `Polygon` | `Polygon` — a closed loop around the lane, made of its inner (`Alpha = 0`) and outer (`Alpha = 1`) edges. Use it as an area to fill or to mask against. `Polyline` — a single open line running along the lane |
| `Polyline Alpha` | `0.5` | Only for `Polyline`: where the line sits across the lane — `0` = inner edge, `0.5` = center, `1` = outer edge |

Every output carries tags you can filter on downstream: the lane's **zone type** name (`Driving`, `Sidewalk`,
…) and `RoadLane_<section>_<lane>`, which identifies exactly which lane it came from.

### Choosing which lanes come through

The three filters combine — a lane must pass all of them. Leave a filter empty to accept everything.

| Setting | Default | Meaning |
|---------|---------|---------|
| `Zone Struct Filter` | `All` | The kind of surface: `All`, `Driving` or `Sidewalk` |
| `Zone Type Filter` | *(empty)* | A list of [Zone Types](/concepts/RoadZones.md#zone-types-project-wide) to accept, e.g. `Parking` + `Bus`. Empty accepts all |
| `Zone Tags Filter` | *(none)* | A ZoneGraph tag mask; a lane must carry at least one matching tag. An empty mask accepts all. Tags come from the lane's `Zone Tags` in [Section Mode](/editing/SectionMode.md) |

```{tip}
Filtering is usually the cheapest way to control a graph: rather than generating over every lane and culling
later, ask for `Sidewalk` lanes only when you are scattering street furniture, or for a `Parking` zone type
when you are placing cars.
```

### Sampling

The lane edges are curves, so they are converted to polylines with the same adaptive sampling the mesh
generator uses — denser through tight curves, sparse on straights.

| Setting | Default | Meaning |
|---------|---------|---------|
| `Max Square Distance From Spline` | `5.0` | Chord tolerance in **cm²** — how far a straight segment may sit from the true curve before it is subdivided |
| `Min Segment Length` | `300.0` | Longest segment in **cm**; a straight lane still gets a point at least this often |

Both are trade-offs between fidelity and point count. Raise them for a coarse pass over a large city, lower
them when the shape of a curve matters.

```{note}
These control how the lane is **sampled for PCG**. They are independent of the road mesh's own
[triangulation settings](/baking/Triangulation.md) — changing them here never affects the baked road. The road
has its own segment-length cap (`Max Segment Length`, default 375) and its own, **linear**, `Error Tolerance`;
these two are separate properties, and this chord tolerance is **squared**.
```

## Typical uses

- **Scatter along a lane** — `Polyline` output at `Polyline Alpha = 1` gives the outer edge; scatter lamp
  posts or bollards along it.
- **Fill an area** — `Polygon` output of a `Sidewalk` lane, fed into a surface sampler, populates the pavement
  with pedestrians or clutter.
- **Mask** — use the road polygons to *subtract* from a landscape scatter, so foliage stops at the curb.

## See also

- [Road Model](/concepts/RoadModel.md) — what a lane is, and what `Alpha` means across its width.
- [Road Zones](/concepts/RoadZones.md) — the zone types and tags the filters work on.
- [ZoneGraph](/integrations/ZoneGraph.md) — the other route from a MetaRoad network into runtime data.
