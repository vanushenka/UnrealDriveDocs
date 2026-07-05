# Curb Profile

A **Curb Profile** defines the **curb cross-section** (material and geometry) for **sidewalk** lanes
(`RoadLaneSidewalk`). You set the curb material and shape once as an asset, then reference it from a road's build
settings; the curb is generated during [baking](/baking/BakeStaticMesh.md).

![A Curb Profile](/img/set-curb-profile.png)

Create one from the Content Browser (**right-click → Meta Road → Curb Profile**) and edit it in the standard **Details**
panel — it has no dedicated editor.


Тут надо рассказать о параметрах URoadCurbProfile, особенно про CurbCurve

![A Curb Profile](/img/curb-profile-props.png)

## See also

- [Profiles](/profiles/Profiles.md) — all Meta Road profile assets.
- [Road Zones and Zone Types](/concepts/RoadZones.md) — sidewalk lanes reference a Curb Profile.
- [Baking](/baking/BakeStaticMesh.md) — where the curb is generated.
