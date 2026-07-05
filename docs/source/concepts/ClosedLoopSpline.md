# Closed-Loop Splines

A closed-loop **URoadSplineComponent** lets you place various "islands" or extra road marks on roads, such as refuge islands, pedestrian crossings, or arrows:  
![alt text](/img/loop-sample1.png)  

![alt text](/img/loop-sample2.png)  

![alt text](/img/loop-sample3.png)  

To start using a closed-loop spline, set two parameters on the **URoadSplineComponent** in the **Details Panel**:
  - Set **Spline -> Closed Loop** to ```true```
  - Set **Road -> RoadLayout -> LoopedRoadZone** to a ```Driving``` or ```Sidewalk``` [Road Zone](/concepts/RoadZones.md)

![alt text](/img/loop-init.png)  

After this, the **URoadSplineComponent** turns into a familiar polygon-drawing tool:  
![alt text](/img/loop-moving.gif)  

In the [Draw Spline Tool](/create-tools/DrawSplineTool.md) you can start drawing a closed-loop **URoadSplineComponent** immediately. To do this, set the following parameters in the tool:
  - Set **Road Spline -> Loop** to ```true```
  - Set **Road Spline -> LoopedRoadZone** to ```Driving``` or ```Sidewalk```

![alt text](/img/loop-drawing.gif)  

In the **Details Panel** of the **URoadSplineComponent** you can set the texture-coordinate parameters for the fill — angle and scale (`LoopedRoadZoneTexAngle` / `LoopedRoadZoneTexScale`):
![alt text](/img/loop-tex.gif)  

```{important}
Keep the drawn "islands" in the **same actor _and_ `SubGroup`** as the main road surface (the logically related **URoadSplineComponent**s). That way [baking](/concepts/Workflow.md#bake-spline-grouping) generates the whole road section as a single seamless unit.
```
