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

### Reservoir release options

| Option      | Description                                                                | const                          | const2               | fp            |
| ----------- | -------------------------------------------------------------------------- | ------------------------------ | -------------------- | ------------- |
| rate        | Release at constant rate                                                   | Release rate in m3/s           |                      |               |
| rate\_pct   | Release at percentage of principal volume                                  | Percentage of principal volume |                      |               |
| inflo\_frac | Release at fraction of inflow                                              | Fraction of inflow             |                      |               |
| ab\_emer    | Release all volume above emergency                                         | Emergency volume               |                      |               |
| days        | Number of days it takes to drawdown to target volume                       | Number of days                 | Multiplier           | Target volume |
| dyrt        | Release based on drawdown days and percentage of principal volume          | Number of days                 | Release rate in m3/s |               |
| inflo\_targ | Release inflow and all volume over target                                  |                                |                      | Target volume |
| irrig\_dmd    | Release based on irrigation demand of HRU or other water allocation object |                                |                      |               |
| weir        | Release based on weir equation                                             |                                |                      |               |
| meas        | Release measured outflow                                                   |                                |                      | Recall file   |


### Divert options

| Option      | Description                                                                | const                          | const2               | fp            |
| ----------- | -------------------------------------------------------------------------- | ------------------------------ | -------------------- | ------------- |
| flo_cms     | Sets constant diversion rate                                               | Diversion rate in m3/s         |                      |               |
| min_cms     | Defines a minimum flow in the source; only transfer the excess             | Min. flow value in m³/s        |                      |               |
| all_flo     | Transfer all the flow from the source                                      | -                              |                      |               |
| min_frac    | Transfer a fraction of the source's flow                                   | Fraction betwen 0 and 1.0      |                      |               |
| recall      | Use records of transferred volumes at daily, monthly and yearly timesteps  |                                |                      |               |

Last updated 4th May 2026
