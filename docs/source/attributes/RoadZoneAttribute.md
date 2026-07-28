# Road Zone Attribute

Changes the **surface a lane is made of** over a stretch of its length, without splitting the road into more
[lane sections](/concepts/RoadModel.md#lane-sections). Use it for a patch of a different asphalt, a painted or
paved stretch inside an ordinary driving lane, or a length that needs its own texture density.

Each key replaces the lane's [Road Zone](/concepts/RoadZones.md#road-zones-per-surface) from the key's position up to the
**next key** (or to the end of the lane). Keys are **stepped** — a surface type does not blend.

```
lane (Driving)
 S: 0 ───────────── 300 ───────────── 700 ───────────── 1000
       lane zone        key #1            key #2
```

## What it can and cannot change

The attribute overrides only the fields that every Road Zone has:

| Property | Description |
|----------|-------------|
| `Zone Type` | The surface type, e.g. `Driving`, `Marking`, `Parking`. **Leave it empty to keep the lane's own type** and change only the overrides below. |
| `Override Material` | Replaces the mesh material for this stretch. |
| `Override Priority` | Material priority for this stretch. Affects the material slot only — see the note below. |
| `Override UV Density` | Texture density [UV units per cm] for this stretch. |
| `Override Decal` | Declared, but not consumed by the generator yet. |

```{important}
The **kind** of surface cannot be changed. A driving lane stays a driving lane and a sidewalk stays a sidewalk —
the sidewalk's height, curb profile and curb flags always come from the lane itself. To turn part of a lane into a
sidewalk (with curbs and a raised surface), add a new [lane section](/editing/SectionMode.md) instead.
```

The attribute can be added to any real lane. It is **not** available on the section centre line, which has no
surface of its own.

## Where the change appears

The generator inserts a real edge across the lane at every key position, so the boundary between two stretches is
a **straight line across the lane**, not a ragged line of triangle edges. Neighbouring lanes get a matching vertex
at the same position, so no crack appears along the lane border.

The change is visible in **Preview**, after **Bake**, and in **Schematic** view — there the stretch is repainted in
the colour of its `Zone Type`, so you can see the result while placing keys.

```{note}
Schematic colours come from the **Zone Type only**. A key that changes just `Override Material`,
`Override Priority` or `Override UV Density` looks the same in Schematic — switch to **Preview** to see it.
```

```{note}
These consumers read the lane's **own** Road Zone and ignore the override: ZoneGraph generation and the PCG node
`GetRoadLaneData`. `Override Priority` likewise does not change which surface wins where two roads overlap — that
is decided per lane, from the lane's own zone.
```

## Tips

- Two keys closer together than a millimetre collapse into one; give a stretch a usable length.
- To end an override and go back to the lane's surface, add a key with an empty `Zone Type` and all the
  override toggles off.
- A different `Override UV Density` on the two sides of a key cuts the texture tiling at that key. That is
  expected — see [Default UV Density](/baking/BakeStaticMesh.md#uv-density).

## See also

- [Attribute Mode](/editing/AttributeMode.md) — add and edit this attribute along a lane.
- [Attributes](/concepts/Attributes.md) — how attributes evaluate and are stored.
- [Road Zones](/concepts/RoadZones.md) — what a Road Zone is and how its material is resolved.
- [Section Mode](/editing/SectionMode.md) — the way to change the *kind* of a surface along a road.
