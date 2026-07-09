# Installation

```{important}
You can't install both MetaRoad Free and MetaRoad Pro plugins simultaneously in a single Unreal Engine. Make sure you only have one version installed. 
You can remove the extra version of the plugin through Epic Game Launcher here:  
![Removing a MetaRoad plugin version from the Epic Games Launcher](/img/uninstall-plugin.png)   
```

**MetaRoad** is a plugin for Unreal Engine, so the installation procedure for MetaRoad is the same as for a regular Unreal Engine plugin (see [Working with Plugins in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine)):  
  1. Copy the **MetaRoad Plugin** folder to the **Plugins** folder of your Unreal Engine project (next to the .uproject file) or to the **Engine\Plugins** folder of the engine. If you purchased and installed the plugin through [fab.com](https://www.fab.com/), it will already be copied to the **Engine\Plugins\Marketplace** folder.  
  2. From the main menu, go to **Edit -> Plugins**. This opens the **Plugins** window and enables the **MetaRoad** plugin:  
    ![The Plugins window with the MetaRoad plugin enabled](/img/plugins.png "Plugins Window")
  3. Make sure that **Translucent Selection** is allowed, otherwise there may be problems with selecting road lanes:  
     ![The Allow Translucent Selection option enabled in the editor](/img/allow-translucent-selection.png)

## Next steps

- [Quick Start](/getting-started/QuickStart.md) — build your first road.
- [The MetaRoad Workflow](/concepts/Workflow.md) — how create → edit → bake fit together.   