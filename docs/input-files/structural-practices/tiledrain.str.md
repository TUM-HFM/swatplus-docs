# tiledrain.str

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/structural-practices/tiledrain.str -->

Tile drains remove excess water from an area to optimize plant growth.

| Field                                                                            | Description                                                                 | Type    | Unit   | Default | Range       |
| -------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------- | ------ | ------- | ----------- |
| [name](tiledrain.str/name_tiledb.md)   | Name of the tiledrain record                                                | ​string | n/a    | n/a     | n/a         |
| [dp](tiledrain.str/dp.md)              | ​Depth of drain tube from the soil surface                                  | ​real   | ​mm    | ​1000.0 | ​0.0-6000.0 |
| [t\_fc](tiledrain.str/t_fc.md)         | Time to drain soil to field capacity                                        | real    | ​hours | ​48.00  | ​0.0-100.0  |
| [lag](tiledrain.str/lag.md)            | ​Drain tile lag time                                                        | ​real   | ​hours | ​24.00  | ​0.0-100.0  |
| [rad](tiledrain.str/rad.md)            | ​Effective radius of drains                                                 | real    | ​mm    | 30.0    | 3.0-40.0    |
| [dist](tiledrain.str/dist.md)          | ​Distance between two drain tubes or tiles                                  | real    | m      | 5.0     | ​5.0-100.0  |
| [drain](tiledrain.str/drain.md)        | Drainage coefficient                                                        | real    | mm/day | 10.0    | 10.0-51.0   |
| [pump](tiledrain.str/pump.md)          | Pump capacity                                                               | real    | mm/hr  | 1.0     | 0.0-10.0    |
| [lat\_ksat](tiledrain.str/lat_ksat.md) | Multiplication factor to determine lateral saturated hydraulic conductivity | real    | none   | 1.0     | 0.01-4.00   |

Last updated 1 year ago
