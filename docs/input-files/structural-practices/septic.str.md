# septic.str

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/structural-practices/septic.str -->

Data contained in the septic.str data file are: type of septic system, geometry of biozone, characteristics of biomass, and bio-physical reaction coefficients occurring in the biozone (adapted from Siegrist et al. (2005)).

| Field                                                                               | Description                                                                                                | Type    | Unit         | Default | Range    |
| ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------- | ------------ | ------- | -------- |
| [name](septic.str/name_sepdb.md)          | Name of septic system record                                                                               | string  | n/a          | n/a     | n/a      |
| [typ](septic.str/typ.md)                  | Septic system type                                                                                         | integer | n/a          | 0       |          |
| [yr](septic.str/yr.md)                    | ​Year the septic system became operational                                                                 | integer | n/a          | 0       |          |
| [operation](septic.str/operation.md)      | ​Septic system operation flag                                                                              | integer | n/a          | 0       | 0-2      |
| [residents](septic.str/residents.md)      | ​Number of permanent residents in the house                                                                | real    | n/a          | 1       | 1.0-12.0 |
| [area](septic.str/area.md)                | ​Average area of drainfield of individual septic systems                                                   | real    | m^2          | 1       |          |
| [t\_fail](septic.str/t_fail.md)           | Time until failing systems gets fixed                                                                      | integer | days         | 0       | 0-150    |
| [dp\_bioz](septic.str/dp_bioz.md)         | Depth to the top of the biozone layer from the ground surface                                              | real    | mm           | 1       |          |
| [thk\_bioz](septic.str/thk_bioz.md)       | Thickness of biozone layer                                                                                 | real    | mm           | 1       |          |
| [cha\_dist](septic.str/cha_dist.md)       | Distance from septic system to the stream                                                                  | real    | km           | 2       |          |
| [sep\_dens](septic.str/sep_dens.md)       | Number of septic systems per square kilometer                                                              | real    | n/a          | 2       |          |
| [bm\_dens](septic.str/bm_dens.md)         | Density of biomass                                                                                         | real    | kg/m^3       | 1       |          |
| [bod\_decay](septic.str/bod_decay.md)     | BOD decay rate coefficient                                                                                 | real    | m^3/day      | 2       |          |
| [bod\_conv](septic.str/bod_conv.md)       | Conversion factor representing the proportion of mass bacterial growth and mass BOD degraded in the septic | real    | n/a          | 2       |          |
| [fc\_lin](septic.str/fc_lin.md)           | Linear coefficient for calculation of field capacity in the biozone                                        | real    | n/a          | 1       |          |
| [fc\_exp](septic.str/fc_exp.md)           | Exponential coefficient for calculation of field capacity in the biozone                                   | real    | n/a          | 2       |          |
| [fecal\_delay](septic.str/fecal_decay.md) | Fecal coliform bacteria decay rate coefficient                                                             | real    | m^3/day      | 2       |          |
| [tds\_conv](septic.str/tds_conv.md)       | Conversion factor for plaque from TDS                                                                      | real    | n/a          | 2       |          |
| [mort](septic.str/mort.md)                | Mortality rate coefficient                                                                                 | real    | n/a          | 2       |          |
| [resp](septic.str/resp.md)                | Respiration rate coefficient                                                                               | real    | n/a          | 3       |          |
| [slough1](septic.str/slough1.md)          | Linear coefficient for calculating the rate of biomass sloughing                                           | real    | n/a          | 2       |          |
| [slough2](septic.str/slough2.md)          | Exponential coefficient for calculating the rate of biomass sloughing                                      | real    | n/a          | 2       |          |
| [nit](septic.str/nit.md)                  | Nitrification rate coefficient                                                                             | real    | n/a          | 2       |          |
| [denit](septic.str/denit.md)              | Denitrification rate coefficient                                                                           | real    | n/a          | 3       |          |
| [p\_sorp](septic.str/p_sorp.md)           | Linear P sorption distribution coefficient                                                                 | real    | L/kg         | 1       |          |
| [p\_sorp\_max](septic.str/p_sorp_max.md)  | Maximum P sorption capacity                                                                                | real    | mg P/kg soil | 1       |          |
| [solp\_slp](septic.str/solp_slp.md)       | Slope of the linear effluent soluble P equation                                                            | real    | n/a          | 3       |          |
| [solp\_int](septic.str/solp_init.md)      | Intercept of the linear effluent soluble P equation                                                        | real    | n/a          | 3       |          |

#### References

> Siegrist, R.L., J. McCray, L. Weintraub, C. Chen, J. Bagdol, P. Lemonds, S. Van Cuyk, K. Lowe, R. Goldstein, and J. Rada (2005): Quantifying Site-Scale Processes and Watershed-Scale Cumulative Effects of Decentralized Wastewater Systems. Project No. WU-HT-00-27. Prepared for the National Decentralized Water Resources Capacity Development Project, Washington University, St. Louis, MO, by the Colorado School of Mines.

Last updated 1 year ago
