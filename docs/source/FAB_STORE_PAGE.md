---
orphan: true
---

<!-- Fab.com store description for MetaRoad. This is a copy-paste marketing page, not part of the docs site.
     The `orphan: true` front matter above only keeps the Sphinx build warning-free — skip those 3 lines when
     pasting into Fab. -->

# MetaRoad — Procedural Road Network & HD-Map Editor

**Draw, edit, preview, bake.** Author complete road networks inside Unreal Engine and get real, game-ready meshes plus a
logical road graph.

MetaRoad turns Unreal Engine into a procedural **road-network and HD-map editor**. You design roads interactively with
splines in a dedicated editor mode, preview the result live, and bake actual `StaticMesh` geometry — drive surface,
sidewalks, curbs, markings, guardrails, bridges and more — together with a logical lane graph for traffic and AI.

**Built for:** city digital twins · ADAS / autonomous-driving validation · games & cinematics · archviz.

## Key Features

**Interactive authoring**
- Draw roads as splines and connect them into networks — one **Meta Road** editor mode with Create / Edit / Bake tile palettes.
- **Live, non-destructive preview** — the road stays editable data until you bake; nothing is written to disk until you choose to.
- One-click tools for the common cases: **Intersections** (T / X / multi-lane), **Roundabouts**, **Crosswalks**, and **Chevron** guide-islands. *(Pro)*

**Rich road model**
- Any number of lanes with **asymmetric sections** and per-lane types: driving, sidewalk, bicycle, bus, parking, tram, shoulder, and custom.
- Per-lane **offset** and **width** curves, lane directions, and full **junction connections** (predecessor / successor, lane-to-lane).
- **Closed-loop splines** to fill areas — plazas, parking lots, intersection interiors.

**Attributes — the extension engine**
- Sample **data and geometry along any lane**: speed limits & metadata, road markings, guardrails / barriers / fences, lamp posts & props, sidewalk ramps, curb cuts, and surface polygons (arrows, stop lines, hatching).
- Generate **meshes, components, or actors** along lanes, or **loft** 2D cross-sections into bridges, tunnels, and retaining walls.
- Add **your own attribute types** in Blueprint (no C++) or C++ — they appear automatically, with no changes to the core plugin.

**Baking & export**
- Bake to `StaticMesh` + `SplineMesh` + decals with per-lane-type materials, **multi-channel UVs** (UV0 / UV1) and **vertex colors** for seamless blending at intersections.
- Configurable asset output location, per-user folders, and **automatic cleanup** of previous bakes.
- **FBX export** for any pipeline.

**Integrations**
- **ZoneGraph** AI-navigation data generation. *(Pro)*
- **Landscape deformation** — carve and paint the Unreal landscape to follow your roads. *(Pro)*
- **Real-world map tiles** (Google Maps / OSM / Bing) for georeferenced building.
- Compatible with the **City Sample** pack.

**Reusable content & API**
- Content-Browser assets: **Road / Curb / Mark / Attribute / Polygon Profiles** and **Build Presets** — plus ready-made samples.
- **C++ and Blueprint APIs** to add lane types, custom attributes, generators, and importers / exporters.

## Free vs Pro

Core road authoring and baking are **FREE**. **Pro** unlocks the advanced automated tools and integrations.

Full breakdown: https://unrealdrive.readthedocs.io/en/latest/introduction/ProVsFree.html

## Good to know

Baked content is plain `StaticMesh` assets and works **without the plugin**. MetaRoad is only required at runtime if you
use the road **graph** in-game (for example, to drive traffic).

## Documentation & Support

- 📖 Documentation: https://unrealdrive.readthedocs.io/en/latest/
- ✉️ Support: ivzhuk7@gmail.com

---

## Technical Details (Fab fields)

**Features:**
- Spline-based road-network editor with a live mesh preview
- Multi-lane model: asymmetric sections, per-lane zone types, offset/width curves, junctions, closed-loop fills
- Automated Intersection / Roundabout / Crosswalk / Chevron tools *(Pro)*
- Lane attributes: speed & metadata, markings, guardrails/props (spline-mesh/component/actor generators), lofted bridges & tunnels, landscape deformation, sidewalk ramps, curb cuts, surface polygons — extensible in Blueprint or C++
- Bake to StaticMesh/SplineMesh + decals with materials, multi-channel UVs and vertex colors; configurable output + auto-cleanup
- FBX export; ZoneGraph AI-navigation generation *(Pro)*; real-world map tiles; City Sample compatible
- Reusable profile & build-preset assets; C++ and Blueprint APIs

**Code Modules:**
- `MetaRoad` — Runtime
- `MetaRoadEditor` — Editor
- `MetaRoadPCG` — Editor (PCG integration)

**Number of C++ Classes:** ‹fill in›
**Number of Blueprints:** ‹fill in›
**Supported Engine Versions:** 5.6
**Network Replicated:** No
**Supported Development Platforms:** Windows ‹+ macOS if applicable›
**Supported Target Build Platforms:** All *(baked content is standard `StaticMesh`; the runtime graph module is optional)*
**Documentation:** https://unrealdrive.readthedocs.io/en/latest/
**Example Project / Important:** Baked meshes are plain StaticMesh assets and require no plugin at runtime.
