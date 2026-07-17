# About MetaRoad

**MetaRoad** turns Unreal Engine into a procedural road-network and **HD-map** editor. You author roads
interactively — draw, edit, preview, bake — and get real, game-ready meshes plus a logical road graph.

**Built for:** digital twins of cities · ADAS / autonomous-driving validation · games & cinematics.

## What it does

- **Author roads interactively** — draw splines, roundabouts, intersections, exits/entrances, and interchanges; edit
  lanes, sections, offsets, and widths in a dedicated editor mode with a live mesh preview.
- **Rich lane model** — any number of lanes with asymmetric sections and per-lane types: driving, sidewalk, bicycle,
  bus, parking, tram, and more.
- **Road markings** — configurable lane markings, stop lines, arrows, chevron guide-islands, and pedestrian crossings.
- **Attributes** — data and geometry sampled along lanes: speed limits and metadata, guardrails/barriers/fences, lamp
  posts, landscape deformation, sidewalk ramps, and fully custom types. Attributes are the plugin's main extension
  point — no core changes needed.
- **Bake to meshes** — generate static/spline meshes (drive surface, sidewalks, curbs, marks, decals) with materials,
  multi-channel UVs, and vertex colors. Export to **FBX** for any pipeline.
- **Logical road graph** — connections and junctions for traffic, pathfinding, and *(Pro)* **ZoneGraph** AI navigation.
- **Landscape integration** — deform the Unreal landscape to follow the roads *(Pro)*.
- **Extensible** — C++ and Blueprint APIs to add lane types, custom attributes, generators, and importers/exporters.

## Free vs Pro

Core authoring and baking are in the Free version; advanced tools (Intersection, Roundabout, Crosswalk, Mark,
Sidewalk), ZoneGraph, Landscape support, and several attributes are Pro — see [Pro vs Free](/introduction/ProVsFree.md).

## Good to know

Baked content is plain `StaticMesh` assets and works **without** the plugin. The plugin is only required at runtime if
you use the road **graph** in-game (e.g. to generate traffic).

## Start here

- [Installation](/introduction/Installation.md) → [Quick Start](/getting-started/QuickStart.md) →
  [The MetaRoad Workflow](/concepts/Workflow.md).
