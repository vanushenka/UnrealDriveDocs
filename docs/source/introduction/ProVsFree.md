# Pro vs Free

MetaRoad ships in two editions. **Pro** contains everything the **Free** edition has, plus the tools, attributes and
integrations listed below.

```{important}
The two editions are separate plugins and cannot be installed in the same engine at the same time — see
[Installation](/introduction/Installation.md).
```

## Only in Pro

### Create tools

- [Intersection Tool](/create-tools/IntersectionTool.md) — quickly generate typical intersections
- [Roundabout Tool](/create-tools/RoundaboutTool.md) — draw circular roundabouts and ring roads
- [Crosswalk Tool](/create-tools/DrawCrosswalkTool.md) — pedestrian crossings

### Detail splines

[Detail splines](/concepts/DetailSplines.md) — the Mark and Sidewalk splines that add surface details on top of a road
network — are Pro in full: the draw tools, the components, the viewport editing and the baked geometry.

- [Mark Spline Tool](/create-tools/MarkSplineTool.md) — chevron guide islands, stripe markings along the spline,
  repeated [Polygon Profile](/profiles/PolygonProfile.md) stamps, a filled surface zone inside a closed loop, and
  closed-loop **Fill Pattern**s: **Waffle (Box Junction)** and **Diagonal Hatch (Guide Island)**.
- [Sidewalk Spline Tool](/create-tools/SidewalkSplineTool.md) — a raised sidewalk surface filling a closed outline plus
  the curb swept around its boundary, with per-node height, curb profile and **Curb Cut** ramps.
- **Magnetism**, shared by both — drag a node onto a **lane corner** or another **spline node** on the same actor to
  link it, and it follows the road as you keep editing. Flag a segment as **Magnetic Segment** and a whole chain of
  them (a *run*) follows the road's real edge — through curb cuts, crossings and junction seams — with no gap to
  patch up. Per-point **Tangent Mode** (Auto / Aligned / Broken) controls the shape between the links.
- **Landscape from a closed loop** — a closed Mark or Sidewalk spline flattens the terrain inside its outline, with
  a falloff skirt outward; see [Landscape support](/integrations/Landscape.md).

### Attributes and shaping

- [Landscape support](/integrations/Landscape.md) and the [Landscape attribute](/attributes/LandscapeAttribute.md) —
  deform the Unreal landscape to follow a road spline, or the area enclosed by a closed detail spline
- [Curb Cut attribute](/attributes/CurbCutAttribute.md) — sidewalk ramps. Besides sidewalk lanes it can be added to
  the center line of a **closed sidewalk island**, where the new `Depth` controls how far the ramp reaches inward;
  a [Sidewalk spline](/create-tools/SidewalkSplineTool.md) node can carry the same ramp directly
- [Polygon attribute](/attributes/PolygonAttribute.md) (e.g. for road arrows) and
  [Polygon profile](/profiles/PolygonProfile.md), including its asset editor and inner contours
  ([holes](/profiles/PolygonProfile.md#holes))
- [Lofting attribute](/attributes/LoftingAttribute.md) — extruded cross-sections for bridges and interchanges

### Integrations

- [ZoneGraph generation](/integrations/ZoneGraph.md) — AI navigation data
- [PCG integration](/integrations/PCG.md) — the **Get Road Lane Data** node, for driving PCG graphs from the road
  network

```{note}
The Free edition also ships without the ready-made **Arrows** and **Lofting** sample profiles, since the attributes
that use them are Pro.
```

## Included in Free

Everything else, including the complete create → edit → bake loop: the
[Draw Spline tool](/create-tools/DrawSplineTool.md), every [Edit](/editing/SplineMode.md) sub-mode, the live preview,
[baking to static meshes](/baking/BakeStaticMesh.md), [FBX export](/baking/FbxExport.md), the
[Generate attributes](/attributes/GenerateAttributes.md) (spline mesh, component and actor templates) and the
[profiles and presets](/profiles/Profiles.md) they use.

In particular, these are **not** Pro features:

- **[Surface density](/baking/Triangulation.md#surface-density)** — fill the road surface with generated vertices
  at a target edge length, in either of two modes, so it can drape, smooth and carry detail
- **[Edge profile](/baking/Triangulation.md#edge-profile)** and the
  [Cross Section attribute](/attributes/CrossSectionAttribute.md) — sink the driving surface toward its edges
  into a gutter, authored along the road
- [Traffic Controller](/traffic/TrafficController.md) and the [Signal attribute](/attributes/SignalAttribute.md) —
  traffic lights with phases and a runtime clock
- [Road Zone attribute](/attributes/RoadZoneAttribute.md) — vary a lane's surface type and materials along its length
- **Split Spline** — cut a road spline in two at a point, from the section context menu
  (see [Section Mode](/editing/SectionMode.md))
- [Sidewalk Height attribute](/attributes/SidewalkHeightAttribute.md) on a road's sidewalk lanes (closed-loop
  sidewalk islands need a [Sidewalk spline](/create-tools/SidewalkSplineTool.md), which is Pro)
- [Road Always Visible](/misc/Visibility.md) and the [Performance](/misc/Performance.md) view-LOD settings
- The Blueprint **Generate Asset** lifecycle and its component nodes — see
  [Generate Attributes](/attributes/GenerateAttributes.md)

## See also

- [About MetaRoad](/introduction/About.md) — what the plugin does.
- [Installation](/introduction/Installation.md) — installing the plugin.
