# Connectivity

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/connectivity -->

Gravity-controlled flow is routed from one spatial object to the next using so-called connect files, which are available for the following objects:

| Object             | Connect file   |
| ------------------ | -------------- |
| HRU                | hru.con        |
| HRU-lte            | hru-lte.con    |
| Routing Unit       | rout\_unit.con |
| Aquifer            | aquifer.con    |
| SWAT-DEG channel   | chandeg.con    |
| Reservoir          | reservoir.con  |
| Point source/inlet | recall.con     |
| Export coefficient | exco.con       |
| Delivery ratio     | delratio.con   |
| Outlet             | outlet.con     |

All connect files have the exact same structure, so to avoid repetition it is only described once instead of for every spatial object (see [**'object'.con**](hru.con.md)). The connectivity between objects can be changed during the simulation using Decision Tables.

If the user wishes to connect an aquifer to more than one channel, the [**aqu\_cha.lin**](aqu_cha.lin.md) file can be used instead of the aquifer connect file.

Last updated 1 year ago
