# About
The MetaRoad is a plugin for UnrealEngine that turns UnrealEngine into a powerful road network editor. 

The main purpose of the MetaRoad is to provide a tool for creating a **High Definition** road networks:
  - To create digital twins of cities
  - For simulations to validate ADAS (advanced driver-assistance systems) and AD (autonomous driving) features. 
  - For games and cinematic
	
The MetaRoad allows to interactively create:
  - Any types of road junctions, roundabouts, exits and entrances, etc. 
  - Sidewalks and any types of special roads lanes: bicycle, bus, parking, tram, etc.
  - Generate road additional objects: street lights, vegetation(trees, bushes, grass), bridges etc.
  - Adjustable road markings for any road lane
  - Road metadata (attributes) -  can be used for game mechanics, for examples: speed limits, vehicle movement priorities, triggers etc.
  - Decal generation - allows to apply the effects of rutting and asphalt wear, rutting from snow and dirt, etc.
	
Conceptually, the plugin solves two problems: 
  - Creation of logical road networks (graphs). 
    The road graphs can be used to create elements of game mechanics - traffic generation, laying out paths for game characters, etc. 
    Also, in future releases it is planned to move the road graph functionality into a separate free or OpenSource plugin.
  - Procedural generation of 3D models based on the constructed road graphs. 
	
The plugin provides flexible APIs (C++ and BluePrint), allowing to:
  - Customize the road network (for example, adding a new type of traffic lanes - tram), 
  - Develop external algorithms for procedural generation (for example, generating bushes along the road).
  - Develop importers/exporters of road networks to/from any custom formats
  - Use the road graph to develop any gameplay logic.

Generated content can be used without the plugin itself, as these are simple StaticMesh assets. But if there is a need to use graphs in a game project (for example, to generate traffic), then the presence of the UnrealDrive plugin will be necessary in the project.