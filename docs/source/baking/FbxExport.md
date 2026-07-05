# FBX Export

```{note}
This is the **Export** tile in the **Bake** palette of the Meta Road editor mode
(see [The Meta Road Editor Mode](/editor-mode/MetaRoadEditorMode.md)).
```

**FBX Export** writes your road meshes to `.fbx` files on disk — for use in other DCC tools, engines, or pipelines. It
exports both static meshes and spline meshes of the road.

## Exporting

1. Enter the **Meta Road** mode, open the **Bake** palette, and click the **Export** tile.
2. Set the export options in the panel (below).
3. Click **Export Selected** (the selected road actors) or **Export All** (every road actor in the level).

![alt text](/img/fbx-props.png)


## Settings

| Setting | Options | Description |
|---------|---------|-------------|
| **Mesh Source** | `Generated Assets` / `From Scratch` | `Generated Assets` exports the already-[baked](/baking/BakeStaticMesh.md) meshes. `From Scratch` regenerates the meshes in memory and exports them directly — no bake needed first. |
| **File Layout** | `Per Actor` / `Combined` / `Per Component` | One file per road actor; a single combined file (roads keep their relative world layout); or one file per mesh component. |
| **Pivot** | `Actor Origin` / `World Position` | Center each export around its origin, or keep world positions. |
| **Output Directory** | path | Filesystem folder for the `.fbx` files. |
| **File Name Prefix** | text | Prefix added to each exported file name. |
| **Combined File Name** | text | File name used in `Combined` layout. |
| **Overwrite Existing** | bool | Overwrite files that already exist. |

## See also

- [Baking](/baking/BakeStaticMesh.md) — generate the in-level road meshes.
