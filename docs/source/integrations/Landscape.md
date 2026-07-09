# Landscape (Pro)
The `URoadSplineComponent` has similar properties to Unreal Engine [Landscape Splines](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-splines-in-unreal-engine): they deform and paint the Landscape underneath it. 

## Setup
To use this feature, you first need to add a **RoadSplines** layer to Landscape:  
![Adding the RoadSplines edit layer to the Landscape](/img/landscape-add-layer.png)  

After that, for each `URoadSplineComponent` for which you want to use the Landscape features, you need to select the corresponding Landscape:  
![Selecting the target Landscape on a road spline component](/img/landscape-set.png)  

That's all, the landscape should update automatically whenever the `URoadSplineComponent` changes:  
![The Landscape deforming automatically as the road spline is edited](/img/landscape.gif)  

The landscape support feature is experimental, and if for some reason the landscape under the `URoadSplineComponent` hasn't updated, you can do it manually. To do this, in the context menu of the **RoadSpline layers**, you must select the **Update Splines** item:
![The Update Splines item in the RoadSplines layer context menu](/img/landscape-update.png)  

## Paint
`URoadSplineComponent` supports [Landscape Paint Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine).  
In the example below, two paint layers (A and B) have already been created:  
![Two Landscape paint layers A and B set up in Paint Mode](/img/landscape-paint2.png)  

Now you just need to specify the **Landscape Layer Name** of the drawing layer, and the landscape under the `URoadSplineComponent` will be painted automatically:  
![The Landscape painted automatically beneath the road spline](/img/landscape-paint.png)  

## See also

- [Baking](/baking/BakeStaticMesh.md) — generate the road meshes that sit on the deformed Landscape.
- [Zone Graph](/integrations/ZoneGraph.md) — another Pro integration driven from road lane data.

