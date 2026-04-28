# septic.sep

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/databases/septic.sep -->

Information of water quality or effluent characteristics required to simulate different types of Onsite Wastewater Systems (OWSs) is stored in the septic water quality database. The information contained in the septic water quality database includes the septic tank effluent flow rate for per capita and the effluent characteristics of various septic systems. The database file distributed with SWAT+ includes water quality data for most conventional, advanced, and failing septic systems. It was developed based on the field data summarized by Siegrist et al. (2005), McCray et al. (2005), and OWTS 201 (2005).

| Field                                                           | Description                                                 | Type   | Unit  | Default | Range     |
| --------------------------------------------------------------- | ----------------------------------------------------------- | ------ | ----- | ------- | --------- |
| [name](septic.sep/name_sepdb.md) | Name of the septic record                                   | string | ​n/a  | ​n/a    | n/a       |
| [q\_rate](septic.sep/q_rate.md)  | Flow rate of the septic tank effluent                       | ​real  | m^3/d | 0.0     | 0.0-1.0   |
| [bod](septic.sep/bod.md)         | ​7-day Biological Oxygen Demand of the septic tank effluent | ​real  | mg/l  | ​0.0    | 0.0-300.0 |
| [tss](septic.sep/tss.md)         | Total suspended solids in the septic tank effluent          | ​real  | ​mg/l | ​0.0    | 0.0-300.0 |
| [nh4\_n](septic.sep/nh4_n.md)    | ​Ammonium nitrogen in the septic tank effluent              | ​real  | ​mg/l | ​0.0    | ​         |
| [no3\_n](septic.sep/no3_n.md)    | ​Nitrate nitrogen in the septic tank effluent               | ​real  | ​mg/l | 0.0     |           |
| [no2\_n](septic.sep/no2_n.md)    | Nitrite nitrogen in the septic tank effluent                | real   | mg/l  | 0.0     |           |
| [org\_n](septic.sep/org_n.md)    | Organic nitrogen in the septic tank effluent                | real   | mg/l  | 0.0     |           |
| [min\_p](septic.sep/min_p.md)    | Mineral phosphorus in the septic tank effluent              | real   | mg/l  | 0.0     |           |
| [org\_p](septic.sep/org_p.md)    | Organic phosphorus in the septic tank effluent              | real   | mg/l  | 0.0     |           |
| [fcoli](septic.sep/fcoli.md)     | Number of fecal coliform in the septic tank effluent        | real   | mg/l  | 0.0     |           |

#### References

> Siegrist et al. (2005)
>
> McCray et al. (2005)
>
> OWTS 201 (2005)

Last updated 1 year ago
