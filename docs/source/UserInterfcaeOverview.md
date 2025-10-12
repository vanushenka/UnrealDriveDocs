# User Interface Overview
После установки плагина, становятся доступны новые элемента пользовательского интерфейса в UnrealEngine и новые классы:
  * Меню [Road Editor Modes](EditorModes.md) - позволяет переключаться между режимами редактирования **URoadSplineComponent** для редактирования свойств сплайна, описанных в [Road Model](RoadModel.md):  
    ![alt text](img/modeling-tools.png)  
    </br>
  * **Road Modeling Toolset** предоставляет тулы для [рисования новых сплайнов](DrawTool.md) и [генерации ассетов](ProcedureGenerationTool.md):  
    ![alt text](img/edit-modes.png)  
    </br>
  * Два ActorComponents:
    * **URoadSplineComponent** - базовый компонент, который является элементарным элементом дорожной сети и реализует в себе концепции [Road Model](RoadModel.md)  
      ![alt text](img/ref-line.png)  
      </br>
    * [UTileMapWindowComponent](TileWindow.md) - позволяет рендерить открытые растровые geo-карты, такие как Google Map, OSM, Bind и др.  
      ![alt text](img/tile-latlon.gif)  
      </br>
  * [Пресеты](Presets.md) - мощный инструмент, который позволят сохранять, переиспользовать и распространять профайлы различных сущностей используемых в UnrealDrive такие как, профайлы процедурной генерации, профайлы [Lane Attributes](RoadModel.md#lane-attributes) и профайлы для [рисования дорог](DrawTool.md).  
    ![alt text](img/preset.png)  

