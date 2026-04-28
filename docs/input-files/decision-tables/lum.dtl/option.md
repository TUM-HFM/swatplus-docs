# option

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/decision-tables/lum.dtl/option -->

| Action                              | Option                | Description                                                                         |
| ----------------------------------- | --------------------- | ----------------------------------------------------------------------------------- |
| plant, harvest, kill, harvest\_kill | "crop"                | Pointer to management.sch if one crop is listed behind the name of the DT           |
| plant, harvest, kill, harvest\_kill | "crop1", "crop2", ... | Pointer to management.sch if more than one crop is listed behind the name of the DT |
| plant, harvest, kill, harvest\_kill | Name of the crop      | Pointer to plant community in plant.ini                                             |
| release                             |                       |                                                                                     |
|                                     |                       |                                                                                     |
|                                     |                       |                                                                                     |
|                                     |                       |                                                                                     |
|                                     |                       |                                                                                     |
|                                     |                       |                                                                                     |
|                                     |                       |                                                                                     |
|                                     |                       |                                                                                     |

| Option      | Description                                                                | const                          | const2               | fp            |
| ----------- | -------------------------------------------------------------------------- | ------------------------------ | -------------------- | ------------- |
| rate        | Release at constant rate                                                   | Release rate in m3/s           |                      |               |
| rate\_pct   | Release at percentage of principal volume                                  | Percentage of principal volume |                      |               |
| inflo\_frac | Release at fraction of inflow                                              | Fraction of inflow             |                      |               |
| ab\_emer    | Release all volume above emergency                                         | Emergency volume               |                      |               |
| days        | Number of days it takes to drawdown to target volume                       | Number of days                 | Multiplier           | Target volume |
| dyrt        | Release based on drawdown days and percentage of principal volume          | Number of days                 | Release rate in m3/s |               |
| inflo\_targ | Release inflow and all volume over target                                  |                                |                      | Target volume |
| irr\_dmd    | Release based on irrigation demand of HRU or other water allocation object |                                |                      |               |
| weir        | Release based on weir equation                                             |                                |                      |               |
| meas        | Release measured outflow                                                   |                                |                      | Recall file   |

Last updated 1 year ago
