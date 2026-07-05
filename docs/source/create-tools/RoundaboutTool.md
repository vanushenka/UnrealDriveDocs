# Roundabout Tool (Pro)

```{note}
This is the **Roundabout** tile in the **Create** palette of the Meta Road editor mode
(see [The Meta Road Editor Mode](/editor-mode/MetaRoadEditorMode.md)). *(Pro feature.)*
```

![Roundabout tool active in the Create palette](/img/roundabout-mode.png)

The **Roundabout Tool** draws a closed, circular road spline (`URoadSplineComponent`) for roundabouts and ring roads
in a single drag gesture. The result is an ordinary closed road — you can edit it afterwards like any other road (add
lanes, attributes, connect approaches).

## Drawing a roundabout

1. Activate the **Roundabout** tile.
2. **Press and hold LMB** at the intended center of the roundabout.
3. **Drag** outward to set the radius — the circular preview updates live, and node 0 follows your cursor direction.
4. **Release LMB** to place the roundabout. A new `AMetaRoad` actor with the closed circular spline is created.

![Dragging out a roundabout — the circular preview updates live](/img/roundabout-live.gif)

After placing it you can keep tuning the shape from the **Details** panel (the values below update the spline live).

## Properties

| Property | Default | Description |
|----------|---------|-------------|
| `Radius` | 1000 (min 200) | Circle radius, cm; also set live while dragging |
| `NumPoints` | 4 (2–16) | Number of control points; more points = smoother circle |
| `Rotation` | 0° (−180…180) | Rotates node 0 around the center — useful to align entry points with approach roads |
| `bClockwise` | off | Spline traversal direction — off = counter-clockwise, on = clockwise |
| `DrawProfile` | `2_Lanes+Borders_Coodirect` | [Road Profile](/profiles/RoadProfile.md) applied to the spline after each rebuild |
| `LoopedRoadZone` | — | Surface zone that fills the interior island (`FRoadLayout::LoopedRoadZone`) |
| `bHitWorld` / `bHitGroundPlane` | on / on | Raycast targets: world geometry and/or the Z=0 plane |
| `ClickOffset` | 20 (0–100) | Offset above the hit surface, cm |
| `bCreateBlueprint` / `BlueprintToCreate` | off | Optionally output a Blueprint instead of a level actor |

```{note}
The control-point tangents are computed automatically so the spline forms a smooth circle for any `NumPoints`.
```

## Next steps

- Add lanes with [Section Mode](/editing/SectionMode.md) and markings with [Attributes](/concepts/Attributes.md).
- Connect approach roads with the [Intersection Tool](/create-tools/IntersectionTool.md) or manually in
  [Spline Mode](/editing/SplineMode.md).
- [Bake](/baking/BakeStaticMesh.md) to generate the mesh.
