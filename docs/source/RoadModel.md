# Road Model

## Basic concepts
В основе модели дорожной сети и всего плагина UnrealDrive лежит ActorComponent **URoadSplineComponent**.
**URoadSplineComponent** - это единственный и достаточный компонент, с помощью которого представляется граф дорожных сетей. Хотя сам компонент описывает всего лишь один простой участок дороги, комбинация **URoadSplineComponent**s способна описать даже очень сложную дорожную сеть, развязки и перекрестки.  
Любой участок дорожной сети на сцене - это произвольный AActor, который включает в себя один или несколько **URoadSplineComponent**, при том, одна дорога, как правило, состоит из одного **URoadSplineComponent**, а перекрестки или развязки - из нескольких.  
Тем, кто знаком со спецификацией [ASM OpenDrive](https://www.asam.net/standards/detail/opendrive/), все идеи, реализованные в **URoadSplineComponent**, покажутся очень знакомыми. Действительно UnrealDrive подчеркнул очень многое из этой спецификации.  

## Road Reference Line
**URoadSplineComponent** - унаследован от [USplineComponent](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/USplineComponent), т.е. он обладает всеми свойствами базового сплайна, который является опорной линией, вдоль генерируемой дорога.
Опорная линия обозначается розовым цветом. It is a left-handed coordinate system. The S-axis (or S-Offset in UI) follows the tangent of the road reference line. The R-axis (R-Offset in UI) is orthogonal to the S-axis and may be rotated around the S-axis by superelevation. The left-handed coordinate system is completed by defining the up-direction H orthogonal to S-axis and R-axis.  
![alt text](img/ref-line.png "Reference Line")

## Road Lanes
Lanes are an essential part of all roads. Lanes are attached to the road reference line of the road and are defined from inside to outside. A minimum road definition requires a center lane and an additional lane with a defined width. The number of lanes per road is not limited.
The center lane has no width and serves as reference for lane numbering. The center lane itself has the lane index 0. The numbering of the other lanes starts at the center lane: Lane numbers descend to the right, meaning a positive  R-direction, and ascend to the left, meaning a negative R-direction.
![alt text](img/lane-indexes.png "Lane Indexes")
This figure shows the center lane for a road with multiple traffic lanes and different driving directions. In this case, the center lane separates the driving directions, depending on left- and right-hand traffic, specified in Road type. Because no lane offset is used, the center lane is identical to the road reference line.

### Lane Types
The lane type is defined per lane. A lane type defines the main purpose of a lane and its corresponding traffic rules. Есть базовые типы (такие как: driving, shoulder, border, biking, etc) и пользовательские (могут быть добавлены через C++ API).  
![alt text](img/lane-types.png "Lane Types")  

### Lane Direction
Каждая полоса дороги имеет направление. На графах это направление показано белыми движущимися стрелками. This direction is specified by a combination of different elements and attributes. Для любой отдельной линии можно поменять направление движения.  
![alt text](img/lane-dir.png "Lane Direction")  
На данной фигуре показано что линия с индексом -1 имеет инвертирование направление.

### Lane Groups
For easier navigation through road description, the lanes within a lane section are grouped into left, center, and right lanes.
![alt text](img/lane-group.png "Lane Groups")

### Lane Sections
Lanes may be split into multiple lane sections. Each lane section contains a **fixed number of lanes**.  
![alt text](img/lane-sections.png "Lane Sections")  
This figure shows that every time the number of lanes changes, a new lane section is required. Lane sections are defined in ascending order along the road reference line.  

![alt text](img/lane-sections-adv.png "Lane Sections Advanced")  
This figure shows how lane sections for complex roads may be defined for one side of the road only - left, right and both sides

### Lane Offset
A lane offset may be used to shift the center lane away from the road reference line. This makes it easier to model local lateral shifts of lanes on roads, for example for left turn lanes.  
A combination of lane offset and shape definition can lead to inconsistencies depending on the interpolation used for the lane offset. Because linear interpolation is used for the road shape along the road reference line, linear interpolation should also be used for the offset definition to enable consistent combined use of both definitions.  
![alt text](img/lane-offset.png "Lane Offset")  
This figure shows the offset of the center lane away from the road reference line.

### Lane Attributes
Lane attributes это произвольные метаданные, которы могут быть закреплены вдоль **Road Lane**.  
Это один из самых мощных инструментов для кастомизации и добавления новых возможностей в UnrealDrive. Пользователь может зарегистрировать и определять поведение любого количества атрибутов. Атрибуты могут быть использованы для кастомизации процедурной генерации (например, для обозначения участков неровной дороги), для определения приоритетов движения и ограничение скорости (например, для генерации дорожного трафика), генерации spline mesh (например, для генерации ограждений вдоль полосы или растительности) и другое.  
Атрибут обладает следующими свойствами:
  - Атрибут имеет уникальное имя (например: speed, mark, fence), которое является типом атрибута.
  - Добавленный атрибут распространяется на всю **Road Lane**.
  - Атрибут имеет один или несколько **Attribute Key**.
  - Первый **Attribute Key** фиксировано расположен в начале **Road Lane** (SOffset = 0) 
**Attribute Key** - это пара значений **SOffset** + **Attribute Data**. **SOffset** - это положение **Attribute Key**, SOffset равный 0 - это начало **Road Lane**. **Attribute Data** - это произвольная С++ или BP структура (например, скоростные лимиты, плотность трафика, тип газона на обочине и др.).
 

![alt text](img/lane-attr.png "Lane Attribute")  
Данная фигура показывает визуализацию атрибута - **Speed**. В этом примере только одна **Road Lane** с ID ```+1``` в **RoadSection** ```1```  имеет Атрибут **Speed**.  Данный Атрибут устанавливает скорость движения трафика на **Road Lane** и имеет 3 ключа с координатами SOffset: 0cm, 400cm, 800см. Ключ содержит только одно поле данных ```speed``` типа - число с плавающей точкой. Три ключа из примера имеют соответствующие данные: 20km/h,  60km/h, 100km/h. 

## Intersections and Junctions
В UnrealDrive нет специальных типов или классов, которые могли бы отвечать за функцию создания перекрестков или развязок. В место этого, UnrealDrive предлагает возможность линковать несколько **URoadSplineComponent** между собой. В свою очередь группа залинкованных **URoadSplineComponent** могут представлять собой перекресток или развязку естественным образом.  

Как уже было сказано, у каждой **Road Lane** есть направление. Вдоль этого направлению в начале и конец есть *Lane Predecessor Connection* и *Lane Successor Connection* соответственно. 
Так же у каждого сплайна **URoadSplineComponent** то же есть направление, начало и конец. Эти начало конец являются *Road Predecessor Connection* и *Road Successor Connection*.  
![alt text](img/connections.png "Road and Lane Connections")  

Есть только два правила линковки:
  * *Road Successor Connection* -> *Lane Predecessor Connection* (связь один ко многим)  
    ![alt text](img/predecessor-to-successor.png) 
  * *Road Predecessor  Connection* -> *Lane SuccessorConnection* (связь один ко многим)  
    ![alt text](img/successor-to-predecessor.png)

Двух этих правил достаточно чтобы смоделировать любые перекрестки или развязки, даже самые сложные.  
![alt text](img/junction.png)  

