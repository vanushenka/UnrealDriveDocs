# Draw Modeling Tools
There are two Modeling Tools - **New Spline** and **Add Spline**, which allow to "draw" **URoadSplineComponent** in the usual way, as in popular 2D vector editors: 
![alt text](img/draw-spline.gif)  

To access these tools, switch **Editor** Mode to **Modeling Mode** and select the **Road** toolset:
![alt text](img/draw-spline2.png)  

These two tools are identical, differing only in the need to create a new AActor:
  - **New Spline** - creates a new AActor and adds a new **URoadSplineComponent** to it.
  - **Add Spline** - adds a new  **URoadSplineComponent** to the selected actor, which already has at least one **URoadSplineComponent**.

You can start drawing a spline with the [Lane Successor Connection](RoadModel.md#intersections-and-junctions):  
![alt text](img/draw-from-successor.gif)  

And finish with [Lane Predecessor Connection](RoadModel.md#intersections-and-junctions):  
![alt text](img/draw-to-predecessor.gif)  

## Lane Source
The **Lane Source** defines the rules for detection of road lanes profile (num and types of the road lanes) for spline drawing.  
![alt text](img/draw-spline-source.png)  

There are next options:
  - **One Lane** - Copy only one road lane from the **Lane Successor Connection**. Only valid if the spline is drawn from the **Lane Successor Connection**.
    ![alt text](img/lane-source-one-lane.gif)  
    </br>
  - **Right Side** - Copy the road lanes from the **Lane Successor Connection** to the last right lane in the source road section. Only valid if the spline is drawn from  the **Lane Successor Connection**.
    ![alt text](img/lane-source-right-side.gif)  
    </br>
  - **Both Sides** -  Copy all road lanes from the **Lane Successor Connection**. Only valid if the spline is drawn from  the **Lane Successor Connection**. 
    ![alt text](img/lane-source-both-sides.gif)  
    </br>
  - **Road Profile** - Copy road lanes from the profile. How to add a new profile - see [Road Lane Profiles](Presets.md#road-lanes-profiles)
    ![alt text](img/lane-source-road-profile.gif)  
