# Tile Window

**Tile Window** - это Actor, который позволяет рендерить открытые растровые geo-карты, такие как Google Map, OSM, Bind и др. Может оказаться полезным для создания цифровых двойников территорий реального мира.  

Для начала использования, достаточно просто разместить **Tile Windows** актор на сцену:  
![alt text](img/tile-create.gif)  

## Система координат
Достаточно задать ```Longitude``` и ```Latitude``` и **Tile Window** мгновенно перегенерит область окна:  
![alt text](img/tile-latlon.gif)  

Параметр ```Use World Coordinate Space``` определяет начало координат для ```Longitude``` и ```Latitude``` в мире Unreal Engine:
  - Если флаг не установлен, то за начало координат берутся координаты **Tile Window** Актора
  - Если флаг установлен, то за начало координат берется точка (0, 0)  мира Unreal Engine. В этом случае при изменении координат **Tile Window** Актора, будет автоматически пересчитана область окна **Tile Window** согласно новым координатам. Обычно такой режим удобнее использовать для воссоздания больших участков территорий земли. Так как в этом случае  **Tile Window** работает как "окно" в реальный мир, и при его перемещении будет автоматически отображен новый участок карты:  
  ![alt text](img/tile-world-space.gif)  

## Размеры окна:
Для изменения размера и разрешения окна используется два параметра ```Window Size``` и ```Zoom```:  
![alt text](img/tile-size.png)    
  - ```Zoom``` - Map tile zoom levels determine the level of detail and the number of tiles displayed by dividing the world into a grid of square tiles at each zoom level, more details [here](https://wiki.openstreetmap.org/wiki/Zoom_levels). Оптимальный уровень zoom - не меньше 18. Редко какие tile sources поддерживают zoom больше 22.
  - ```Window Size``` - определяет количество тайлов (по горизонтали и вертикали), которое следуют отрендерить. Не стоит здесь указывать слишком большие значения в целях избежания переполнения видео памяти:
  ![alt text](img/tile-size2.png)  

## Источники карт
По умолчанию **Tile Window** поддерживает Google, OSM и Yandex карты. Достаточно просто сменить ```Source```:  
![alt text](img/tile-source.gif)  
</br>
Так же есть возможность добавить собственные источники, для этого необходимо зайти в **Edit -> Project Settings -> Unreal Drive Editor** и добавить новый источник в ```Tile Sources```:  
![alt text](img/tile-add-source.png)  
</br>
```URL``` источника это произвольный URL адрес формата ```https://sample.map.source.com/{x}/{y}{z}```, где ```{x}```, ```{y}```, ```{z}``` будут заменены на x, y, z координаты тайлов во время рендеринга.


