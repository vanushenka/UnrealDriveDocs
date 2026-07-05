# Landscape (Pro)
The **URoadSplineComponent** has similar properties to UnrealEngine [Landscape Splines](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-splines-in-unreal-engine): it deform and paint the Landscape underneath it. 

## Setup
To use this feature, you first need to add a **RoadSplines** layer to Landscape:  
![alt text](/img/landscape-add-layer.png)  

After that, for each **URoadSplineComponent** for which you want to use the Landscape features, you need to select the corresponding Landscape:  
![alt text](/img/landscape-set.png)  

That's all, the landscape should update automatically whenever the **URoadSplineComponent** changes:  
![alt text](/img/landscape.gif)  

The landscape support feature is experimental, and if for some reason the landscape under the **URoadSplineComponent** hasn't updated, you can do it manually. To do this, in the context menu of the **RoadSpline layers**, you must select the **Update Splines** item:
![alt text](/img/landscape-update.png)  

## Paint
**URoadSplineComponent** supports [Landscape Paint Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine).  
In the example below, two paint layers (A and B) have already been created:  
![alt text](/img/landscape-paint2.png)  

Now you just need to specify **Landscape Layer Name** of the drawing layer, and the landscape under the **URoadSplineComponent** will be pint automatically:  
![alt text](/img/landscape-paint.png)  


