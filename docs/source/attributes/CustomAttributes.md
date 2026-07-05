---
orphan: true
---

<!-- Parked (removed from the site nav 2026-07): the Blueprint route (subclass Generate → GenerateAsset) now lives in
     Generate Attributes → Base classes. The C++ route below is retained as seed material for the future
     reference/CPP_API.md section, where Custom Attributes will be documented. Not linked from any page. -->

# Custom Attributes

Attributes are designed to be extended. You can define your **own attribute type** — storing any data and performing
any action along a lane — and it becomes available in the [Attribute sub-mode](/editing/AttributeMode.md) automatically,
with no changes to the core plugin.

There are two routes, depending on what you need.

## 1. Generate objects along a lane (no C++)

If you want to place meshes, components, or actors along a lane, you usually don't need custom code — use a
**[Generate Attribute](/attributes/GenerateAttributes.md)**. Create an **[Attribute Profile](/profiles/AttributeProfile.md)**
asset, pick the base class (Spline Mesh / Component Template / Actor Template), and configure it. This covers most
"repeat this thing along the road" cases.

For fully custom generation logic, base your profile on **Generate** (`URoadLaneAttributeGenerateDescriptor`) and override
`GenerateAsset()` in Blueprint or C++.

## 2. Define a brand-new attribute type (C++)

To store custom data and control its evaluation and editor drawing:

1. Subclass **`FRoadLaneAttributeValue`** — define your data fields. Override `CanInterpolate()` / `Interpolate()` for
   smooth blending, and `GetKeyAlpha()` to control where the editor handle sits across the lane width.
2. Subclass **`URoadLaneAttributeDescriptor`** — the "type key" that registers your attribute and provides its editor
   name, icon, and drawing. Override `GetAttributeValueTemplate()` to return a default instance of your value struct.
3. Read it at runtime with `Lane.Attributes.Find(UMyDescriptor::StaticClass())->Evaluate<FMyValue>(SOffset)`.

Your new descriptor is discovered automatically and appears in the attribute tree of the Attribute sub-mode.

```{note}
For the C++ types, methods, and runtime querying, see the C++ API reference (under revision).
```

## See also

- [Attributes](/concepts/Attributes.md) — the attribute data model: how attributes evaluate and are stored.
- [Attribute Profile](/profiles/AttributeProfile.md) — the asset that registers a new attribute type.
