# Road Zone Attribute

Changes the **surface a lane is made of** over a stretch of its length, without splitting the road into more
[lane sections](/concepts/RoadModel.md#lane-sections) — a patch of different asphalt, a painted stretch inside an
ordinary lane, or a length that needs its own texture density.

![A driving lane with a Road Zone key part-way along it, the stretch after the key repainted in a different surface](/img/road-zone-attribute.png)

![A driving lane with a Road Zone key part-way along it, the stretch after the key repainted in a different surface](/img/road-zone-attribute.gif)

Each key replaces the lane's [Road Zone](/concepts/RoadZones.md#road-zones-per-surface) from its own position up
to the next key. Keys are **stepped** — a surface type does not blend.


## Properties

| Property | Description |
|----------|-------------|
| `Zone Type` | The surface type — `Driving`, `Marking`, `Parking`, … **Leave it empty to keep the lane's own type** and change only the overrides below |
| `Override Material` | Replaces the mesh material for this stretch |
| `Override Priority` | Material priority for this stretch. Affects the material slot only |
| `Override UV Density` | Texture density for this stretch, in UV units per cm |

Add it to any real lane; it is not offered on the section center line, which has no surface of its own.

```{important}
The **kind** of surface cannot be changed. A driving lane stays a driving lane and a sidewalk stays a sidewalk —
height, curb profile and curb flags always come from the lane itself. To turn part of a lane into a sidewalk, add
a new [lane section](/editing/SectionMode.md) instead.
```

The boundary between two stretches is a **straight line across the lane**, and neighbouring lanes get a matching
vertex at the same position, so no crack appears along the lane border.

```{note}
**Schematic** repaints the stretch in the color of its `Zone Type`, so a key that changes only a material,
priority or UV density looks unchanged there — switch to **Preview** to see it. ZoneGraph and the PCG node
`GetRoadLaneData` also read the lane's **own** zone and ignore the override.
```

```{tip}
To end an override and return to the lane's own surface, add a key with an empty `Zone Type` and every override
toggle off.
```

## See also

- [Attribute Mode](/editing/AttributeMode.md) — add and edit this attribute along a lane.
- [Road Zones](/concepts/RoadZones.md) — what a Road Zone is and how its material is resolved.
- [Section Mode](/editing/SectionMode.md) — the way to change the *kind* of a surface along a road.
