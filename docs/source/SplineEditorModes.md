# Spline Editing Modes
Spline Editing Modes allows to switch between **URoadSplineComponent** editing modes to edit spline properties described in [Road Model](RoadModel.md):  
![alt text](img/edit-modes2.png).  

## Base Modes

### Spline Mode
This mode allows to interact with **URoadSplineComponent** as with a regular UnrealEngine spline - create and delete nodes, edit tangents. The spline itself is pink in this mode.
According to Road Model, **Spline Mode** is the editing mode for the [Road Reference Line](RoadModel.md#road-reference-line):  
![alt text](img/spline-edit.gif)  

Additional spline editing features - the ability to assign a node type - **Arc**:  
![alt text](img/spline-arc.gif)  

You can also manage spline connections in this mode (see [Intersections and Junctions](RoadModel.md#intersections-and-junctions)):  
![alt text](img/spline-conn.gif)  

In the **Details Panel**, in the **Selection** group, you can edit the selected spline node:  
![alt text](img/spline-selection.png)  

### Section Mode
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

### Offset Mode
This mode allows to set the **Center Lane**  offset relative to the [Road Reference Line](RoadModel.md#road-reference-line) and corresponds to the [Lane Offset](RoadModel.md#lane-offset) described in [Road Model](RoadModel.md).
Editing the **Road Offset** width is similar to editing a spline - you can set any shape, add/delete nodes, and edit tangents:  
![alt text](img/offset.gif)  

In the **Details Panel**, in the **Selection** group, you can edit the selected **Offset Key**:  
![alt text](img/offset-selection.png)  

### Width Mode
This mode allows you to edit the width of the **Road Lane**.
Editing the **Road Lane** is similar to editing a spline - you can set any shape, add/delete nodes, and edit tangents:  
![alt text](img/width.gif)  

In the **Details Panel**, in the **Selection** group, you can edit the selected **Width Key**:  
![alt text](img/width-selection.png)  

## Attribute Modes
These mode allow to add various **Road Attributes** to **Road Lane**, which can be used for procedural generation or any other purposes (see the [Road Attributes](RoadModel.md#lane-attributes) section):  
![alt text](img/attributes.png)  


By default, two types of attributes are available: speed limit and road markings. 
To learn how to create new attribute types, see [Road Attribute Entries](Presets.md#road-attribute-entries).
To add a new attribute for a lane, select the appropriate mode in the **Road Editing Modes** menu, select the required **Road Lane**, and select **Create ATTRIBUTE_NAME** from the context menu. Then, add the required **Attribute Keys** from the same context menu:  
![alt text](img/attribute-add.gif)  

In the **Details Panel**, in the **Selection** group, you can edit the selected **Attribute Key**:  
![alt text](img/attribute-selection.png)  

### Road Mark Attribute
**Road Mark Attribute** is one of the [Road Attributes](RoadModel.md#lane-attributes) types that is available "out of the box" and allows you to add a **Mark** attribute to **Road Lane**, which is used in [Procedural Generation](ProcedureGenerationTool.md) to generate road markings. Each **Attribute Key** is assigned a road marking type, which can be selected in ```Profile Name```. Or you can create a new type on the spot (```Profile Name -> Use Custom```):  
![alt text](img/mark.png)  

If you need to remove markings for any of the sections on **Road Lane**, set ```Profile Name``` to ```None```:  
![alt text](img/mark-none.png)  

To add new road marking profiles, see [Lane Mark Profiles](Presets.md#lane-mark-profiles).
