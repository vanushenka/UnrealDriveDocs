# Closed-Loop Splines

A closed-loop `URoadSplineComponent` lets you place various "islands" or extra road marks on roads, such as refuge islands, pedestrian crossings, or arrows:  
![A closed-loop spline forming a refuge island on a road](/img/loop-sample1.png)  

![A closed-loop spline forming a pedestrian crossing fill](/img/loop-sample2.png)  

![A closed-loop spline forming a road arrow marking](/img/loop-sample3.png)  

To start using a closed-loop spline, set two parameters on the `URoadSplineComponent` in the **Details Panel**:
  - Set **Spline -> Closed Loop** to `true`
  - Set **Road -> RoadLayout -> LoopedRoadZone** to a `Driving` or `Sidewalk` [Road Zone](/concepts/RoadZones.md)

![The Closed Loop and LoopedRoadZone properties set in the Details Panel](/img/loop-init.png)  

After this, the `URoadSplineComponent` turns into a familiar polygon-drawing tool:  
![Editing a closed-loop spline as a polygon by moving its points](/img/loop-moving.gif)  

In the [Draw Spline Tool](/create-tools/DrawSplineTool.md) you can start drawing a closed-loop `URoadSplineComponent` immediately. To do this, set the following parameters in the tool:
  - Set **Road Spline -> Loop** to `true`
  - Set **Road Spline -> LoopedRoadZone** to `Driving` or `Sidewalk`

![Drawing a closed-loop spline directly with the Draw Spline Tool](/img/loop-drawing.gif)  

In the **Details Panel** of the `URoadSplineComponent` you can set the texture-coordinate parameters for the fill — the **Texture** group (`LoopedTexture`: angle, scale and shift):
![Adjusting the fill texture angle and scale of a closed-loop spline](/img/loop-tex.gif)  

`Scale` is a **multiplier** on the road-wide [texture density](/baking/Texturing.md#uv-density), so the default
`1.0` gives the fill exactly the same texture density as the surrounding road surface — regardless of how large the
island is. Raise it to tile the texture more finely on this fill only, and use `Shift` (world centimetres) to line the
pattern up with the road. See [Per-shape Texture group](/baking/Texturing.md#per-shape-texture-group).

```{important}
Keep the drawn "islands" in the **same actor _and_ `SubGroup`** as the main road surface (the logically related `URoadSplineComponent`s). That way [baking](/concepts/Workflow.md#bake-spline-grouping) generates the whole road section as a single seamless unit.
```

## See also

- [Road Zones and Zone Types](/concepts/RoadZones.md) — the `Driving` / `Sidewalk` zone a `LoopedRoadZone` fills with.
- [Draw Spline Tool](/create-tools/DrawSplineTool.md) — draw a closed-loop spline directly.
- [Bake: spline grouping](/concepts/Workflow.md#bake-spline-grouping) — keep islands in one actor + `SubGroup` to bake seamlessly.
