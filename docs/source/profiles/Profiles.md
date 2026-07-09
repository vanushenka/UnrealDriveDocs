# Profiles

**Profiles** are reusable MetaRoad **assets** — you create them in the **Content Browser** under the **Meta Road**
category and reference them from roads, attributes, and tools. Create one from the right-click **Add → Meta Road** menu:

![Creating a Meta Road profile from the Content Browser Add menu](/img/create-preset.png)

A set of default profiles ships at **/MetaRoad/DefaultPreset**; keep it unchanged for backward compatibility:

![The default profiles at /MetaRoad/DefaultPreset](/img/default-preset.png)

## Profile types

| Profile asset | Defines |
|---------------|---------|
| [Road Profile](/profiles/RoadProfile.md) | The lane layout a new road starts with |
| [Curb Profile](/profiles/CurbProfile.md) | Curb material + geometry for sidewalk lanes |
| [Mark Profile](/profiles/MarkProfile.md) | A road-marking strip (type, size, color) |
| [Attribute Profile](/profiles/AttributeProfile.md) | A custom lane-attribute type (Generate / Spline Mesh / Component / Actor / Lofting) |
| [Polygon Profile](/profiles/PolygonProfile.md) (Pro) | Reusable 2D polygon shapes for lane overlays |

Most profiles open a **dedicated editor** when you double-click them — described on each profile's page. Many can also be
applied to a road lane by **[dragging them from the Content Browser onto the road](#drag-and-drop)**.

Not a content profile, but a related Meta Road asset: the **[Build Preset](/profiles/BuildPreset.md)** — a saved bundle
of a road's *build settings* (see [Preset Mode](/editing/PresetMode.md)).

## Drag and drop

You can apply many profile assets to a road **directly from the Content Browser** — drag the asset into the viewport and
drop it onto a road. Instead of spawning a new actor (the usual Unreal behavior), MetaRoad adds the corresponding
attribute to the **currently selected road lane**:

| Dragged asset | Result on drop |
|---------------|----------------|
| **Mark Profile** (`URoadMarkProfile`) | Sets the lane's [Road Mark](/attributes/RoadMarkAttribute.md) attribute (**replaces** the existing one) |
| **Polygon Profile** (`URoadPolygonProfile`) (Pro) | Adds a [Polygon](/attributes/PolygonAttribute.md) attribute **key** at the point nearest the cursor |
| **Attribute Profile** (any `URoadLaneAttributeDescriptor` blueprint) | Adds that [attribute](/concepts/Attributes.md) to the lane |

```{note}
Select the target road (and be in a lane-editing context) before dropping. Any **other** asset dropped on the level
behaves normally — this special handling only applies to MetaRoad profile/attribute assets.
```

## See also

- [Road Profile](/profiles/RoadProfile.md) — the lane layout a new road starts with.
- [Curb Profile](/profiles/CurbProfile.md) — curb cross-section for sidewalk lanes.
- [Mark Profile](/profiles/MarkProfile.md) — a road-marking strip.
- [Attribute Profile](/profiles/AttributeProfile.md) — register a custom lane-attribute type.
- [Polygon Profile](/profiles/PolygonProfile.md) (Pro) — reusable 2D polygon shapes for lane overlays.
- [Build Preset](/profiles/BuildPreset.md) — a saved bundle of a road's build settings.
- [Attributes](/concepts/Attributes.md) — how lane attributes work.
