# Lofting Attribute (Pro)

```{note}
Inherited from **[Generate Attributes](/attributes/GenerateAttributes.md)** — shares its anchor, alignment, and per-key
transform channels.
```

**Lofting** sweeps one or more **2D cross-section profiles** along the lane to build a continuous surface — the tool for
**bridges, tunnels, retaining walls, and multilevel interchange decks**. Unlike the other
[Generate Attributes](/attributes/GenerateAttributes.md) (which repeat a mesh/component), lofting extrudes a shape, so the
result is a single watertight run that follows the road's curvature, width, and the per-key transform channels
(`Scale`, `Offset`, `Roll`, width overrides, …).

```{image} /img/lofting-concept.svg
:align: center
:width: 470px
:alt: A Lofting attribute sweeps a 2D cross-section (in the road's R–H plane) along the lane to build one continuous surface
```

*You draw a 2D cross-section in the road's **R–H** plane; the attribute sweeps it along the lane (**S**) — following the
road's curve and width — into one continuous surface.*

Add it and place keys with [Attribute Mode](/editing/AttributeMode.md). A Lofting profile is a **Blueprint subclass** of
the `Lofting` descriptor; create several subclasses for different shapes, and add **multiple lofting attributes to the
same lane** to build independent lofted meshes (e.g. a deck plus its parapets).

![A lofted surface generated along a road](/img/lofting-live.gif)

## Size control

How large the lofted mesh is across its cross-section depends on each item's **Coordinate System**:

- **Relative (Normalized)** *(default)* — you draw the cross-section curve in a normalized **−1 … +1** box, and at bake
  MetaRoad stretches it onto the lane, so the loft **adapts to the road**: X spans the lane width and Y scales with it.
  Widen the road and the loft grows with it, keeping its proportions.
- **Absolute (cm)** — the curve's X and Y are taken as literal **centimeters** (X = offset from the reference line,
  Y = height above the surface), so the loft keeps a **fixed** real-world size regardless of lane width.

**Width**: 
- In **Relative** mode the horizontal extent of the cross-section is mapped across the lane, using the **same
width machinery as every [Generate Attribute](/attributes/GenerateAttributes.md#how-a-generate-attribute-follows-the-lane)**: the
curve's **X = −1** lands on the lane's **left** edge and **X = +1** on its **right** edge, so the loft is exactly as wide
as the lane at each point (and follows the lane's width changes along the road). **Alignment** positions the `X = 0`
anchor (`Auto` = lane center; `Fixed` = by `Alpha`, 0 = inner edge … 1 = outer), and on the **center lane** you can
decouple the extents with `Override Left/Right Width` + `Left/Right Width` (cm). 
- In **Absolute** mode, width is simply
the curve's X range in centimeters from the reference line (alignment and width overrides ignored).

**Height**: 
- In **Relative** mode the vertical extent scales with the road too: by default **`Y = 1.0` equals half the
lane width**, so the loft keeps its aspect ratio as the road widens or narrows. To give it a **fixed** height instead,
enable `bOverrideHeight`. 
- In **Absolute** mode, `Y` is the height in centimeters above the surface directly.

| Field | Default | Description |
|-------|---------|-------------|
| `bOverrideHeight` | off | Fix the lofted height instead of scaling it with the lane width |
| `OverrideHeight` | 500 cm | With `bOverrideHeight` on, the world height that the profile's `Y = 1.0` maps to (blended between keys) |

![The lofted cross-section mapped onto the lane's width and height](/img/lofting-size-control.png)

## Create new Attribute

Create a new attribute from the **Content Browser** under the **Meta Road** category:

![Creating a new attribute from the Content Browser Meta Road category](/img/create-new-attribute.png)

In the **Pick Parent Class** dialog choose **`RoadLaneAttributeLoftingDescriptor`**:

![Choosing RoadLaneAttributeLoftingDescriptor as the parent class](/img/lofting-create.png)

## Lofting Attribute editor

**Double-click** a Lofting profile to open its dedicated **2D cross-section canvas** — you draw the profile once and it
is extruded along the road.

![The Lofting 2D cross-section editor](/img/lofting-editor.png)

- **Canvas viewport** — the 2D cross-section, drawn in the road's R (horizontal) / H (vertical) plane. All cross-section
  **items** are shown together; the active item is highlighted.
- **Details panel** — the descriptor: its value template and the list of cross-section **items**.
- **Selected Item panel** — the properties of the item you are currently editing.

Canvas controls: **LMB drag** moves a point or its tangent handle; **RMB** opens a context menu to add/delete points and
items; **Scroll** zooms; **MMB / RMB drag** pans.

### Cross-section items

The profile is built from one or more **cross-section items** — each is a 2D curve plus a material. An **open** curve
becomes an extruded shell (a deck, wall, or barrier); a **closed** curve becomes a tube (a rail or pipe). Add several
items, each with its own material, to build a compound profile — for example a deck, its parapets, and a curb in a single
Lofting attribute.

| Item property | Default | Description |
|---------------|---------|-------------|
| `Curve` | — | The 2D cross-section shape (a 2D spline). **Open** curve → an extruded shell; **closed** curve → a tube |
| `CoordinateSystem` | Relative | `Relative (Normalized)` — X/Y in −1…1, mapped onto the lane (see [Size control](#size-control)). `Absolute (cm)` — X/Y are centimeters from the reference line / surface |
| `Material` | — | Material applied to this item's mesh strip |
| `ChordTolerance` | 2 | Curve → polyline tolerance [cm]; smaller = smoother |
| `UVScale` | (1, 1) | UV tiling — X across the cross-section perimeter, Y along the road path |
| `bFlipNormals` | off | Reverse triangle winding (flip faces inward) |
| `bGenerateCaps` | on | For closed curves only — triangulate end caps at each lofted segment |

## Drag and Drop

Drag a Lofting attribute profile from the Content Browser onto a road lane to add it directly:

![Dragging a Lofting attribute profile onto a road lane](/img/grag-and-drop-loft.gif)

## Examples

MetaRoad ships ready-made Lofting profiles in **`/MetaRoad/MetaRoad/Profiles/Lofting`**. Apply one directly, or open it
in the [editor](#lofting-attribute-editor) to see how its cross-section is assembled and use it as a starting point:

- **`TunnelSample1`** — a tunnel.
- **`BridgeSample1`**, **`BridgeSample2`** — bridge decks.

![The bundled Lofting sample profiles — a tunnel and two bridge decks](/img/lofting-samples.svg.png)

## See also

- [Generate Attributes](/attributes/GenerateAttributes.md) — the base family Lofting belongs to (shared anchor / alignment /
  per-key transform channels).
- [Attribute Profile](/profiles/AttributeProfile.md) — how attribute assets are created in the Content Browser.
- [Attribute Mode](/editing/AttributeMode.md) — add the attribute and place keys along a lane.
