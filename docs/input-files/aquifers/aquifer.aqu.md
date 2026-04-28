# aquifer.aqu

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/aquifers/aquifer.aqu -->

| Field                                                                | Description                                                                      | Type    | Unit      | Default | Range  |
| -------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------- | --------- | ------- | ------ |
| [id](aquifer.aqu/id-aquifer.aqu.md)    | ID of the aquifer                                                                | integer | n/a       |         |        |
| [name](aquifer.aqu/name.md)            | Name of the aquifer                                                              | string  | n/a       | n/a     | n/a    |
| [aqu\_init](aquifer.aqu/aqu_ini.md)    | Pointer to the aquifer initialization file                                       | string  | n/a       | n/a     | n/a    |
| [gw\_flo](aquifer.aqu/gw_flo.md)       | Initial groundwater flow                                                         | real    | mm        | 0.05    | 0-2    |
| [dep\_bot](aquifer.aqu/dep_bot.md)     | Depth from mid-slope surface to bottom of aquifer                                | real    | m         | 10.0    | 0-10   |
| [dep\_wt](aquifer.aqu/dep_wt-1.md)     | Depth from mid-slope surface to initial water table                              | real    | m         | 10.0    | 0-10   |
| [no3\_n](aquifer.aqu/no3_n.md)         | NO3-N concentration in aquifer                                                   | real    | ppm NO3-N | 0       | 0-1000 |
| [sol\_p](aquifer.aqu/sol_p.md)         | Mineral P concentration in aquifer                                               | real    | mg P/L    | 0       | 0-1000 |
| [carbon](aquifer.aqu/ptl_n.md)         | Organic carbon in aquifer                                                        | real    | percent   | 0.50    | 0-15   |
| [flo\_dist](aquifer.aqu/ptl_p.md)      | Average flow distance to stream or object                                        | real    | m         | 50.0    | 0-1000 |
| [flo\_max](aquifer.aqu/flo_max.md)     | Baseflow rate at which all streams linked to an aquifer receive groundwater flow | real    | mm        | 1.0     | 0-2    |
| [alpha\_bf](aquifer.aqu/alpha_bf.md)   | Alpha factor for groundwater recession curve                                     | real    | 1/days    | 0.05    | 0-1    |
| [revap](aquifer.aqu/revap.md)          | Groundwater revap coefficient                                                    | real    | fraction  | 0       | 0-1    |
| [rchg\_dp](aquifer.aqu/rchg_dp.md)     | Recharge to deep aquifer                                                         | real    | fraction  | 0       | 0-1    |
| [spec\_yld](aquifer.aqu/spec_yld.md)   | Specific yield of the aquifer                                                    | real    | m^3/m^3   | 0       | 0-0.40 |
| [hl\_no3](aquifer.aqu/hl_no3n.md)      | Half-life of NO3-N in the aquifer                                                | real    | days      | 0       | 0-200  |
| [flo\_min](aquifer.aqu/flo_min.md)     | Threshold depth from surface to water table for groundwater flow to occur        | real    | m         | 3       | 0-10   |
| [revap\_min](aquifer.aqu/revap_min.md) | Threshold depth from surface to water table for revap to occur                   | real    | m         | 5       | 0-10   |

Last updated 1 year ago
