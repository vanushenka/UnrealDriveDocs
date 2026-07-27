# Polygon Profile (Pro)

A **Polygon Profile** (`URoadPolygonProfile`) is a reusable asset that stores one or more **2D closed polygon shapes**.
The [Polygon Attribute](/attributes/PolygonAttribute.md) (Pro) uses them to place custom overlays — stop lines,
arrows, hatching, and the like — on road lanes.

![A Polygon Profile with its 2D shapes](/img/polygon-profile.png)

## Properties

Each profile holds an array of **Polygon** entries. Every entry defines:

| Property | Description |
|----------|-------------|
| `Curve` | A 2D Hermite spline (`FInterpCurveVector2D`) defining the closed polygon outline in local lane space |
| `RoadZone` | Road surface type applied to this polygon (determines its material and color) |
| `Texture` | UV placement of this polygon: `Angle` (deg), `Scale` (multiplier on the road-wide [UV density](/baking/BakeStaticMesh.md#uv-density)) and `Shift` (world cm) — see [Per-shape Texture group](/baking/BakeStaticMesh.md#per-shape-texture-group) |
| `MaxSquareDistanceFromSpline` | Curve-to-polyline simplification tolerance |

Create one from the Content Browser (**right-click → Meta Road → Polygon Profile**); **double-click** it to open the
Polygon Profile editor.

## The Polygon Profile editor

A dedicated **2D canvas** for drawing and shaping the polygons.

![Drawing polygons in the Polygon Profile 2D canvas](/img/polygon-editor.png)

- **Canvas viewport** — the 2D editing surface. All polygons in the profile are shown together; the active polygon is
  highlighted while the others are dimmed.
- **Details panel** — properties of the profile and its polygon entries (the table above).

Canvas controls:

- **LMB drag** — move a polygon point, or its tangent handle (for Hermite/curved segments).
- **RMB** — context menu to **add or delete** polygons and individual points.
- **Scroll** — zoom in / out.
- **MMB / RMB drag** — pan the canvas.

## How it's used

- Referenced by the `Profile` of a [Polygon Attribute](/attributes/PolygonAttribute.md) key — one shape can be reused
  across many lanes.
- Can be **[dragged from the Content Browser onto a road lane](/profiles/Profiles.md#drag-and-drop)** to add a polygon
  key at the point nearest the cursor.

## See also

- [Profiles](/profiles/Profiles.md) — all Meta Road profile assets.
- [Polygon Attribute](/attributes/PolygonAttribute.md) — places a Polygon Profile shape on a lane.
