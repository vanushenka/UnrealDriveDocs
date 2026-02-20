# Zone Graph (Pro)

Билдниг **ZoneGraphData** происходит через меню **Build->Build ZoneGraph**, так же как и в [стандартном подходе для ZoneShape](https://dev.epicgames.com/community/learning/tutorials/qz6r/unreal-engine-zonegraph-quick-start-guide). В результате чего будет сгенерировано по одному **ZoneGraphData** актору для каждого левела, который будет содержать навигационные данные для соотвествующего левела:  
![alt text](img/zone-graph-build.png)  

Визуализация построенных **ZoneGraphData** удобно посмотреть, активировав флаг **Navigation**:  
![alt text](img/zone-graph-view-debug.png)  

**ZoneGraphData** не не билдится для **URoadSplineComponent**. Билдниг **ZoneGraphData** будет происходить только для тех акторов, у которых есть компонент **URoadGraphDataComponent**. :  
![alt text](img/zone-graph-data.png)  

**URoadGraphDataComponent** генерируется в момент генерации меша (см. [Build Mesh Modeling Tool](ProcedureGenerationTool.md)) и содержит даные необходимы для генерации графов дорог (включая ZoneGraph):  
![alt text](img/zone-graph-data2.png)  

В **Edit -> Project Settings -> MetaRoad Editor** можно указать соотвесте **Road Lane Types** и **Zone Graph Tags** для того чтобы выбрать для каких типов дорожных полос необходимо генерировать **ZoneGraphData**:
![alt text](img/zone-graph-settings.png)  

В примере ниже показано, что для трамвайной полосы был сгенерирован участок ZoneGraph с Tag = Tram:
![alt text](img/zone-graph-settings2.png)  



