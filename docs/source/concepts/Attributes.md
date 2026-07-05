# Attributes

**Attributes are the most powerful idea in MetaRoad.** One uniform mechanism lets a plain lane carry *any* data or
generate *any* geometry along its length: the same lane can become a marked highway, a guardrail run, a lofted bridge, a
landscape-shaping cut, or a carrier of your own custom data. Everything is a **typed curve of keys sampled along the
lane by arc-length (`SOffset`)**, and new attribute types plug in with **no changes to the core plugin**.

```{image} /img/attribute-tracks.svg
:align: center
:width: 560px
:alt: One lane carrying several attributes, each a track of keys along the SOffset axis
```

*One lane can carry many attributes at once — each is an independent track of **keys** placed along the lane's `SOffset`
(arc-length) axis, and the first key of each sits at `S = 0`.*

You place and edit attributes in the editor with the [Attribute sub-mode](/editing/AttributeMode.md).

## What attributes let you do

Each capability below is produced by a built-in attribute type — at bake time, or live for Landscape:

- **Paint lane markings** — the [Road Mark](/attributes/RoadMarkAttribute.md) attribute generates center lines, edge
  lines, dashes, and custom strips.
- **Line the road with meshes and props** — [Spline Mesh](/attributes/SplineMeshAttribute.md) sweeps a mesh (guardrails,
  barriers, kerbs) while [Component](/attributes/ComponentTemplateAttribute.md) and
  [Actor](/attributes/ActorTemplateAttribute.md) templates repeat props (lamp posts, cones, power lines) along the lane.
- **Build bridges, tunnels and walls** — [Lofting](/attributes/LoftingAttribute.md) *(Pro)* extrudes a 2D cross-section
  into a continuous surface that follows the road.
- **Shape sidewalks and drop kerbs** — [Sidewalk Height](/attributes/SidewalkHeightAttribute.md) ramps the walkway and
  [Curb Cut](/attributes/CurbCutAttribute.md) *(Pro)* lowers the curb at crossings and driveways.
- **Drop surface overlays** — the [Polygon](/attributes/PolygonAttribute.md) *(Pro)* attribute places stop lines,
  arrows, and hatching.
- **Shape the terrain** — the [Landscape](/attributes/LandscapeAttribute.md) *(Pro)* attribute deforms the Unreal
  landscape along the road.
- **Carry your own data** — [Speed](/attributes/SpeedAttribute.md) (and any custom struct) stores values along the lane
  that you can read at runtime to drive your own systems.

## How an attribute works

- An attribute is attached to a **lane** (or the section center-line). It has a unique **type** (e.g. `Speed`, `Mark`,
  `Fence`) and holds a sorted list of **keys**.
- Each **Attribute Key** pairs an `SOffset` (arc-length position along the lane; `0` = the lane's start) with
  **Attribute Data** — an arbitrary C++ or Blueprint structure (a speed value, a mark profile, a cross-section, …). The
  first key is fixed at `SOffset = 0`.
- **Evaluation** is either **stepped** or **interpolated**, depending on the value type:

```{image} /img/attribute-stepped-interpolated.svg
:align: center
:width: 520px
:alt: Stepped versus interpolated attribute evaluation
```

*Stepped attributes hold the last key's value until the next key (speed limits, road marks); interpolated attributes
blend smoothly between keys (landscape height, curve transforms).*

- Attributes are stored per lane and per section center-line, keyed by attribute type, so one lane can carry many
  different attributes at once.

For example, the `Speed` attribute below is set on a single lane (ID `+1` in section `1`) with three keys at `SOffset`
0 cm, 400 cm and 800 cm. Each key's **Attribute Data** is a single float, giving 20, 60 and 100 km/h along the lane:

![alt text](/img/lane-attr.png "Speed attribute with three keys")

## Data or geometry

An attribute produces one of two things along the lane:

- **Data** — a value sampled at every position (Speed, or your own struct). Nothing is generated; you *read* it — at
  bake, at runtime, or from your own code.
- **Geometry** — meshes, props, or surfaces laid along the lane. The [Generate Attributes](/attributes/GenerateAttributes.md)
  family and Lofting position an **anchor** on the road surface and lay geometry along it with a per-key transform
  (scale, offset, roll, width). See [Generate Attributes](/attributes/GenerateAttributes.md) for the anchor/alignment model.

## Types of attributes

Every attribute type that ships with MetaRoad:

- **[Speed](/attributes/SpeedAttribute.md)** — per-lane speed-limit metadata.
- **[Road Mark](/attributes/RoadMarkAttribute.md)** — lane markings generated at bake time.
- **[Curb Cut](/attributes/CurbCutAttribute.md)** *(Pro)* — dropped kerbs on sidewalks.
- **[Landscape](/attributes/LandscapeAttribute.md)** *(Pro)* — deform the Unreal landscape along the road.
- **[Sidewalk Height](/attributes/SidewalkHeightAttribute.md)** — vary sidewalk vertex height for ramps and slopes.
- **[Polygon](/attributes/PolygonAttribute.md)** *(Pro)* — custom 2D overlays: stop lines, arrows, hatching.
- **[Generate Attributes](/attributes/GenerateAttributes.md)** — generate geometry along a lane (guardrails, barriers, fences,
  lamp posts, power lines, bridges). A family of related types:
  - **[Generate (base)](/attributes/GenerateAttributes.md#the-generate-base-class)** — the base class; subclass it in Blueprint to
    build your own generator.
  - **[Spline Mesh](/attributes/SplineMeshAttribute.md)** — sweep a static mesh into a spline mesh along the lane.
  - **[Component Template](/attributes/ComponentTemplateAttribute.md)** — repeat a scene component along the lane.
  - **[Actor Template](/attributes/ActorTemplateAttribute.md)** — spawn an actor repeatedly along the lane.
  - **[Lofting](/attributes/LoftingAttribute.md)** *(Pro)* — extrude 2D cross-sections into a continuous surface
    (bridges, tunnels, decks).

## Extending attributes

Attributes are built to be extended — a new type **appears automatically** in the Attribute tree and the build pipeline,
with no edits to the core plugin (MetaRoad auto-discovers every attribute descriptor, native **and** Blueprint):

- **Attribute Profile assets** register and pre-configure a type — see
  [Attribute Profile](/profiles/AttributeProfile.md).
- **Blueprint** — subclass **[Generate](/attributes/GenerateAttributes.md#the-generate-base-class)** and override
  `GenerateAsset()` to emit any geometry along a lane (no C++ needed); the mesh pipeline builds it automatically.
- **C++** — subclass `FRoadLaneAttributeValue` + `URoadLaneAttributeDescriptor` for a brand-new data type with its own
  evaluation and editor drawing. *(To be documented in the upcoming C++ API section.)*

## Editing attributes

Add, pin, and key attributes on a lane in [Attribute Mode](/editing/AttributeMode.md) — a searchable tree of every type,
with a pin column that adds or removes a type on the selected lane(s):

![The attribute tree in Attribute Mode](/img/attribute-tree.png)

## See also

- [Attribute Mode](/editing/AttributeMode.md) — add and edit attributes in the editor.
- [The Road Model](/concepts/RoadModel.md#road-lanes) — how lanes (which carry attributes) fit into a road.
