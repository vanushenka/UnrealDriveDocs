# Release Notes

## v2.0.2
  - Added **ConvertSplineToPolyline_InDistanceRange2()** method to URoadSplineComponent
  - Fixed GraphOp for **Build Mesh Tool**
  - Fixed redirects (Engine.ini -> CoreRedirects)
  - Fixed ZoneGraphData connections
  - Fixed default road materials assets
  
## v2.0.3
  - Fixed ZoneGraphData connections
  - Added **LandscapeLayerFactor** property for URoadSplineComponent
  - Added **ZoneTags** property for FRoadLane
    
## v2.0.4
  - Fixed decals generation in the **Build Mesh Tool**
  - Fixed ctrl+z in the **Draw Spline Tool**
  - Fixed landscape layer painting in UE5.7
  - Supported of Mac
  
## v2.0.5
  - Fixed landscape spline intersections
  - Added collision profiles to the [Build Mesh Tool](/baking/BakeStaticMesh.md)

## v2.0.6
  - Fixed UV maps for long road splines
  - Fixed wrong error messages in the **Build Mesh Mode** 
  - Fixed the movement of multiple road actors simultaneously
  
## v2.0.7
  - Fixed UV maps bug from v2.0.6 release

## v2.1.0
  - The mechanism of preset has been completely refactored:
    - `UMetaRoadPreset` has been deprecated and is no longer used.
    - Road profiles, markings, curbs and attributes have been added as separate assets. See [Profiles](/profiles/Profiles.md).
  - More advanced **Lane Types** have been added and the ability to create new **Lane Types** has become available. See [Lane Types](/baking/Texturing.md#lane-materials).
  - Improved approach to assigning materials to road lanes. See [Lane Types](/baking/Texturing.md#lane-materials).
  
## v2.2.0
  - Ability to create a road profile from a selected road section 
  - Ability to automatically align the width of lanes at connections 
  - Quick lane direction change
  - Ability to quickly re-attach a road spline between different actors
  - Automatic fit of the width of the lanes at the end of the spline 
  - Added Landscape Attribute
  - FixedG of "shooting triangles" in the landscape due to sharp spline curvature
  
## v2.3.0
  - New [Curb Cut](/attributes/CurbCutAttribute.md) road attribute
  - New [Sidewalk Height](/attributes/SidewalkHeightAttribute.md) attribute
  - Improved UI/UX for working with road attributes 
  - Added attribute spline mesh collision
  - Fixed crashes when working with road attributes
  - Improved "Sidewalk Height" workflow
  - Fixed build for linux

## v2.4.0
  - Added [Polygon Profile](/profiles/PolygonProfile.md) includes new [Attribute](/attributes/PolygonAttribute.md) , and  [Polygon Profile Editor](/profiles/PolygonProfile.md)
  - Supported of [Crosswalk](/create-tools/DrawCrosswalkTool.md)
  - Minor fixes and improvements 
   
## v2.5.0
  - Refactored (renamed): FLaneInstance -> FRoadZone, FLaneType -> FRoadZoneType, FLaneTypeDetails -> FRoadZoneTypeDetails, etc
  - Hot fix: Height (Z coordinates of vertices) of the generated mesh

## v2.6.0
  - New [Lofting](/attributes/LoftingAttribute.md) attribute *(Pro)* — extrude 2D cross-section profiles along a lane into bridges, tunnels, and walls, with a dedicated 2D cross-section editor
  - New [Roundabout Tool](/create-tools/RoundaboutTool.md) *(Pro)* — draw circular roundabouts and ring roads
  - Roads are now **`AMetaRoad`** actors
  - **Spline grouping** — group a road's splines so they bake into one seamless mesh; added road underside generation
  - Added a segment **sampler** mode for generative attributes (by segment length / between keys)
  - Landscape improvements and smoother meshes on sharp spline curvature
  - Fixes: looped road marks, SVG-imported polygons, loft cap normals

## v2.7.0
  - New **Chevron Marking Tool** *(Pro)* — chevron guide-island markings (now the [Mark Spline Tool](/create-tools/MarkSplineTool.md))
  - **Drag & drop** — drag Mark / Polygon / Attribute profiles from the Content Browser straight onto a road lane
  - **Multiple lane selection** — edit several lanes at once
  - Dedicated **Road Profile editor**
  - New selected-key **overlay widget** and reworked attribute-editor UI
  - Fix: broken spline node handling

## v2.7.1
  - Fixed a baking bug where cleanup could **delete user meshes**
  - Added an **undoable Clean Strategy** for re-bakes — *Move to Trash* or *Permanent Delete* (see [Auto-cleaning](/baking/BakeStaticMesh.md#auto-cleaning-previous-assets))

## v3.0.0
  - Supported of UE5.8
  - Unified **Meta Road** editor mode — a single entry point for all road authoring (drawing, editing, live preview, baking) with an integrated tile palette (Create / Edit / Bake / Misc)
  - Baking is now a **mode action** ([Bake Selected / Bake All](/baking/BakeStaticMesh.md), asynchronous with a progress notification); the separate interactive "Build Mesh Tool" was removed
  - New **Schematic / Preview** view toggle with a live, non-destructive mesh preview
  - New [FBX Export](/baking/FbxExport.md)
  - **Closed-loop splines** to fill areas — plazas, parking lots, and intersection interiors (see [Closed-Loop Spline](/concepts/ClosedLoopSpline.md))
  - Roads can **drape onto the landscape** (Snap-to-Ground overlap strategy)
  - The generative attribute family "Curve" was renamed to **[Generate](/attributes/GenerateAttributes.md)** (Spline Mesh / Component / Actor / Lofting)
  - Road-spline editing is now available even outside the Meta Road editor mode
  - Documentation fully restructured for this release

## v3.1.0

### Major
  - New **[Detail Splines](/concepts/DetailSplines.md)** *(Pro)* — a second class of spline that lays surface detail on top of the road and bakes with it. Anchor a node to a lane corner, then flag a segment (or a whole chain) as **Magnetic Segment** to follow the road's real geometry, curb-cut ramps and junction seams included. Off by default, so existing content is unaffected
    - **[Mark splines](/create-tools/MarkSplineTool.md)**, replacing the Chevron Marking Tool — sweep a [Mark Profile](/profiles/MarkProfile.md) stripe, fill a closed loop with chevrons or a repeating pattern (`Waffle`, `Diagonal Hatch`), or stamp a [Polygon Profile](/profiles/PolygonProfile.md) at a fixed interval, with per-node overrides
    - **[Sidewalk splines](/create-tools/SidewalkSplineTool.md)** — a closed outline fills as a raised sidewalk with a [curb](/profiles/CurbProfile.md) around it, both driven by its [Road Zone](/concepts/RoadZones.md). A node can override the height or curb profile, and carry a **curb cut** directly
  - New **[Signal attribute](/attributes/SignalAttribute.md)** and **[Traffic Controller](/traffic/TrafficController.md)**, both **Free** — place traffic and pedestrian lights on lanes, link them from the viewport and drive them through named phases from Blueprint or C++. The clock runs in PIE and packaged builds only; the light model still comes from a [Spline Mesh](/attributes/SplineMeshAttribute.md) or [Actor Template](/attributes/ActorTemplateAttribute.md) attribute
  - New **[Road Zone attribute](/attributes/RoadZoneAttribute.md)** — change a lane's surface type, material or texture density along its length without splitting it into more [lane sections](/concepts/RoadModel.md#lane-sections)
  - **Texturing rework** — one **[Default UV Density](/baking/Texturing.md#uv-density)** in UV per cm drives the whole surface (curbs and lofts excepted), overridable per [Zone Type](/concepts/RoadZones.md#zone-types-project-wide) and per [Road Zone](/concepts/RoadZones.md#road-zones-per-surface). Every filled shape carries one **[Texture](/baking/Texturing.md#per-shape-texture-group)** group — `Angle`, `Scale` and a new world-cm `Shift`. **Breaking:** filled shapes no longer normalize the texture to their own bounding box, so their appearance changes and `Scale` may need re-tuning
  - **Breaking: two property groups were merged without redirects, so their saved values reset on first load** — the per-shape `Texture` group, and *(Pro)* the Mark-spline `Chevron Profile` group, whose `Road Zone` now defaults to **Marking**
  - **`Sub Group` now applies to every road component** — Mark splines, Sidewalk splines and [Crosswalks](/create-tools/DrawCrosswalkTool.md) too, edited from a shared **Road → Sub Group** row. **Breaking:** generation is partitioned by sub-group for all of them, so each feature belongs to exactly one — check yours after upgrading

### Minor
  - **Per-point tangent modes on detail splines** *(Pro)* — `Auto`, `Aligned` and `Broken` in a unified **Spline Point Type** list, a matching **Tangent Type** on the draw tools, and a `Chord Tolerance (cm²)` driving the spline's sampling
  - **[Curb Cuts](/attributes/CurbCutAttribute.md) and [Sidewalk Height](/attributes/SidewalkHeightAttribute.md) on sidewalk island rings** — a curb cut *(Pro)* can now sit on the center line of a closed sidewalk island, where a new `Depth` replaces `Alpha`; a Sidewalk Height key there now lifts the island instead of leaving it flat
  - **Landscape** — Mark and Sidewalk splines *(Pro)* gained the [Landscape](/integrations/Landscape.md) group and flatten the area inside their closed loop. `Landscape Side Offset` lost its zero minimum here, on the road spline and on the [Landscape attribute](/attributes/LandscapeAttribute.md), so a negative value narrows the band inward
  - New **[Split Spline](/editing/SectionMode.md)** — right-click a section to cut a road spline in two. The second half becomes a new spline on the same actor, taking the connections of the lanes that moved with it. Closed loops are not supported
  - **Schematic view LOD** — the schematic thins out with distance and stops drawing past a cull threshold, tuned in **Project Settings → Plugins → Meta Road Editor → Performance**. A new `Road Always Visible` toggle in [Visibility](/misc/Visibility.md) draws roads outside the Meta Road mode
  - **[Generate attribute](/attributes/GenerateAttributes.md) Blueprint API** — the new `Add Generated Component` node creates a component per call, so a descriptor can emit one per segment; `Begin` / `End Generate Asset` now fire once per output actor

### Fixes
  - Fixed: **Alt+dragging the first or last node of a road spline** could crash, stuttered from re-rasterizing the Landscape every frame, and sent the duplicated endpoint flying off
  - Fixed: **three failures from invalid targets or stale selection** — [Width Mode](/editing/WidthMode.md) handles from indices that no longer existed, targeting the section center line with **Curb Cut** or **Sidewalk Height** active, and a stale spline-point selection after undo or Split Spline
  - Fixed: **attribute-editor glitches** — a key that looked selected on every lane, the Selection panel showing a stale lane, a new center-line key's gizmo landing on the reference line, and six attribute types showing the generic icon
  - Fixed *(Pro)*: **per-point edits on detail splines could not be undone**, and anchored nodes ignored Add Lane / Delete Lane / Reverse Direction / Delete Section
  - Fixed: **only the first sub-group of an actor was rebuilt**, so the preview of the others went stale
  - Fixed: the **closed-loop fill could fail to draw in Schematic view**
  - Fixed *(Pro)*: **markings and curbs cracked against the road surface** — every feature line is now welded into the triangulation or matched onto the road's real edges, and one running off the surface is clipped
  - Fixed: **island curbs sat 0.5 cm below the lane curbs** they stitch to
  - Fixed: **Blueprint attribute descriptors lost components** created with Unreal's built-in *Add Component* node — use `Get Or Add Generated Component` instead
  - Fixed: **UV artefacts on bake** — splines shorter than ~5 m produced collapsed UVs, and UVs could drift between successive bakes of the same road
  - Fixed: materials used by detail splines and crosswalks could be **garbage-collected mid-bake** *(Pro)*, and a **material-verification error** appeared in the log after editing settings or a hot reload

## v3.2.0

### Major
  - New **[Surface density](/baking/Triangulation.md#surface-density)** — the road surface can be filled with generated vertices instead of being a strip of edge-to-edge triangles, so draping, smoothing and the gutter below finally have something to work on. One dial (`Target Edge Length`) and two modes: `Refined (Delaunay)` for anything with crossings, `Aligned rows (S-R)` for a single spline. Defaults to **`None`**, which reproduces the pre-3.2 mesh exactly — **an upgraded project is unchanged until you opt in**
  - New **[Edge profile](/baking/Triangulation.md#edge-profile)** and the **[Cross Section attribute](/attributes/CrossSectionAttribute.md)** — sink the driving surface toward its edges into a gutter, so a road drains instead of holding water. Depth, width and shape are authored along the road on the section center line. Needs surface density
  - **[Holes in a Polygon Profile](/profiles/PolygonProfile.md#holes)** *(Pro)* — a polygon can carry inner contours cut out of it, so one shape can be a ring, a stencilled letter or an arrow with a cut-out. Authored from the canvas context menu; the canvas also gained a translucent fill you can click to select

### Minor
  - **[Curb cuts](/attributes/CurbCutAttribute.md) now hold across the seam** *(Pro)* — the ramp carries into whatever abuts it, so a road's sidewalk lane ramps down with a Sidewalk spline's cut instead of standing at full height beside it. On a closed-loop spline the ramp no longer points out of the island. **Breaking:** an island-ring cut comes out about half as dense as before — raise its `Mesh Density`
  - **Normals are taken from the smoothed surface**, so shading matches the geometry you see. Any multi-spline road with `Smooth` on shades slightly differently
  - **[Preset mode](/editing/PresetMode.md) commits from the viewport** — `Apply To Selected` moved into the viewport bar where a drawing tool shows Accept, and is now just **`Apply`**
  - One more broken-line profile in the shipped **Mark** library

### Fixes
  - Fixed: the **Free edition's [Traffic Controller](/traffic/TrafficController.md)** failed to build in the Free package
  - Fixed *(Pro)*: a **magnetized detail spline lost its exact follow after a level load or an undo**, silently falling back to its own curve until the spline was edited again
  - Fixed: **undo and redo on a road spline** now rebuild the preview mesh and every detail spline anchored to it
  - Fixed *(Pro)*: **unlinking a node made the incoming segment snap**. It now keeps its shape
  - Fixed: a **constrained edge the triangulator refused to insert** was silent, showing up only as unexplained holes in the surface. It now reports how many were lost


