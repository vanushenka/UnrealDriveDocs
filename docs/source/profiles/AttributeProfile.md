# Attribute Profile

An **Attribute Profile** is the Content-Browser asset that registers a **custom lane attribute** as a Blueprint. Once
created, the new attribute type appears automatically in [Attribute Mode](/editing/AttributeMode.md) — no changes to the
core plugin.

![Creating an Attribute Profile](/img/preset-attributes.png)

## Creating one

From the Content Browser: **right-click → Meta Road → Attribute Profile**, then choose the **base class** the profile
derives from:

![Choosing the base class of a new Attribute Profile](/img/entry-type.png)

The base classes are the **[Generate Attributes](/attributes/GenerateAttributes.md)** family — each generates something along a
lane. Pick one, configure it, and see its page in **Attribute Types** for the full field reference:

- **[Generate](/attributes/GenerateAttributes.md#the-generate-base-class)** — the base class; override `GenerateAsset()` in
  Blueprint to emit any geometry (samples: `/MetaRoad/MetaRoad/Profiles/Custom`).
- **[Spline Mesh](/attributes/SplineMeshAttribute.md)** — sweep a static mesh along the lane (`SplineMeshSample`).
- **[Component Template](/attributes/ComponentTemplateAttribute.md)** — repeat a scene component (`ComponentSample`).
- **[Actor Template](/attributes/ActorTemplateAttribute.md)** — spawn an actor (`ActorSample`).
- **[Lofting](/attributes/LoftingAttribute.md)** *(Pro)* — extrude a 2D cross-section (bridges, tunnels, decks); it has
  its own [cross-section editor](/attributes/LoftingAttribute.md#lofting-attribute-editor).

## See also

- [Attributes](/concepts/Attributes.md) — what attributes are and the full type catalogue.
- [Generate Attributes](/attributes/GenerateAttributes.md) — the base-class family this profile derives from.
- [Attribute Mode](/editing/AttributeMode.md) — add and edit attributes on a lane.
