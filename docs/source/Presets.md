# Presets

**UUnrealDrivePreset** - класс, позволяющий хранить и использовать различные пользовательские присеты, такие как:
  - Профайлы для всех процедурно генерируемых объектов (поферхность дороги, сайдволки, маркировка, бордюры и др.)
  - The road lane attributes
  - Профайлы дорог для рисования (количество и типы полос)  

Пресетов в проекте может быть много, но логически все они объеденяются в один. Поэтому нужно быть внимательным с именами профайлов в присетах, так как если в двух или более присетах будут найден профайлы с одинаковым именем, будет использоваться только один случайным образом.  
Для того, чтобы создать новый пресет, достаточно просто просто создать новый BP ассет в Content Browser, отнаследованный от UUnrealDrivePreset.  
![alt text](img/create-preset.gif)  
**UUnrealDrivePreset** отнаследован от **UPrimaryDataAsset**, поэтому важно чтобы в  **Asset Manager -> Primary Assets to Scan** были добавлены соотвествующие пути, где был создан пресет. Обычно достаточно указать только две директории **/Game** и **/UnrealDrive**, но если вы создаете пресет внутри вашего плагина, то необходимо указать пути и до соотвествующих плагинов, где находится пресеты. Смотри раздел [Installation](Installation.md) за подробностями.  
Плагин UnrealDrive в контенете уже имеет дефолтный пресет. Его не следует менять для обратной совместимосьти, но могут быть случае, когда это можеть быть необходимо.  
![alt text](img/default-preset.png)  

## Lane Mark Profiles
Содержит дескрипторы типов дорожной разметки вдоль дорожных полос. Можно задать тип (сплошная, прерывистая, двойная), размеры и цвет полосы разметки. Эти профайлы, доступны в режиме [Road Mark Attribute](EditorModes.md#road-mark-attribute):   
![alt text](img/preset-mark.png)  

## Curb Profiles
Содержит дескрипторы типов бордюров. Можно задать материал и геометрию бордюра. Эти профайлы, будут доступны в режиме [Build Mesh Modeling Tool](ProcedureGenerationTool.md):  
![alt text](img/preset-curb.png)

## Driveable Material Profiles
Содержит дескрипторы типов driveable road lanes. Можно задать материал и декали для driveable road lanes. Эти профайлы, будут доступны в режиме [Build Mesh Modeling Tool](ProcedureGenerationTool.md):  
![alt text](img/preset-driveable.png)

## Sidewalk Material Profiles
Содержит дескрипторы типов sidewolk road lanes. Можно задать материал sidewolk road lanes. Эти профайлы, будут доступны в режиме [Build Mesh Modeling Tool](ProcedureGenerationTool.md):  
![alt text](img/preset-sidewolk.png)

## Road Lanes Material Profiles
Содержит дескрипторы типов road marks. Можно задать материал road marks. Эти профайлы, будут доступны в режиме [Build Mesh Modeling Tool](ProcedureGenerationTool.md):  
![alt text](img/preset-mark-mat.png)

## Road Lanes Profiles
Содержит дескрипторы дорожных секций для рисования в режиме **Draw/Add Spline** [Build Mesh Modeling Tool](DrawTool.md#lane-source) -> **Road Profile**: 
![alt text](img/preset-lanes.png)

## Road Attribute Entries
**Road Attribute Entrie** - это вспомогательный объект-констуктор, который позволяет быстро создовать престы [Lane Attribute](RoadModel.md#lane-attributes) и быстра добавлять их на **Road Lane**. Все **Road Attribute Entries** из всех пресетов, автоматически становтся доступны в [Road Attribute Editor Mode](EditorModes.md#attribute-modes)  
![alt text](img/preset-attributes.png)  
Есит 3 основных типа **Road Attribute Entrie** (Component Template, Spline Mesh, Custom Builder):  
![alt text](img/entry-type.png)  

### Component Template
Позволят генерировать произвольный **USceneComponent** вдоль **Road Lane** с заданным интервалом в процессе [Build Mesh](ProcedureGenerationTool.md).  
Достаточно создать BP или С++ класс отнаследованный от **USceneComponent** (например **Cone**):  
![alt text](img/entry-component.png)  
И в **Road Attribute Entriy** указать созданный класс  в ```Component Template``` и задать ```LengthOfSegment```, после чего, созданный пресет станет доступен в [Lane Attribute](RoadModel.md#lane-attributes):  
![alt text](img/entry-component2.png)  
И теперь его можно добавлять на **RoadLane**:  
![alt text](img/entry-component4.gif)  
Этот шаблон удобно использовать для потовряющихся объектов в доль **Road Lane**, напрмиер дорожные конусы, древки, фонарные столбы, линии электро передач:  

### Spline Mesh
Позволят генерировать USplineMeshComponent вдоль **Road Lane** в процессе [Build Mesh](ProcedureGenerationTool.md).  
Для этого необходимо в **Road Attribute Entriy** указать желаемый ```Static Mesh``` и задать ```LengthOfSegment```, после чего, созданный пресет станет доступен в [Lane Attribute](RoadModel.md#lane-attributes):
![alt text](img/entry-spline.png)  
И теперь его можно добавлять на **RoadLane**:  
![alt text](img/entry-spline2.gif)  

### Custom Builder
Предоставлят возможность написать кастомный обработчик атрибута на С++ или BP скрипту в процессе [Build Mesh](ProcedureGenerationTool.md) 
Для этого необходимо создать класс отнаследованный от **UCustomSplineBuilder** и переопределить функцию **Generate Asset**:  
![alt text](img/entry-custom.png)  
После регестрируем созданный класс в пресете и он станет доступен в [Lane Attribute](RoadModel.md#lane-attributes) для добавления его на **RoadLane**:  
![alt text](img/entry-custom2.png)  