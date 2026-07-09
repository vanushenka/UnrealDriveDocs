# Curb Profile

A **Curb Profile** (`URoadCurbProfile`) defines the **curb cross-section** — its shape, width, and material — for
**sidewalk** lanes (`RoadLaneSidewalk`). You set it once as an asset, reference it from a sidewalk lane, and the curb is
generated along the lane's edge during [baking](/baking/BakeStaticMesh.md).

![A Curb Profile asset](/img/set-curb-profile.png)

Create one from the Content Browser (**right-click → Meta Road → Curb Profile**) and edit it in the standard **Details**
panel — it has no dedicated editor.

## Properties

| Property | Default | Description |
|----------|---------|-------------|
| `CurbCurve` | — | The curb's **cross-section silhouette**, as a float curve. Its input (X) runs across the curb — `X = 0` at the **sidewalk-side back wall**, increasing toward the road up to `Width` — and its value (Y) is the **height** at that point. Needs **at least two keys**, or no curb is generated. |
| `Width` | 15 | Curb width [cm] — the lateral extent the `CurbCurve` X axis is mapped onto. |
| `DefaultMaterial` | — | Material applied to the generated curb. A sidewalk lane can override it per lane. |

The `CurbCurve` is where the curb's shape lives — edit it in the curve editor in the Details panel. It starts at
`X = 0` — the **back wall on the sidewalk side**, at full height — and moving toward the road traces the curb's flat top
and face, then **ends sharply at `Y = 0`** where it meets the road.

```{image} /img/curb-cross-section.svg
:align: center
:width: 440px
:alt: The CurbCurve maps lateral position to height. X = 0 is the sidewalk-side back wall at full height; moving toward the road the silhouette drops down the curb face and ends sharply at Y = 0.
```

![The Curb Profile properties, including the CurbCurve editor](/img/curb-profile-props.png)

## How it's used

- A **sidewalk lane** references a Curb Profile; the curb is built along that lane's edge at
  [baking](/baking/BakeStaticMesh.md).
- The profile's `DefaultMaterial` is used unless the lane **overrides the curb material** (`Override Curb Material`).

## See also

- [Profiles](/profiles/Profiles.md) — all Meta Road profile assets.
- [Road Zones and Zone Types](/concepts/RoadZones.md) — sidewalk lanes reference a Curb Profile.
- [Baking](/baking/BakeStaticMesh.md) — where the curb is generated.
