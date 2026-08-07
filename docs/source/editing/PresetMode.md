# Preset Mode

```{note}
This is the **Preset** tile in the **Edit** palette of the Meta Road editor mode
(see [The Meta Road Editor Mode](/editor-mode/MetaRoadEditorMode.md)). Active when one or more road actors are
selected.
```

![Preset sub-mode active in the Meta Road palette](/img/preset-mode.png)

**Preset Mode** lets you tune the **mesh-build settings** of the selected road(s) and preview the result before
committing. Build settings control how a road is baked — which mesh layers are generated (surface, decals, sidewalks,
curbs, marks, spline meshes), their materials, [triangulation parameters](/baking/Triangulation.md), and so on. They
are stored per actor as `UMetaRoadBuildSettings`.

```{note}
**Presets vs Profiles.** *Presets* here are saved bundles of **build settings** managed by this panel. They are not
the same thing as the reusable **[Profiles](/profiles/Profiles.md)** assets (road/curb/mark/attribute/polygon shapes)
in the Content Browser.
```

## The working-copy model

Everything you do in the Preset panel edits a **transient working copy** of the selected actors' build settings — shown
live when the view toggle is set to **Preview**. The actor's **committed** settings are never touched until you
explicitly hit **Apply**. So you can pick presets, tweak values, and compare freely; only Apply writes changes
back to the actors, and **baking always uses each actor's committed settings** (see [Baking](/baking/BakeStaticMesh.md)).

![The Preset panel with the build-settings working copy](/img/preset-mode2.png)

## The Preset panel

The panel has two parts:

- **Preset combo** (star icon) — its **Apply Preset** section lists every [Build Preset](/profiles/BuildPreset.md) in the
  project; picking one copies its settings onto the working copy (the Preview updates immediately). Its **Manage**
  section (**Save As New** / **Save to Selected**) creates or updates a [Build Preset](/profiles/BuildPreset.md) from the
  current settings.
- **Build settings** — a details view of the working copy: the
  [triangulation parameters](/baking/Triangulation.md) plus one property set per mesh layer (surface, decals,
  sidewalks, curbs, marks, spline meshes, …). Editing here updates the Preview; with several actors selected the
  values are multi-edited across them.

![Adjusting build settings with the live Preview updating](/img/preset-live.gif)

## Committing — the Apply bar

While the Preset tile is active, an **Apply bar** sits at the bottom of the viewport — the same place a drawing tool
shows its Accept/Cancel buttons:

**Apply** writes the working settings into the selected road actors (**commit**). It is the only action
that changes an actor, and it is separate from saving a preset asset. The button is greyed out when there is nothing
to commit (no road actor selected). Leaving the Preset tile without applying simply discards the working copy.

![The Apply bar at the bottom of the viewport while Preset mode is active](/img/preset-apply-bar.png)

```{note}
In earlier versions this button sat at the bottom of the Preset panel itself. It moved to the viewport so that
committing a Preset session looks and behaves like accepting a tool.
```

## Workflow

1. Select one or more **road actors**.
2. Open the **Preset** tile and switch the view toggle to **Preview**.
3. **Pick a preset** from the combo and/or **adjust the build settings** in the panel — the Preview updates live on the
   working copy.
4. *(Optional)* save the settings as a reusable **[Build Preset](/profiles/BuildPreset.md)** (combo → **Save As New** /
   **Save to Selected**).
5. **Apply** (the bar at the bottom of the viewport) to commit the settings onto the actors, then bake
   when ready — the bake uses the committed settings.

## See also

- [Build Preset](/profiles/BuildPreset.md) — the reusable build-settings asset you apply and save here.
- [Triangulation](/baking/Triangulation.md) — what the settings in this panel actually do.
- [Baking](/baking/BakeStaticMesh.md) — where each actor's committed build settings are used.
