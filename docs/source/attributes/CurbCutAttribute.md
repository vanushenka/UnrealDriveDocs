# Curb Cut Attribute (Pro)

Creates **curb cuts** (dropped curbs) on sidewalks — the lowered ramp where a sidewalk meets a crossing or a
driveway. The key marks the **center** of the cut and the attribute reshapes the sidewalk around it procedurally.

Unlike [Sidewalk Height](/attributes/SidewalkHeightAttribute.md), this attribute carves its own geometry: it adds the
vertices the ramp needs, so the cut stays crisp however short it is, and the curb along the edge drops with it.

## Where it can be added

The attribute is offered on two hosts, both of them sidewalk surfaces:

| Host | How to target it | How far the cut reaches |
|------|------------------|-------------------------|
| **A sidewalk lane** — any lane whose [Road Zone](/concepts/RoadZones.md) is a `Sidewalk` | select the lane | `Alpha` — a fraction of the lane width |
| **A sidewalk island ring** — the section center line of a **closed** spline whose `Looped Road Zone` is a `Sidewalk` | select the **section** (that targets its center line) | `Depth` — centimetres inward from the ring |

Anywhere else the attribute is simply not offered: a driving lane will not take it, and neither will the center line
of a spline that is not a closed sidewalk island.

```{note}
In earlier versions, targeting the section center line while the Curb Cut attribute was active could crash the
editor. See the [release notes](/reference/ReleaseNotes.md).
```

```{important}
The ramp is carved out of the vertices **inside** the sidewalk, so the road actor's
[`Surface Density Mode`](/baking/Triangulation.md#surface-density) must not be `None`. With density off, a
sidewalk has only its two edges and the cut degenerates into a single flat wedge whatever the profile says.
```

## Properties

| Property | Default | Description |
|----------|---------|-------------|
| `Is Cross` | off | Crossing-style cut: full strength all the way in, using the *A* width and falloff throughout. `Width B`, `Falloff B` and `Alpha` are then unused. |
| `Width A` | 200 cm | Length of the fully lowered part along the curb, at the curb itself [10–1000 cm]. The key sits in its middle. |
| `Falloff A` | 50 cm | Ramp added on **each** side of `Width A`, at the curb [10–1000 cm]. |
| `Width B` | 200 cm | Length of the fully lowered part at the **far edge** of the cut, so the cut can taper as it goes inward (when `Is Cross` is off). |
| `Falloff B` | 0 cm | Ramp on each side of `Width B`, at the far edge; `0` = a straight end there (when `Is Cross` is off). |
| `Alpha` | 0.5 | **Sidewalk lanes only.** How far across the lane width the cut reaches [0.1 = inner edge … 0.5 = center … 1.0 = outer edge] (when `Is Cross` is off). |
| `Depth` | 200 cm | **Island rings only.** How far *into* the island the cut reaches [10–2000 cm]. |
| `Mesh Density` | 4 | Subdivisions per profile span — the topology density of the generated ramp [1–10]. |
| `Smooth` | off | Rounded rather than straight ramps. |

```{important}
`Alpha` and `Depth` are the same control for two different hosts, and only one of them is read at a time. On a
**lane**, the cut's extent is `Alpha` — a fraction of the lane width. On an **island ring** there is no lane width
for it to be a fraction of, so the extent is `Depth`, in centimetres inward from the ring. Editing the other one has
no effect on that host.
```

The *A* pair describes the profile **at the curb** (the sidewalk's road-side edge, or the island ring itself) and the
*B* pair the profile **at the far edge** of the cut; the width and falloff blend from one to the other as the cut
goes inward. Equal *A* and *B* values give a straight-sided cut; a smaller *B* width gives a wedge, as under a
driveway ramp.

![A curb cut (dropped curb) generated on a sidewalk](/img/curb-cut.gif)

```{tip}
On an island ring, a cut placed near the closed spline's start point wraps around the seam — it is measured along the
ring, so it does not get clipped at the spline's zero point.
```

```{note}
**Changed in 3.2.0.** The ramp now carries across the seam into **whatever abuts it** — where a
[Sidewalk spline](/create-tools/SidewalkSplineTool.md) meets a road's sidewalk lane, that lane and its curb ramp
down with it. On a closed-loop road spline the ramp also pointed *out* of the island; it now always ramps inward.
```

```{important}
**Breaking change in 3.2.0.** A cut on an island ring used to produce roughly twice the cross-sections the same
`Mesh Density` gives on a lane. Both hosts now agree, so an **existing island-ring cut comes out about half as
dense** — raise its `Mesh Density` if a ramp that looked smooth now looks faceted.
```

## The same cut on a sidewalk spline

A node of a [Sidewalk Spline](/create-tools/SidewalkSplineTool.md) *(Pro)* can carry a curb cut directly: tick
**Curb Cut** in its **Selected Points** panel and edit the very same payload (`Is Cross`, `Width A` … `Depth`,
`Mesh Density`, `Smooth`), plus a `Curb Cut Offset` that slides the ramp along the boundary away from the node.

Both routes share one implementation, so the ramp is identical however it is authored — use whichever host the
sidewalk is built on.

## See also

- [Triangulation](/baking/Triangulation.md) — surface density, which the ramp needs in order to bend.
- [Attribute Mode](/editing/AttributeMode.md) — add and edit this attribute along a lane.
- [Attributes](/concepts/Attributes.md) — how attributes evaluate and are stored.
- [Sidewalk Height Attribute](/attributes/SidewalkHeightAttribute.md) — related sidewalk shaping; it also works on a
  closed-loop sidewalk island.
- [Sidewalk Spline Tool](/create-tools/SidewalkSplineTool.md) *(Pro)* — per-node curb cuts on a free-standing
  sidewalk.
