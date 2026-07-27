# Road Zones and Zone Types

Every road surface in MetaRoad is built from **zones**. There are two levels:

- a **Zone Type** — a *named surface category* (Driving, Sidewalk, Tram, Marking, …) defined **once for the whole
  project**;
- a **Road Zone** — an *instance* that assigns a Zone Type to a **specific surface** (a lane, or a closed-loop fill),
  with optional per-surface overrides.

## Zone Types (project-wide)

A **Zone Type** defines what a surface *is* and how it looks when baked. Zone Types are registered project-wide in
**Project Settings → Plugins → Meta Road → Road Zone Types** (`UMetaRoadSettings::RoadZoneTypes` — a map of name →
details).

MetaRoad ships a built-in set — **Driving, Sidewalk, Shoulder, Border, Stop, Median, Parking, Biking, Restricted,
Marking, Tram, Rail, Bus** — and you can add your own.

![The built-in Road Zone Types listed in Project Settings](/img/zone-types.png)

Each Zone Type stores:

| Property | Meaning |
|----------|---------|
| **Mesh Material** | Default material applied to this surface when [baking](/baking/BakeStaticMesh.md) |
| **Decal Material** | Default decal material — leave empty and no decal is built for this type |
| **Material Priority** | Where surfaces overlap, the triangle takes the material with the **highest** priority |
| **Is Decal** | The zone is a flat overlay projected onto the road surface (adds no height) — for asphalt markings such as arrows and stop lines. *(Unrelated to Unreal's `UDecalComponent`.)* |
| **Editor Color** / **Editor Material** | Color and preview material used only in the editor (Schematic view) |
| **Description** | Free-text note |
| **Override UV Density** / **UV Density** | Give this zone type its own texture density instead of the road-wide [Default UV Density](/baking/BakeStaticMesh.md#uv-density) — e.g. finer paving on sidewalks than on asphalt. Absolute (UV per cm), it *replaces* the default rather than scaling it |

![Zone types shown on a road](/img/lane-types.png)

## Road Zones (per surface)

A **Road Zone** is a Zone Type *in use* on a concrete surface. It references a **Zone Type** and may **override** that
type's defaults for this one surface:

| Property | Meaning |
|----------|---------|
| **Zone Type** | Which Zone Type this surface uses |
| **Override Material** | Use a custom material instead of the Zone Type's default |
| **Override Decal** | Use a custom decal material instead of the default |
| **Override Priority** | Use a custom material priority instead of the default |
| **Override UV Density** | Use a custom texture density for this one surface. Wins over the Zone Type's UV Density, which in turn wins over the road-wide Default UV Density |

### Driving and Sidewalk zones

A Road Zone comes in two kinds, matching the two surface families. Both bake all of their zones into a **single mesh**
(with per-zone material IDs).

**Driving** (`FRoadZoneDriving`) — a drivable surface: a normal lane, shoulder, bike, bus, or tram lane. It adds one
option on top of the shared Road Zone fields:

| Property | Meaning |
|----------|---------|
| **Invert UV0** | Flip the U texture coordinate of this lane's surface |

**Sidewalk** (`FRoadZoneSidewalk`) — a pedestrian surface with **curb generation**. Besides the shared Road Zone fields
it adds:

| Property | Meaning |
|----------|---------|
| **Default Height** | Sidewalk height (cm); can be varied along the lane by the [Sidewalk Height attribute](/attributes/SidewalkHeightAttribute.md) |
| **Inside Curb** / **Outside Curb** | Build the curb on the inner / outer edge of the sidewalk |
| **Begin Curb** / **End Curb** (+ cap curves) | Build a cap curb at the start / end of the sidewalk, shaped by a curve |
| **Curb Profile** | The [Curb Profile](/profiles/CurbProfile.md) asset defining the curb's cross-section |
| **Override Curb Material** | Use a custom curb material instead of the profile's default |

## Where Road Zones are used

- **Per lane** — every road lane carries a Road Zone, edited in its **Selection** panel in
  [Section Mode](/editing/SectionMode.md) (the *Road Zone* / *Zone Type* rows).
- **Closed-loop fill** — a closed spline fills its outline with a Road Zone via **`LoopedRoadZone`** — used for refuge
  islands, pedestrian crossings, and arrow markings. See
  [Closed Loop Spline](/concepts/ClosedLoopSpline.md).

## How the material is resolved

When baking, a surface's material is chosen in this order:

1. the **Zone Type**'s default *Mesh Material*;
2. overridden by the **Road Zone**'s *Override Material*, if set;
3. where surfaces overlap, the one with the higher **Material Priority** wins.

See [Baking → Mesh Lane Materials](/baking/BakeStaticMesh.md#mesh-lane-materials) for the baking side.

## See also

- [The Road Model](/concepts/RoadModel.md#road-lanes) — how lanes (which carry Road Zones) fit into a road.
- [Closed-Loop Splines](/concepts/ClosedLoopSpline.md) — closed-loop fills that use a `LoopedRoadZone`.
- [Baking](/baking/BakeStaticMesh.md) — how zones are baked into meshes and materials.
