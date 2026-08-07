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
- Reshape the network as you go: **Split Spline** cuts a road spline in two at the clicked point, sections split full-width or per side, and lanes are added, deleted or reversed straight from the viewport context menu.
- One-click tools for the common cases: **Intersections** (T / X / multi-lane), **Roundabouts**, **Crosswalks**, **Mark** splines (chevron islands, stripes, box-junction and guide-island fill patterns, stamped polygons) and **Sidewalk** splines — with **magnetic snapping** that makes a detail spline follow the road's own geometry exactly, through curb cuts, crossings and junction seams. *(Pro)*

**Rich road model**
- Any number of lanes with **asymmetric sections** and per-lane types: driving, sidewalk, bicycle, bus, parking, tram, shoulder, and custom.
- Per-lane **offset** and **width** curves, lane directions, and full **junction connections** (predecessor / successor, lane-to-lane).
- **Closed-loop splines** to fill areas — plazas, parking lots, intersection interiors.

**Attributes — the extension engine**
- Sample **data and geometry along any lane**: speed limits & metadata, road markings, guardrails / barriers / fences, lamp posts & props, sidewalk ramps, curb cuts, **road zones** (switch a lane's surface type — and its material and texture density — part-way along its length), **cross-section profiles** (sink the driving surface toward its edges into a gutter that varies along the road), and surface polygons (arrows, stop lines, hatching).
- **Traffic lights** — place signal heads with the **Signal** attribute (vehicle or pedestrian, with OpenDRIVE type codes), then wire them into a **Traffic Controller** component: named phases, a per-signal Red / Red-Yellow / Green / Yellow state grid, and a looping runtime clock that plays in PIE and packaged builds.
- Generate **meshes, components, or actors** along lanes, or **loft** 2D cross-sections into bridges, tunnels, and retaining walls.
- Add **your own attribute types** in Blueprint (no C++) or C++ — they appear automatically, with no changes to the core plugin.

**Baking & export**
- Bake to `StaticMesh` + `SplineMesh` + decals with per-lane-type materials, **multi-channel UVs** (UV0 / UV1, plus a UV2 channel at a uniform real-world texture density) and **vertex colors** for seamless blending at intersections.
- **Control the mesh resolution** — fill the road surface at a target edge length, either with well-shaped triangles that handle any junction, or with rows running along the road; then drape the result onto the landscape and smooth it.
- Configurable asset output location, per-user folders, and **automatic cleanup** of previous bakes.
- **FBX export** for any pipeline.

**Integrations**
- **ZoneGraph** AI-navigation data generation. *(Pro)*
- **Landscape deformation** — carve and paint the Unreal landscape to follow your roads, or flatten the area enclosed by a closed detail spline. *(Pro)*
- **PCG integration** — a **Get Road Lane Data** node feeds lane geometry and attributes into Procedural Content Generation graphs. *(Pro)*
- **Real-world map tiles** (Google Maps / OSM / Bing) for georeferenced building.
- Compatible with the **City Sample** pack.

**Reusable content & API**
- Content-Browser assets: **Road / Curb / Mark / Attribute Profiles**, **Polygon Profiles** *(Pro, with inner contours / holes)* and **Build Presets** — plus ready-made samples (the arrow and lofting profile libraries ship with Pro only).
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
- Spline-based road-network editor with a live mesh preview; split a spline or a section anywhere in the network
- Multi-lane model: asymmetric sections, per-lane zone types, offset/width curves, junctions, closed-loop fills
- Automated Intersection / Roundabout / Crosswalk tools + Mark & Sidewalk detail splines with magnetic snapping, fill patterns and polygon stamping *(Pro)*
- Lane attributes: speed & metadata, markings, road zones, cross-section (gutter) profiles, traffic signals, guardrails/props (spline-mesh/component/actor generators), lofted bridges & tunnels, landscape deformation, sidewalk ramps, curb cuts, surface polygons — extensible in Blueprint or C++
- Traffic Controller component: phases, per-signal states and a looping runtime clock
- Adjustable surface mesh density with a target edge length, in two modes (well-shaped triangles, or rows aligned to the road)
- Bake to StaticMesh/SplineMesh + decals with materials, multi-channel UVs (UV0/UV1/UV2) and vertex colors; configurable output + auto-cleanup
- FBX export; ZoneGraph AI-navigation generation *(Pro)*; PCG lane-data node *(Pro)*; real-world map tiles; City Sample compatible
- Reusable profile & build-preset assets; C++ and Blueprint APIs

**Code Modules:**
- `MetaRoad` — Runtime
- `MetaRoadEditor` — Editor
- `MetaRoadPCG` — Runtime (PCG integration) *(Pro)*

**Number of C++ Classes:** ‹fill in›
**Number of Blueprints:** ‹fill in›
**Supported Engine Versions:** 5.6, 5.7, 5.8
**Network Replicated:** No
**Supported Development Platforms:** Win64, Linux, macOS
**Supported Target Build Platforms:** All *(baked content is standard `StaticMesh`; the runtime graph module is optional)*
**Documentation:** https://unrealdrive.readthedocs.io/en/latest/
**Example Project / Important:** Baked meshes are plain StaticMesh assets and require no plugin at runtime.
