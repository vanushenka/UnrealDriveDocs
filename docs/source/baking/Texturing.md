# Texturing

How materials and texture coordinates land on the generated road surface: which material a lane gets, what the
three UV channels are for, and how to control texture density.

## Lane materials

Every road lane has a `Lane Type`, and each type carries a `Default Material` set in **Project Settings**.

![The Lane Type property shown on a selected road lane](/img/lane-type.png)

![The Default Material assigned to a Lane Type in Project Settings](/img/lane-type-material.png)

The material is resolved in this order, first one set wins:

1. `Override Material` on the selected lane's [Road Zone](/concepts/RoadZones.md#road-zones-per-surface), edited
   in [Section Mode](/editing/SectionMode.md#selecting-a-lane):  
   ![Overriding the default lane material on a selected road lane](/img/lane-type-material-override.png)
2. Override in the road's [build settings](/baking/Triangulation.md#where-to-find-these-settings), per mesh layer:  
   ![The Lane Type material override in the road's Build Settings](/img/lane-material-build-settings.png)
3. `Default Material` of the [Lane Type](/concepts/RoadZones.md#zone-types-project-wide)
   ![The Default Material assigned to a Lane Type in Project Settings](/img/lane-type-material.png)

## The three UV channels

| Channel | Runs across | Good for |
|---------|-------------|----------|
| **UV0** | a single **lane**, normalized | ruts, tram tracks, wheel-path wear |
| **UV1** | the **whole road**, normalized | patches, repairs, puddles |
| **UV2** | the surface at a **uniform real-world density** | asphalt, dirt, detail textures that must keep their size everywhere |

![The UV0 per-lane and UV1 left/right texture-coordinate channels on the road surface](/img/TexCoords.png)

UV0 and UV1 are normalized, so their density follows the road's width — that is the point of those channels. UV2
is the one that keeps a constant texel size.

To visualize them, apply the **UV0 Debug** or **UV1 Debug** preset material:

![The UV0 Debug and UV1 Debug preset materials visualizing the texture-coordinate channels](/img/debug-tex-coords.png)

## UV density

**Default UV Density** (in the [Triangulation](/baking/Triangulation.md) settings) sets the density of the whole
generated surface in **UV units per centimetre**. The default `0.003` means one tile per about 333 cm; halving it
doubles every tile everywhere.

It drives UV2 of the road lanes, **all** UV channels of the filled shapes — [closed-loop
fills](/concepts/ClosedLoopSpline.md), [crosswalks](/create-tools/DrawCrosswalkTool.md), [chevrons and island
fills](/create-tools/MarkSplineTool.md), sidewalk-spline surfaces, [polygon-profile](/profiles/PolygonProfile.md)
shapes — and the along-the-stripe coordinate of markings. Curbs and lofted cross-sections have their own scales
and are unaffected.

### Per-zone overrides

Two levels can replace the road-wide default, first one set wins:

1. **One surface** — `Override UV Density` on its [Road Zone](/concepts/RoadZones.md#road-zones-per-surface).
2. **A whole zone type** — `Override UV Density` on the
   [Zone Type](/concepts/RoadZones.md#zone-types-project-wide), to give every sidewalk a finer paving texture
   than the asphalt, for example.

Both are **absolute** densities that replace the default rather than scaling it; a shape's own `Texture > Scale`
still multiplies on top of whichever wins.

```{note}
Editing a Zone Type in Project Settings does **not** rebuild the road — press **Update** in the Meta Road panel,
or re-bake. The same is true of its material and priority.
```

Giving two zones different densities deliberately cuts the tiling at their shared edge: `Driving` and `Marking`
both bake into `RoadSurface` and share one UV space. That is usually what you want, and it is why the density is
one number by default.

## Per-shape Texture group

Every shape that produces a filled surface — crosswalk, chevron, closed-loop fill, sidewalk-spline surface,
polygon-profile shape — carries the same **Texture** group:

| Property | Default | Meaning |
|----------|---------|---------|
| `Angle` | 0° | Rotation of the texture about the shape's center |
| `Scale` | 1.0 | **Multiplier** on the UV density: `1.0` = the same density as the road surface |
| `Shift` | (0, 0) | Offset in **world centimetres**, along world X/Y |

`Shift` slides the texture across the ground by exactly that many centimetres and stays put when the density or
`Scale` changes, so use it to line a pattern up with a physical feature. Each shape keeps its own texture origin,
so neighbouring shapes tile independently.

```{warning}
**Changed in 3.1.** Filled shapes used to normalize the texture to their own bounding box, so `Scale = 1.0` meant
"one tile across this shape" whatever its size. They now use the global density instead, so **existing crosswalks,
chevrons, islands, sidewalk fills and polygon shapes change appearance** and may need `Scale` re-tuned — roughly by
`bbox_cm × Default UV Density`. The former `Texture Angle` / `Texture Scale` properties were also merged into this
group without redirects, so their saved values reset to the defaults on the first load.
```

## Vertex color

For road-surface materials, use the **Vertex Color** attribute to mask where the UV0/UV1 textures appear — puddles,
ruts, patches. It removes the artifacts at seams where several road splines meet:

![Vertex color removing texture artifacts at seams where road spline components meet](/img/VertexColor2.gif)

MetaRoad writes a color at the center of the road, another along its edges and where lanes intersect, controlled by
the Drive Surface build settings:

![Suggested vertex color parameters for the Drive Surface material](/img/VertexColor3.png)

![Vertex colors applied at the mesh center, edges, and lane intersections](/img/VertexColor.png)

For complex intersections you may still need to paint vertices by hand in **Mesh Paint** mode.

## See also

- [Baking](/baking/BakeStaticMesh.md) — running a bake and where the generated assets go.
- [Triangulation](/baking/Triangulation.md) — where `Default UV Density` and the per-channel scales live.
- [Road Zones](/concepts/RoadZones.md) — the zones that can override the density.
