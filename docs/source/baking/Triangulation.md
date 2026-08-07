# Triangulation

The per-road settings that turn your road layout into triangles: how finely the splines are sampled, how dense
the surface is, how overlapping roads resolve their height, and how the result is smoothed and welded.

## Where to find these settings

Select the road actor → **Details** → **Meta Road** → **Build Settings** → **Edit...**. That opens the **Road
Build Settings** window, with **Triangulation** as its first section.

![The Road Build Settings window opened from the actor, with the Triangulation section expanded](/img/road-build-settings.png)  

```{note}
The settings are **not** listed in the actor's Details panel directly — only that **Edit...** button is. The
**[Preset](/editing/PresetMode.md)** tile shows the same sections inline against the live Preview, which is the
better place to tune them.
```

They apply to one **generation unit** — one `(AMetaRoad actor, SubGroup)` pair — not the whole level. Each mesh
layer below Triangulation (Drive Surface, Decals, Sidewalks, Curbs, Marks, …) has its own section; see
[Baking](/baking/BakeStaticMesh.md).

## Sampling the splines

How closely the boundary outlines follow the true spline curve.

| Property | Default | Meaning |
|----------|---------|---------|
| `Error Tolerance` *(Advanced)* | 5.0 cm | How far an outline may deviate from the curve before another point is added. Lower = smoother curves, more vertices |
| `Sidewalk Cap Error Tolerance` *(Advanced)* | 2.0 cm | The same, for the curved cap at the end of a sidewalk |
| `Max Segment Length` | 375 cm | The longest a sampled segment may be, so a straight lane still gets points at regular intervals |

```{important}
All three work **along the road only** — they shape the outline and place no vertex inside a lane. Filling the
surface is **Surface density** below, and the two are independent.
```

![A curved lane boundary sampled at a coarse and a fine Error Tolerance](/img/error-tolerance.png)  

## Surface density

By default a lane is a strip of triangles running edge to edge, with **no vertices inside it**. Nothing can then
drape onto the landscape, smooth, or carry a gutter. Surface density fills the surface so it can.

![The same road surface in wireframe with and without generated interior vertices](/img/road-surface-density2.png)  

| Property | Default | Meaning |
|----------|---------|---------|
| `Surface Density Mode` | **None** | Whether the surface is filled, and how |
| `Target Edge Length` | 150 cm | Target mesh-edge length, in every direction. Minimum 50 cm. Editable only when the mode is not `None` |

| Mode | Use it when |
|------|-------------|
| **None** *(default)* | You need no surface detail, draping or gutter. Reproduces the pre-3.2 mesh exactly |
| **Refined (Delaunay)** | **The default answer** — junctions, roundabouts, anything where splines cross |
| **Aligned rows (S-R)** | A single spline where a mesh running *with* the road reads better. Costs ~1.66× the vertices |

![The same lane in wireframe under None, Refined (Delaunay) and Aligned rows (S-R), side by side](/img/road-surface-density.png)

```{warning}
**`Aligned rows (S-R)` degenerates at junctions** — crossing lanes propose conflicting rows and one is dropped,
leaving a fan of thin triangles. Use `Refined (Delaunay)` wherever splines cross.
```

```{note}
Triangles come out at or below `Target Edge Length` with no angle under 30°, except where the road itself forces
one — splines crossing at a shallow angle, or a lane tapering to zero width.
```

## Edge profile

Sinks the driving surface toward the edge of the driveable area — a gutter, so water runs off the lane.

![A road cross-section with the edge profile lowering the surface into a gutter at both curbs](/img/edge-profile.png)  

```{important}
It takes **two** things: `Edge Profile` here, **and** a
[Cross Section attribute](/attributes/CrossSectionAttribute.md) on the section center line, where the depth and
width are authored. It also needs `Surface Density Mode` to be something other than `None` — with no interior
vertices the gutter comes out as one straight wedge.
```

| Property | Default | Meaning |
|----------|---------|---------|
| `Edge Profile` | off | Master switch for the gutter on this road |
| `Edge Profile Blend Radius` *(Advanced)* | 0 cm = auto | How far two roads' settings blend into each other along the edge. Raise it to smooth the handover at a junction |
| `Lane Cuts Are Edges` *(Advanced)* | on | Whether a lane that runs out mid-road counts as an edge and gets a gutter across its cut |

The edges it finds belong to the **merged driveable area**, so a lane boundary inside a junction stays flat, and
a spline end is a joint rather than an edge. A spline connected into another `AMetaRoad` takes that road's
settings, so the two meshes join without a step.

```{tip}
Rather than butting a lane on at full width, open its `Width` curve from zero. The taper leaves no cross-cut for
the profile to treat as an edge.
```

![Two roads meeting at a junction at a small and a large Edge Profile Depth, showing the handover smooth out](/img/edge-profile-blend-radius.png)

## Overlapping roads and the ground

Where two splines pass over the same place, one height has to win. **Overlap Strategy** decides which.

![Two roads crossing at different heights, resolved with Use Max Z and with Use Min Z side by side](/img/overlap-strategy.png)

| Strategy | At a shared point | Around it, within `Overlap Radius` |
|----------|-------------------|------------------------------------|
| **Use Max Z** *(default)* | The **higher** surface wins | The lower road is **lifted** toward it, ramping down to its own height at the edge of the radius. Use for an overpass or a road crossing a dip |
| **Use Min Z** | The **lower** surface wins | The higher road is **pulled down** toward it, ramping back up at the edge of the radius. Use for an underpass or a road cutting through a rise |
| **Snap to Ground** | Neither — every vertex is line-traced straight down onto the landscape | Nothing. `Overlap Radius` is **not used** in this mode |

| Property | Default | Meaning |
|----------|---------|---------|
| `Overlap Strategy` | Use Max Z | Which surface wins where splines cross — see above |
| `Overlap Radius` | 500 cm | How far the winning height reaches into the surrounding surface. Larger = a longer, gentler ramp into the crossing; `0` = the surfaces meet in a step |

```{note}
The blend only moves **interior** vertices — a road's own outer boundary keeps its authored height, so raising
`Overlap Radius` widens the ramp without dragging the road's edges out of place.
```

![The same crossing at a small and a large Overlap Radius, showing the ramp lengthen](/img/overlap-radius.png)

Only with **Snap to Ground**:

![A road draped onto hilly landscape with Snap to Ground](/img/overlap-snap-to-ground.png)

| Property | Default | Meaning |
|----------|---------|---------|
| `Snap Trace Channel` | WorldStatic | Collision channel the downward trace tests against |
| `Snap Trace Height Above` | 1000 cm | How far above each vertex the trace starts |
| `Snap Trace Depth Below` | 10000 cm | How far below each vertex it reaches |
| `Snap Ground Offset` | 0 cm | Offset above the hit point; negative sinks the road in |
| `Snap Trace Complex` *(Advanced)* | on | Trace against per-polygon collision. Off is faster |
| `Smooth After Snap` | off | Re-smooth after draping, so the road follows the terrain gently instead of every bump |

```{warning}
**Snap to Ground traces once per vertex, on the game thread.** Paired with a small `Target Edge Length` it stalls
the editor on every rebuild. Raise the edge length, or use a different overlap strategy.
```

[Landscape support](/integrations/Landscape.md) is the other half of this: draping fits the road to the terrain,
the Landscape settings deform the terrain to fit the road.

## Smoothing

| Property | Default | Meaning |
|----------|---------|---------|
| `Smooth` | on | Smooth the surface height where several splines meet, removing creases at their seams |
| `Smoothness` | 0.5 | How strong the smoothing is. Not linear — larger is smoother |

```{note}
**Changed in 3.2.0.** Normals now come from the smoothed surface, so shading matches the geometry you see. Any
multi-spline road with `Smooth` on will shade slightly differently.
```

![A junction where several splines meet, with Smooth off and on, showing the creases at the seams disappear](/img/triangulation-smooth.png)

## Welding and output

| Property | Default | Meaning |
|----------|---------|---------|
| `Vertex Snap Tolerance` *(Advanced)* | 0.01 cm | Points closer than this are welded into one vertex |
| `Split By Sections` | off | Split the road into one component per section instead of a single mesh |
| `Merge Sections Area Threshold` | 100 m² | With `Split By Sections` on, smaller sections merge into a neighbour |
| `Output Mesh Type` | Static Mesh | Static Mesh, or a Dynamic Mesh actor. Static Mesh needs no plugin at runtime |
| `Force Assign Material` *(Advanced)* | off | Ignore per-surface material overrides. A debugging aid |

## Texture density

| Property | Default | Meaning |
|----------|---------|---------|
| `Default UV Density` | 0.003 | Texture density of the whole surface, in UV per cm — see [UV density](/baking/Texturing.md#uv-density) |
| `UV0 Scale` | 0.0025 | Density along the road for UV0, which runs across a single **lane** — ruts, tram tracks, wheel-path wear |
| `UV1 Scale` | 0.001 | Density along the road for UV1, which runs across the **whole road** — patches, repairs, puddles |
| `UV Wrap Period` | 13 | How many tiles the along-the-road coordinate runs before wrapping. Keeps UVs precise on very long roads; a seam appears at the wrap |

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| The mesh looks coarse, and draping only moves its borders | `Surface Density Mode` is `None`. Set it to `Refined (Delaunay)` |
| The editor stalls on every edit | `Snap to Ground` with a small `Target Edge Length`. Raise the edge length |
| A warning says densification "stopped after N vertices" | `Target Edge Length` is too small for this road. Raise it, or split the network into smaller units |
| The gutter is one straight wedge whatever the `Exponent` | Density is `None`, or `Target Edge Length` is not below the attribute's `Falloff Width` |
| A step in the ground between two roads | They use a different `Depth`. Raise `Edge Profile Blend Radius` |
| The gutter is missing and the log says the contour could not be traced | Overlapping splines. Connect them instead of laying one over the other |

## See also

- [Baking](/baking/BakeStaticMesh.md) — running a bake, the per-layer settings and the UV channels.
- [Preset Mode](/editing/PresetMode.md) — tune these against the live preview.
- [Build Preset](/profiles/BuildPreset.md) — save the whole set as a reusable asset.
- [Cross Section Attribute](/attributes/CrossSectionAttribute.md) — where the gutter's shape is authored.
