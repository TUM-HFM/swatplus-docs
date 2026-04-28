# 'obj'

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/connectivity/hru.con/hru -->

The pointer to the object data file is a foreign key referencing the unique ID in the respective object data file. The header of this column is different in each connect file.

| Connect file   | Column header | Object data file                                                                   |
| -------------- | ------------- | ---------------------------------------------------------------------------------- |
| hru.con        | hru           | [**hru-data.hru**](../../hydrologic-response-units/hru-data.hru.md) |
| hru-lte.con    | hlt           | [**hru-lte.hru**](../../hydrologic-response-units/hru-lte.hru.md)   |
| rout\_unit.con | rtu           | [**rout\_unit.rtu**](../../routing-units/untitled.md)               |
| aquifer.con    | aqu           | [**aquifer.aqu**](../../aquifers/aquifer.aqu.md)                    |
| chandeg.con    | lcha          | [**channel-lte.cha**](../../channels/channel-lte.cha.md)            |
| reservoir.con  | res           | [**reservoir.res**](../../reservoirs/reservoir.res.md)              |
| recall.con     | rec           | [**recall.rec**](../../point-sources-and-inlets/recall.rec.md)      |
| exco.con       | exc           |                                                                                    |
| delratio.con   | dlr           |                                                                                    |
| outlet.con     | out           | No data file                                                                       |

Last updated 1 year ago
