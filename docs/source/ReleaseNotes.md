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
  - Fixed decales generation in the **Build Mesh Tool**
  - Fixed ctrl+z in the **Draw Spline Tool**
  - Fixed landscape layer painting in UE5.7
  - Supported of Mac
  
**v2.0.5**  
  - Fixed landscape spline intersections
  - Added collision profiles to the [Build Mesh Tool](ProcedureGenerationTool.md)

**v2.0.6**  
  - Fixed UV maps for long road splines
  - Fixed wrong error messages in the **Build Mesh Mode** 
  - Fixed the movement of multiple road actors simultaneously
  
**v2.0.7** 
  - Fixed UV maps bug from v2.0.6 release

**v2.1.0**
  - The mechanism of preset has been completely refacted:
    - **UMetaRoadPreset** has been deprecated and is no longer used.
    - Road profiles, markings, curbs and attributes have been added as separate assets. See [Profiles](Presets.md).
  - More advanced **Lane Types** have been added and the ability to create new **Lane Types** has become available. See [Lane Types](ProcedureGenerationTool.md#mesh-lane-materials).
  - Improved approach to assigning materials to road lanes. See [Lane Types](ProcedureGenerationTool.md#mesh-lane-materials).
  
**v2.2.0**
  - Ability to create a road profile from a selected road section 
  - Ability to automatically align the width of lanes at connections 
  - Quick lane direction change
  - Ability to quickly re-attach a road spline between different actors
  - Automatic fit of the width of the lanes at the end of the spline 
  - Added Landsacpe Attribute
  - FixedG of "shooting triangles" in the landscape due to sharp spline curvature
  
 **v2.3.0**
  - New [Curb Cut](AttributeModes.md#curb-cut-attribute-pro) road attribute
  - New [Sidewalk Height](AttributeModes.md#sidewalk-height-attribute) attribute
  - Improved UI/UX for working with road attributes 
  - Added attribute spline mesh collision
  - Fixed crashes when working with road attributes
  - Improved "Sidewalk Height" workflow
  - Fixed build for linux

 **v2.4.0**
   - Added [Polygon Profile](Presets.md#polygon-profile-pro) includes new [Attribute](AttributeModes.md#polygon-attribute-pro) , and  [Polygon Editor](Presets.md#polygon-editor)
   - Supported of [Crosswalk](DrawCrosswalkTool.md)
   - Minor fixes and imporovments 
   
 **v2.5.0**
	- Refacted (renamed): FLaneInstance -> FRoadZone, FLaneType -> FRoadZoneType, FLaneTypeDetails -> FRoadZoneTypeDetails, etc
	- Hot fix: generated mesh vertex Z 