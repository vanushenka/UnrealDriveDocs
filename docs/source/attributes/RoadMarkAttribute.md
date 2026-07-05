# Road Mark Attribute

Adds a **Mark** attribute to a road lane; it is used during [baking](/baking/BakeStaticMesh.md) to generate road
markings. Each **Attribute Key** is assigned a road-marking type via `Profile`, or you can create a new type on the spot
(`Profile Source → Use Custom`). To remove markings for a stretch of the lane, set `Profile` to `empty`.

![Assigning a road-marking profile to an Attribute Key](/img/mark.png)

## Properties

| Property | Description |
|----------|-------------|
| `Profile` | The [Mark Profile](/profiles/MarkProfile.md) asset defining the marking (type, size, color). Set to `empty` to clear markings for that stretch. |
| `Profile Source` | Reference a Mark Profile asset, or define a marking inline on the key (`Use Custom`). |

## Drag and Drop

Drag a Mark Profile from the Content Browser onto a lane to set its Road Mark attribute:

![Dragging a Mark Profile onto a road lane](/img/grag-and-drop-makrs.gif)

## See also

- [Attribute Mode](/editing/AttributeMode.md) — add and edit this attribute along a lane.
- [Attributes](/concepts/Attributes.md) — how attributes evaluate and are stored.
- [Mark Profile](/profiles/MarkProfile.md) — reusable road-marking profiles.
