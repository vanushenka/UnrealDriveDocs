# Build Preset

A **Build Preset** is a reusable **Road Build Preset** asset (`URoadBuildPreset`) in the Content Browser. It stores a
complete snapshot of a road's **mesh-build settings** — the same `UMetaRoadBuildSettings` a road actor carries
(triangulation parameters plus one property set per mesh layer: surface, decals, sidewalks, curbs, marks, spline
meshes, …) — together with a **Display Name** and **Description**. You apply it to roads from
[Preset Mode](/editing/PresetMode.md).

![The Road Build Preset asset editor with its Settings, Display Name, and Description](/img/edit-preset.png)

```{note}
A Build Preset bundles **how a road bakes**. It is *not* one of the content [Profiles](/profiles/Profiles.md)
(`Road` / `Curb` / `Mark` / `Attribute` / `Polygon`), which describe road **content**. No Build Preset ships with the
plugin — you create your own.
```

| Field | Meaning |
|-------|---------|
| **Settings** | The embedded build settings (triangulation + per-layer property sets) — the payload applied to a road |
| **Display Name** | User-facing name shown in the Preset combo |
| **Description** | Free-text notes about the preset |

## Creating a Build Preset

Right-click in the Content Browser → **Meta Road → Road Build Preset**. The asset is created with the default property
sets and the blue **Meta Road** asset color; double-click it to fill in the settings, name, and description.

<!-- TODO 📷 screenshot: creating a Road Build Preset from the Content Browser "Meta Road" menu -->

You can also **capture a preset from a road** you have already set up — from the
[Preset panel](/editing/PresetMode.md#the-preset-panel), choose **Save As New** (a new asset) or **Save to Selected**
(overwrite an existing preset). Both capture the **primary (first) selected** actor's build settings.

![The Preset combo's Manage section — Save As New and Save to Selected](/img/preset-combo.png)

## Editing and updating

- **Edit the asset** — double-click it to change its **Settings**, **Display Name**, and **Description** in the standard
  asset editor.
- **Update from a road** — from the [Preset panel](/editing/PresetMode.md#the-preset-panel), select the preset, adjust
  the build settings, and **Save to Selected**.

Saving or updating a preset changes the **asset**, not any road actor — save it (**Ctrl+S** / **Save All**) to keep the
change.

## See also

- [Preset Mode](/editing/PresetMode.md) — apply and stage build settings on road actors with a live preview.
- [Baking](/baking/BakeStaticMesh.md) — the build settings a preset carries are what the bake reads.
