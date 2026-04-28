# snow.sno

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/hydrology/snow.sno -->

| Field                                                              | Description                                       | Type   | Unit          | Default | Range     |
| ------------------------------------------------------------------ | ------------------------------------------------- | ------ | ------------- | ------- | --------- |
| [name](snow.sno/name.md)            | Name of the snow record                           | string | n/a           | n/a     | n/a       |
| [fall\_tmp](snow.sno/fall_tmp.md)   | Snowfall temperature                              | real   | ºC            | 1       | -5 - 5    |
| [melt\_tmp](snow.sno/melt_tmp.md)   | Snow melt base temperature                        | real   | ºC            | 0.5     | -5 - 5    |
| [melt\_max](snow.sno/melt_max.md)   | Melt factor for snow on June 21                   | real   | mm H2O/day-ºC | 0.0     | 0.0-10.0  |
| [melt\_min](snow.sno/melt_min.md)   | Melt factor for snow on December 21               | real   | mm H2O/day-ºC | 0.0     | 0.0-10.0  |
| [tmp\_lag](snow.sno/tmp_lag.md)     | Snowpack temperature lag factor                   | real   | none          | 1       | 0.01-1    |
| [snow\_h2o](snow.sno/snow_h2o.md)   | Minimum snow water content                        | real   | mm            | 0.0     | 0.0-500.0 |
| [cov50](snow.sno/cov50.md)          | Fraction of snow                                  | real   | fraction      | 0.50    | 0.0-1.0   |
| [snow\_init](snow.sno/snow_init.md) | Initial snow water content at start of simulation | real   | mm            | 0.0     | 0.0-0.50  |

Last updated 1 year ago
