# Landscape (Pro)
The `URoadSplineComponent` has similar properties to Unreal Engine [Landscape Splines](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-splines-in-unreal-engine): they deform and paint the Landscape underneath it. 

Closed [detail splines](/concepts/DetailSplines.md) — Mark and Sidewalk splines — carry the same **Landscape** group, but
they flatten the **area they enclose** instead of a ribbon along the road. See
[Detail splines](/integrations/Landscape.md#detail-splines) below.

## Setup
To use this feature, you first need to add a **RoadSplines** layer to Landscape:  
![Adding the RoadSplines edit layer to the Landscape](/img/landscape-add-layer.png)  

After that, for each `URoadSplineComponent` for which you want to use the Landscape features, you need to select the corresponding Landscape:  
![Selecting the target Landscape on a road spline component](/img/landscape-set.png)  

That's all, the landscape should update automatically whenever the `URoadSplineComponent` changes:  
![The Landscape deforming automatically as the road spline is edited](/img/landscape.gif)  

The landscape support feature is experimental, and if for some reason the landscape under the `URoadSplineComponent` hasn't updated, you can do it manually. To do this, in the context menu of the **RoadSpline layers**, you must select the **Update Splines** item:
![The Update Splines item in the RoadSplines layer context menu](/img/landscape-update.png)  

You can also repaint a single spline's imprint from its own **Details** panel with the **Update Landscape** button in the
**Landscape** group.

## Properties

The **Landscape** group of the component's **Details** panel. The same eight properties exist on a road spline and on a
detail spline; where the meaning differs, the difference is described in
[Detail splines](/integrations/Landscape.md#detail-splines).

| Property | Default | Description |
|----------|---------|-------------|
| `Landscape` | none | The Landscape actor this spline deforms and paints. Leave it empty to switch the whole feature off for this spline. |
| `Landscape Blend Mode` | `Default` | How overlapping splines resolve their heights. `Default` uses the project-wide setting (**Project Settings → Plugins → Meta Road Editor → Landscape → Landscape Blend Mode**, itself `Maximum`). `Maximum` takes the higher of the overlapping splines, so end-to-end junctions close up by themselves. `Legacy` blends the way a stock Unreal landscape spline does, and always wins over `Maximum` where the two overlap. |
| `Landscape Layer Name` | none | Paint layer written under the spline — see [Paint](/integrations/Landscape.md#paint). `None` = nothing is painted. |
| `Landscape Layer Factor` | 1.0 | Width of the **painted** band's fade, as a fraction [0–1] of `Landscape Side Falloff`. `0` ends the paint exactly at the flattened area's edge; `1` fades it out over the same distance as the terrain. |
| `Landscape Side Falloff` | 1000 | Distance [cm] over which the terrain eases sideways back to its original shape. |
| `Landscape Side Offset` | 0 | Signed [cm]. Positive widens the flattened band beyond the outer lane edges; negative narrows it inward. |
| `Landscape Resolution` | 512 | Sampling step [cm] along the spline. Lower = the flattened band follows tight curves more closely, at the cost of a slower update. |
| `Landscape Offset` | 50 | How far [cm] below the road surface the terrain is placed. |

```{note}
`Landscape Side Offset` is **signed** — a negative value pulls the flattened band inward, which is the usual way to keep
a hard shoulder or a verge un-flattened. Narrow it past half the road width and the two edges would cross; instead of
turning the band inside out, it collapses to the road's center line. It is the only signed property in the group —
`Landscape Side Falloff`, `Landscape Layer Factor`, `Landscape Resolution` and `Landscape Offset` are all clamped at 0.
```

```{tip}
To vary the deformation **along** a road spline instead of using one setting for its whole length, add the
[Landscape Attribute](/attributes/LandscapeAttribute.md) to the section center line. Its keys override
`Landscape Layer Factor`, `Landscape Side Falloff`, `Landscape Side Offset` and `Landscape Offset` per position, and
blend smoothly between keys.
```

## Paint
`URoadSplineComponent` supports [Landscape Paint Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine).  
In the example below, two paint layers (A and B) have already been created:  
![Two Landscape paint layers A and B set up in Paint Mode](/img/landscape-paint2.png)  

Now you just need to specify the **Landscape Layer Name** of the drawing layer, and the landscape under the `URoadSplineComponent` will be painted automatically:  
![The Landscape painted automatically beneath the road spline](/img/landscape-paint.png)  

Painting works the same way for a detail spline: the layer is written over the enclosed area, faded out by
`Landscape Layer Factor`.

## Detail splines

A **Mark spline** or **Sidewalk spline** ([detail splines](/concepts/DetailSplines.md)) can deform the Landscape too.
Assign a **Landscape** in its **Details** panel exactly as you would on a road spline; the same eight properties and the
same **Update Landscape** button are there.

The geometry, however, is different. A road flattens a **ribbon** derived from its lane widths. A detail spline has no
lanes and no width — what it has is an enclosed region, so it flattens **the area inside its loop**, sunk by
`Landscape Offset` and surrounded by a falloff skirt that fades outward over `Landscape Side Falloff`. The flattened
area is not level: it takes the height of the loop's own nodes and interpolates across the interior, so an island
that slopes with the road carries that slope into the terrain.

```{important}
This is gated on a **closed loop**. An open detail spline ignores the Landscape group entirely — nothing is deformed
and nothing is painted. Sidewalk splines are always closed; on a Mark spline, switch **Spline → Closed Loop** on (or
draw it with **Closed Loop** enabled in the [Mark Spline Tool](/create-tools/MarkSplineTool.md)).
```

![A closed sidewalk island with its Landscape group assigned, the terrain flattened inside the ring](/img/landscape-fill.png)

### What differs from a road spline

| Behavior | Road spline | Detail spline (closed loop) |
|-----------|-------------|-----------------------------|
| What is deformed | A ribbon following the lane edges | The area enclosed by the loop, plus an outward falloff skirt |
| `Landscape Side Offset` | Moves the two ribbon edges apart (positive) or together (negative) | **Dilates** (positive) or **erodes** (negative) the whole filled area |
| `Landscape Resolution` | The sampling step along the spline | Only a **maximum chord length** — the ring is already sampled adaptively (see below), so this just subdivides chords that came out longer than it, typically on long straight runs |
| Per-position variation | The [Landscape Attribute](/attributes/LandscapeAttribute.md) on the section center line | Not available — a detail spline has no lane sections to hold attribute keys |

The boundary a detail spline flattens is the **same ring the bake uses**, sampled adaptively by the component's
`Chord Tolerance (cm²)` (the **Magnetic** group). That has a useful consequence: if the loop's segments are magnetised
onto road geometry, the terrain edge follows that geometry exactly, curve for curve, rather than cutting the corners of
a fixed-step approximation.

```{note}
Erosion has a limit. A negative `Landscape Side Offset` deeper than the narrowest part of the island turns the ring
inside out; rather than corrupt the terrain, the fill is dropped for that spline — the deformation simply disappears.
If an island stops flattening after you lower `Landscape Side Offset`, raise it back toward 0.
```

Road splines and detail splines share one Landscape edit layer and resolve against each other by
`Landscape Blend Mode`, exactly as two overlapping roads do — an island fill and the road ribbon underneath it blend
the same way.

```{tip}
Deleting a spline that had a Landscape assigned now erases its imprint automatically — no manual **Update Splines** pass
is needed to clean up after removing a road or an island.
```

## See also

- [Detail Splines](/concepts/DetailSplines.md) — Mark and Sidewalk splines, and how their nodes magnetise onto the road.
- [Landscape Attribute](/attributes/LandscapeAttribute.md) — vary the deformation along a road spline.
- [Baking](/baking/BakeStaticMesh.md) — generate the road meshes that sit on the deformed Landscape.
- [Zone Graph](/integrations/ZoneGraph.md) — another Pro integration driven from road lane data.
