# Release Notes

**v2.0.2**  
  - Added **ConvertSplineToPolyline_InDistanceRange2()** method to URoadSplineComponent
  - Fixed GraphOp for **Build Mesh Tool**
  - Fixed redirects (Engine.ini -> CoreRedirects)
  - Fixed ZoneGraphData connections
  - Fixed default road materials assets
  
**v2.0.3**  
  - Fixed ZoneGraphData connections
  - Added **LandscapeLayerFactor** property for URoadSplineComponent
  - Added **ZoneTags** property for FRoadLane
    
**v2.0.4**  
  - Fixed decals generation in the **Build Mesh Tool**
  - Fixed ctrl+z in the **Draw Spline Tool**
  - Fixed landscape layer painting in UE5.7
  - Supported of Mac
  
**v2.0.5**  
  - Fixed landscape spline intersections
  - Added collision profiles to the [Build Mesh Tool](/baking/BakeStaticMesh.md)

**v2.0.6**  
  - Fixed UV maps for long road splines
  - Fixed wrong error messages in the **Build Mesh Mode** 
  - Fixed the movement of multiple road actors simultaneously
  
**v2.0.7** 
  - Fixed UV maps bug from v2.0.6 release

**v2.1.0**
  - The mechanism of preset has been completely refactored:
    - `UMetaRoadPreset` has been deprecated and is no longer used.
    - Road profiles, markings, curbs and attributes have been added as separate assets. See [Profiles](/profiles/Profiles.md).
  - More advanced **Lane Types** have been added and the ability to create new **Lane Types** has become available. See [Lane Types](/baking/BakeStaticMesh.md#mesh-lane-materials).
  - Improved approach to assigning materials to road lanes. See [Lane Types](/baking/BakeStaticMesh.md#mesh-lane-materials).
  
**v2.2.0**
  - Ability to create a road profile from a selected road section 
  - Ability to automatically align the width of lanes at connections 
  - Quick lane direction change
  - Ability to quickly re-attach a road spline between different actors
  - Automatic fit of the width of the lanes at the end of the spline 
  - Added Landscape Attribute
  - FixedG of "shooting triangles" in the landscape due to sharp spline curvature
  
 **v2.3.0**
  - New [Curb Cut](/attributes/CurbCutAttribute.md) road attribute
  - New [Sidewalk Height](/attributes/SidewalkHeightAttribute.md) attribute
  - Improved UI/UX for working with road attributes 
  - Added attribute spline mesh collision
  - Fixed crashes when working with road attributes
  - Improved "Sidewalk Height" workflow
  - Fixed build for linux

 **v2.4.0**
  - Added [Polygon Profile](/profiles/PolygonProfile.md) includes new [Attribute](/attributes/PolygonAttribute.md) , and  [Polygon Profile Editor](/profiles/PolygonProfile.md)
  - Supported of [Crosswalk](/create-tools/DrawCrosswalkTool.md)
  - Minor fixes and improvements 
   
 **v2.5.0**
  - Refactored (renamed): FLaneInstance -> FRoadZone, FLaneType -> FRoadZoneType, FLaneTypeDetails -> FRoadZoneTypeDetails, etc
  - Hot fix: Height (Z coordinates of vertices) of the generated mesh

 **v3.0.0**
  - Unified **Meta Road** editor mode — a single entry point for all road authoring (drawing, editing, live preview, baking) with an integrated tile palette (Create / Edit / Bake / Misc)
  - Baking is now a **mode action** ([Bake Selected / Bake All](/baking/BakeStaticMesh.md), asynchronous with a progress notification); the separate interactive "Build Mesh Tool" was removed
  - New **Schematic / Preview** view toggle with a live, non-destructive mesh preview
  - New [FBX Export](/baking/FbxExport.md)
  - New [Roundabout Tool](/create-tools/RoundaboutTool.md) and [Chevron Marking Tool](/create-tools/ChevronMarkingTool.md) *(Pro)*
  - Road-spline editing is now available even outside the Meta Road editor mode
  - Documentation fully restructured for this release