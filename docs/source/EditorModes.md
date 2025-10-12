# Road Editor Modes
Road Editor Modes это режимы редактирования **URoadSplineComponent**. Каждый из режимов предоставляет доступ к редактированию соответствующих свойств, описанных в [Road Model](RoadModel.md).
![alt text](img/edit-modes2.png).  

## Base Modes

### Spline Mode
Этот режим позволяет взаимодеиствовать с **URoadSplineComponent** как с обычным сплайном UnrealEngine - создавать и удалять узлы, редактировать тангенты. Сам сплайн в этом режиме имеет розовый цвет.  
Согласно Road Model, **Spline Mode** это режим редактирования [Road Reference Line](RoadModel.md#road-reference-line).  
![alt text](img/spline-edit.gif)  
Из дополнительных функций редактирования сплайна - была добавлена возможность назначения тип узла - **Arc**:  
![alt text](img/spline-arc.gif)  
Так же в этом режиме можно управлять соединениями сплайнов (смотри [Intersections and Junctions](RoadModel.md#intersections-and-junctions)):  
![alt text](img/spline-conn.gif)  
В **Details Panel** в группе **Selection** доступна возможность редактирования выделенного узел сплайна:  
![alt text](img/spline-selection.png)  

### Section Mode
Этот режим позволят редактировать [Road Lanes](RoadModel.md#road-lanes) и [Lane Sections](RoadModel.md#lane-sections) описанные в [Road Model](RoadModel.md).  
Центральная сиреневая линия - это [Center Lane](RoadModel.md#road-lanes) и на най располагаются узлы, потянув за которые, можно изменить длину **Road Section**:  
![alt text](img/section-resize.gif)  
Через контекстное меню можно добавлять и удалять **Road Sections**:  
![alt text](img/section-split.gif)  
Так же добавлять и удалять **Road Lanes**:  
![alt text](img/lane-add.gif)  
В **Details Panel** в группе **Selection** доступна возможность редактировать выделенный **Road Section**:  
![alt text](img/section-selected.png)  
Так же в **Details Panel** в группе **Selection** доступна возможность редактировать выделенный **Road Lane**:  
![alt text](img/lane-selection.png)  

### Offset Mode
Этот режим позволят задавать смещения **Center Lane** относительно [Road Reference Line](RoadModel.md#road-reference-line) и соответствует [Lane Offset](RoadModel.md#lane-offset) описанному в [Road Model](RoadModel.md).  
Редактирование ширины **Road Offset** похоже на редактирование сплайна - можно задать произвольное форму, добавлять/удалять узлы, редактировать тангенты:
![alt text](img/offset.gif)  
В **Details Panel** в группе **Selection** доступна возможность редактировать выделенный **Offset Key**:  
![alt text](img/offset-selection.png)  

### Width Mode
Этот режим позволят редактировать ширину **Road Lane**.  
Редактирование **Road Lane** так же похоже на редактирование сплайна - можно задать произвольное форму, добавлять/удалять узлы, редактировать тангенты:
![alt text](img/width.gif)  
В **Details Panel** в группе **Selection** доступна возможность редактировать выделенный **Width Key**:  
![alt text](img/width-selection.png)  

## Attribute Modes
Эти режимы позволяют добавлять к **Road Lane** различные **Road Attributes**, которые могут использоваться для процедурной генерации или любых других целей (смотри раздел [Road Attributes](RoadModel.md#lane-attributes)).  
![alt text](img/attributes.png)  
По умолчанию, доступно два типа атрибутов - speed limit и дорожная разметка. 
Как создавать новые типы аттрибутов - смотри [Road Attribute Entries](Presets.md#road-attribute-entries).  
Чтобы добавить новый аттрибут для полосы, необходимо выбрать соответствующий режим в меню **Road Editor Modes**, выделить необходимый **Road Lane** и в контекстом меню выбрать пункт **Create ATTRIBUTE_NAME**. После чего, из того же контентного меню добавить необходимые **Attribute Keys**:  
![alt text](img/attribute-add.gif)  
И в **Details Panel** в группе **Selection** доступна возможность редактировать выделенный **Attribute Key**:  
![alt text](img/attribute-selection.png)  

### Road Mark Attribute
Как следует из названия **Road Mark Attribute** - это один из типов [Road Attributes](RoadModel.md#lane-attributes), который доступен "из коробки" и позволят добавить в **Road Lane** атрибут типа **Mark**, который используется в [Процедурной Генерации](ProcedureGenerationTool.md) для генерации дорожной разметки. За каждым **Attribute Key** закрепляется типа дорожной разметки, который можно выбрать в ```Profile Name```. или создать новый тип на месте (```Profile Name -> Use Custom```):  
![alt text](img/mark.png)  
Если для какого-то из участков на **Road Lane** необходимо убрать разметку, то ```Profile Name``` необходимо устанавливается в ```None```:
![alt text](img/mark-none.png)  
Для добавления новых профайлов дорожной разметки, смотри [Lane Mark Profiles](Presets.md#lane-mark-profiles).