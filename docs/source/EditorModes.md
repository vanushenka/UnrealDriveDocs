# Editor Modes
**Editor Modes** allows to switch between **URoadSplineComponent** editing modes to edit spline properties described in [Road Model](RoadModel.md):  
![alt text](img/edit-modes2.png).  

## Spline Mode
This mode allows to interact with **URoadSplineComponent** as with a regular UnrealEngine spline - create and delete nodes, edit tangents. The spline itself is pink in this mode.
According to Road Model, **Spline Mode** is the editing mode for the [Road Reference Line](RoadModel.md#road-reference-line):  
![alt text](img/spline-edit.gif)  

Additional spline editing features - the ability to assign a node type - **Arc**:  
![alt text](img/spline-arc.gif)  

You can also manage spline connections in this mode (see [Intersections and Junctions](RoadModel.md#intersections-and-junctions)):  
![alt text](img/spline-conn.gif)  

In the **Details Panel**, in the **Selection** group, you can edit the selected spline node:  
![alt text](img/spline-selection.png)  

## Section Mode
This mode allows to edit [Road Lanes](RoadModel.md#road-lanes) and [Lane Sections](RoadModel.md#lane-sections) described in the [Road Model](RoadModel.md):  
![alt text](img/section-resize.gif)  

You can add and delete **Road Sections** via the context menu:  
![alt text](img/section-split.gif)  

You can also add and delete **Road Lanes**:  
![alt text](img/lane-add.gif)  

In the **Details Panel**, in the **Selection**  group, you can edit the selected **Road Section**:  
![alt text](img/section-selected.png)  

The **Details Panel** in the **Selection** group also allows you to edit the selected **Road Lane**:  
![alt text](img/lane-selection.png)  

## Offset Mode
This mode allows to set the **Center Lane**  offset relative to the [Road Reference Line](RoadModel.md#road-reference-line) and corresponds to the [Lane Offset](RoadModel.md#lane-offset) described in [Road Model](RoadModel.md).
Editing the **Road Offset** width is similar to editing a spline - you can set any shape, add/delete nodes, and edit tangents:  
![alt text](img/offset.gif)  

In the **Details Panel**, in the **Selection** group, you can edit the selected **Offset Key**:  
![alt text](img/offset-selection.png)  

## Width Mode
This mode allows you to edit the width of the **Road Lane**.
Editing the **Road Lane** is similar to editing a spline - you can set any shape, add/delete nodes, and edit tangents:  
![alt text](img/width.gif)  

In the **Details Panel**, in the **Selection** group, you can edit the selected **Width Key**:  
![alt text](img/width-selection.png)  
