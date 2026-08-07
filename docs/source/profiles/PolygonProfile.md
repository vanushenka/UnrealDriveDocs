# Polygon Profile (Pro)

A **Polygon Profile** (`URoadPolygonProfile`) is a reusable asset that stores one or more **2D closed polygon
shapes**. The [Polygon Attribute](/attributes/PolygonAttribute.md) (Pro) uses them to place custom overlays —
stop lines, arrows, hatching, and the like — on road lanes.

A polygon can also carry **holes**: inner contours cut out of it, so one shape can be a ring, a stencilled
letter, or an arrow with a cut-out.

![A Polygon Profile with its 2D shapes](/img/polygon-profile.png)

## Properties

Each profile holds an array of **Polygon** entries. Every entry defines:

| Property | Description |
|----------|-------------|
| `Curve` | A 2D Hermite spline (`FInterpCurveVector2D`) defining the closed polygon outline in local lane space |
| `Holes` | **Edited on the canvas only** — inner contours cut out of `Curve`. They are deliberately not shown in the Details panel, because restructuring them from there would renumber the canvas's shapes with no warning |
| `RoadZone` | Road surface type applied to this polygon (determines its material and color) |
| `Texture` | UV placement of this polygon: `Angle` (deg), `Scale` (multiplier on the road-wide [UV density](/baking/Texturing.md#uv-density)) and `Shift` (world cm) — see [Per-shape Texture group](/baking/Texturing.md#per-shape-texture-group) |
| `Chord Tolerance` | 2.0 cm — a curve segment is subdivided while its midpoint deviates from the chord by more than this **distance**. Lower = a smoother outline, more vertices |

```{note}
Holes carry no properties of their own, on purpose: `RoadZone`, `Texture` and `Chord Tolerance` all belong to the
polygon that owns them, so a hole can never disagree with the surface it is cut out of, and a hole is never
sampled coarser than its boundary.
```

```{note}
This `Chord Tolerance` is a **linear distance in cm**. The `Chord Tolerance` on a
[Mark](/create-tools/MarkSplineTool.md) or [Sidewalk](/create-tools/SidewalkSplineTool.md) detail spline is a
different property measured in **cm²**. Same name, different units.
```

Create one from the Content Browser (**right-click → Meta Road → Polygon Profile**); **double-click** it to open
the Polygon Profile editor.

## The Polygon Profile editor

A dedicated **2D canvas** for drawing and shaping the polygons.

![Drawing polygons in the Polygon Profile 2D canvas](/img/polygon-editor.png)

- **Canvas viewport** — the 2D editing surface. All polygons in the profile are shown together; the active
  polygon is highlighted while the others are dimmed.
- **Details panel** — properties of the profile and its polygon entries (the table above).

Canvas controls:

- **LMB drag** — move a polygon point, or its tangent handle (for Hermite/curved segments).
- **RMB** — context menu to **add or delete** polygons and individual points, and to work with holes.
- **Scroll** — zoom in / out.
- **MMB / RMB drag** — pan the canvas.

```{note}
**Changed in 3.2.0.** Polygons draw with a translucent **fill**, and a filled region is **clickable** — you no
longer have to hit the thin outline. Topmost shape wins, and a click inside a hole falls through to what is
underneath. Selecting a hole shows its owner's properties, since a hole has none of its own.
```

## Holes

Authored entirely from the canvas **context menu** — no new toolbar buttons, no new shortcuts.

![The Polygon Profile canvas showing a polygon with a hole cut out of it](/img/polygon-hole.png)

| Menu entry | Right-click on | What it does |
|------------|----------------|--------------|
| **Add Hole in Polygon {N}** | a polygon's body | Cuts a new square hole there |
| **Paste as Hole in Polygon {N}** | a polygon's body | Pastes the copied contour as a hole |
| **Make Hole of Polygon {N}** | a contour | Turns a standalone polygon into a hole of the one enclosing it |
| **Detach Hole** | a hole | Turns it back into a standalone polygon |

A hole must lie **strictly inside** its owner and must not **overlap another hole**. **Make Hole of** is offered
only where that holds — the same test the mesh build applies — so if no entry appears, the shape is not fully
inside anything. Nesting is one level deep.

```{note}
A hole that breaks the rules is **dropped with a warning and the fill is solid there** — it never fails the
build. The generation report names the reason: too few points, self-intersecting, not strictly inside, or
overlapping another hole.
```

Holes reach the mesh through the [Polygon attribute](/attributes/PolygonAttribute.md) and
[polygon stamps](/create-tools/MarkSplineTool.md) on a Mark spline; crosswalks, sidewalk splines and chevrons
cannot have them. A stamp on a road lane shows the road through its holes.

## How it's used

- Referenced by the `Profile` of a [Polygon Attribute](/attributes/PolygonAttribute.md) key — one shape can be
  reused across many lanes.
- Can be **[dragged from the Content Browser onto a road lane](/profiles/Profiles.md#drag-and-drop)** to add a
  polygon key at the point nearest the cursor.

## See also

- [Profiles](/profiles/Profiles.md) — all Meta Road profile assets.
- [Polygon Attribute](/attributes/PolygonAttribute.md) — places a Polygon Profile shape on a lane.
- [Mark Spline Tool](/create-tools/MarkSplineTool.md) *(Pro)* — stamps a Polygon Profile shape along a spline.
