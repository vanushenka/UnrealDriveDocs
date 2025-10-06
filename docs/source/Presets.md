# Presets

**UUnrealDrivePreset** - класс, позволяющий хранить и использовать различные пользовательские присеты, такие как:
  - Профайлы для всех процедурно генерируемых объектов (поферхность дороги, сайдволки, маркировка, бордюры и др.)
  - The road lane attributes
  - Профайлы дорог для рисования (количество и типы полос) 
Пресетов в проекте может быть много, но UnrealDrive все они логически объеденяются в один. Поэтому нужно будет быть внимательным с именами профайлов в присетах, так как если в двух или более присетах будут найден профайлы с одинаковым именем, будет использоваться только один случайным образом.  
Для того, чтобы создать новый пресет, достаточно просто просто создать новый BP ассет в Content Browser, отнаследованный от UUnrealDrivePreset.  
![alt text](img/create-preset.gif)  
**UUnrealDrivePreset** отнаследован от **UPrimaryDataAsset**, поэтому важно чтобы в  **Asset Manager -> Primary Assets to Scan** были добавлены соотвествующие пути, где был создан пресет. Обычно достаточно указать только две директории **/Game** и **/UnrealDrive**, но если вы создаете пресет внутри вашего плагина, то необходимо указать пути и до соотвествующих плагинов, где находится пресеты. Смотри раздел [Installation](Installation.md) за подробностями.  
Плагин UnrealDrive в контенете уже имеет дефолтный пресет. Его не следует менять для обратной совместимосьти, но могут быть случае, когда это можеть быть необходимо.  
![alt text](img/default-preset.png)  

## Lane Mark Profiles
Содержит дескрипторы типов дорожной разметки вдоль дорожных полос. Можно задать тип (сплошная, прерывистая, двойная), размеры и цвет полосы разметки. Эти профайлы, будут доступны в режиме **Mark Editor Mode**:   
![alt text](img/preset-mark.png)  

## Curb Profiles
Содержит дескрипторы типов бордюров. Можно задать материал и геометрию бордюра. Эти профайлы, будут доступны в режиме **Build Mesh Modeling Tool**:  
![alt text](img/preset-curb.png)

## Driveable Material Profiles
Содержит дескрипторы типов driveable road lanes. Можно задать материал и декали для driveable road lanes. Эти профайлы, будут доступны в режиме **Build Mesh Modeling Tool**:  
![alt text](img/preset-driveable.png)

## Sidewalk Material Profiles
Содержит дескрипторы типов sidewolk road lanes. Можно задать материал sidewolk road lanes. Эти профайлы, будут доступны в режиме **Build Mesh Modeling Tool**:  
![alt text](img/preset-sidewolk.png)

## Road Lanes Material Profiles
Содержит дескрипторы типов road marks. Можно задать материал road marks. Эти профайлы, будут доступны в режиме **Build Mesh Modeling Tool**:  
![alt text](img/preset-mark-mat.png)

## Road Lanes Profiles
Содержит дескрипторы дорожных секций для рисования в режиме **Draw/Add Spline**: 
![alt text](img/preset-lanes.png)

## Road Attribute Entries
Содержит дескрипторы Road Lane Attributes. Аттрибут добавленный сюда, станет достпный как новый Road Editor Mode:    
![alt text](img/preset-attributes.png)