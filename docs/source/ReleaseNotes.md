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
    - Road profiles, markings, curbs and attributes have been added separately assets. See [Presets](Presets.md).
  - More advanced **Lane Types** have been added and the ability to create new **Lane Types** has become available. See [Lane Types](ProcedureGenerationTool.md#mesh-lane-materials).
  - Improved approach to assigning materials to road lanes. See [Lane Types](ProcedureGenerationTool.md#mesh-lane-materials).