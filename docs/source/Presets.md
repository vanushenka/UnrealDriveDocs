# Presets

**UUnrealDrivePreset** - класс, позволяющий хранить и использовать различные пользовательские присеты, такие как:
  - Профайлы для всех процедурно генерируемых объектов (Road Surface, Sidewalk, маркировка, бордюры и др.)
  - The road lane attributes
  - Профайлы дорог для рисования (количество и типы полос)  

Пресетов в проекте может быть много, но логически все они объединяются в один. Поэтому нужно быть внимательным с именами профайлов в присетах, так как если в двух или более присетах будут найдены профайлы с одинаковым именем, будет использоваться только один случайным образом.  
Для того, чтобы создать новый пресет, достаточно просто просто создать новый BP ассет в **Content Browser**, унаследованный от UUnrealDrivePreset.  
![alt text](img/create-preset.gif)  

**UUnrealDrivePreset** отнаследован от **UPrimaryDataAsset**, поэтому важно чтобы в  **Asset Manager -> Primary Assets to Scan** были добавлены соответствующие пути, где был создан пресет. Обычно достаточно указать только две директории **/Game** и **/UnrealDrive**, но если пресет создан внутри какого либо плагина, то необходимо указать пути и до соответствующих плагинов, где находится пресеты (Смотри раздел [Installation](Installation.md)).  
Плагин UnrealDrive уже имеет дефолтный пресет по пути */UnrealDrive/DefaultPreset*. Его не следует менять для обратной совместимости, но могут быть случаи, когда в это может быть необходимость (например, для смены левостороннего движения на правостороннее).  
![alt text](img/default-preset.png)  

## Driveable Material Profiles
Содержит профайлы материалов для **Road Lane** типа **RoadLaneDriving**. Можно задать материал и декали для driveable road lanes. Эти профайлы доступны в режиме [Build Mesh Modeling Tool](ProcedureGenerationTool.md):  
![alt text](img/preset-driveable.png)

## Sidewalk Material Profiles
Содержит профайлы материалов для **Road Lane** типа **RoadLaneSidewalk**. Можно задать материал sidewalk road lanes. Эти профайлы, будут доступны в режиме [Build Mesh Modeling Tool](ProcedureGenerationTool.md):  
![alt text](img/preset-sidewolk.png)

## Curb Profiles
Содержит профайлы типов бордюров для **Road Lane** типа **RoadLaneSidewalk**. Можно задать материал и геометрию бордюра. Эти профайлы доступны в режиме [Build Mesh Modeling Tool](ProcedureGenerationTool.md):  
![alt text](img/preset-curb.png)

## Lane Mark Profiles
Содержит профайлы типов дорожной разметки для **Road Lane** типа **RoadLaneDriving**. Можно задать тип (сплошная, прерывистая, двойная), размеры и цвет полосы разметки. Эти профайлы доступны в режиме [Road Mark Attribute](EditorModes.md#road-mark-attribute):   
![alt text](img/preset-mark.png)  

## Road Lanes Material Profiles
Содержит профайлы материалов дорожной разметки для **Road Lane** типа **RoadLaneDriving**. Можно задать материал Road Marks. Эти профайлы, будут доступны в режиме [Build Mesh Modeling Tool](ProcedureGenerationTool.md):  
![alt text](img/preset-mark-mat.png)

## Road Lanes Profiles
Содержит профайлы дорожных секций для рисования в режиме **Draw/Add Spline** [Build Mesh Modeling Tool](DrawTool.md#lane-source) -> **Road Profile**: 
![alt text](img/preset-lanes.png)

## Road Attribute Entries
**Road Attribute Entry** - это вспомогательный объект-конструктор, который позволяет быстро создавать престы для [Lane Attribute](RoadModel.md#lane-attributes) и добавлять их на **Road Lane**. Все **Road Attribute Entries** из всех пресетов, автоматически доступны в [Road Attribute Editor Mode](EditorModes.md#attribute-modes):  
![alt text](img/preset-attributes.png)   

Есть 3 основных типа **Road Attribute Entries** (Component Template, Spline Mesh, Custom Builder):  
![alt text](img/entry-type.png)  

### Component Template
Позволяет генерировать произвольный **USceneComponent** вдоль **Road Lane** с заданным интервалом в процессе [Build Mesh](ProcedureGenerationTool.md).  
Достаточно создать BP или С++ класс унаследованный от **USceneComponent**:  
![alt text](img/entry-component.png)  

И в **Road Attribute Entry** указать созданный класс  в ```Component Template``` и задать ```LengthOfSegment```, после чего, созданный пресет станет доступен в [Lane Attribute](RoadModel.md#lane-attributes):  
![alt text](img/entry-component2.png)  

И теперь его можно добавлять на **RoadLane**:  
![alt text](img/entry-component4.gif)  

Этот шаблон удобно использовать для повторяющихся объектов вдоль **Road Lane**, например, дорожные конусы, древки, фонарные столбы, линии электро передач.  

### Spline Mesh
Позволяет генерировать **USplineMeshComponent** вдоль **Road Lane** в процессе [Build Mesh](ProcedureGenerationTool.md).  
Для этого необходимо в **Road Attribute Entry** указать желаемый ```Static Mesh``` и задать ```LengthOfSegment```, после чего, созданный пресет станет доступен в [Lane Attribute](RoadModel.md#lane-attributes):
![alt text](img/entry-spline.png)  

И теперь его можно добавлять на **RoadLane**:  
![alt text](img/entry-spline2.gif)  

### Custom Builder
Предоставляет возможность написать кастомный обработчик атрибута на С++ или BP в процессе [Build Mesh](ProcedureGenerationTool.md). 
Для этого необходимо создать класс унаследованный от **UCustomSplineBuilder** и переопределить функцию **Generate Asset**:  
![alt text](img/entry-custom.png)  

После чего необходимо указать созданный класс в пресете и он станет доступен в [Lane Attribute](RoadModel.md#lane-attributes):  
![alt text](img/entry-custom2.png)  