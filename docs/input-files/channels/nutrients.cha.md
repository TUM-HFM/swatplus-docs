# nutrients.cha

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/channels/nutrients.cha -->

| Field                                                                         | Description                                                                                            | Type    | Unit                          | Default | Range       |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------- | ----------------------------- | ------- | ----------- |
| [name](nutrients.cha/name.md)                   | Name of the channel nutrient record                                                                    | string  | n/a                           | n/a     | n/a         |
| [plt\_n](nutrients.cha/plt_n.md)                | Channel organic N concentration                                                                        | real    | ppm                           | 0.0     | 0.0-100.0   |
| [plt\_p](nutrients.cha/plt_p.md)                | Channel organic P concentration                                                                        | real    | ppm                           | 0.0     | 0.0-100.0   |
| [alg\_stl](nutrients.cha/alg_stl.md)            | Local algal settling rate in the channel at 20ºC                                                       | real    | m/day or m/hr                 | 1.0     | 0.15-1.82   |
| [ben\_disp](nutrients.cha/ben_disp.md)          | Benthic source rate for dissolved P in the channel at 20ºC                                             | real    | mg P/m2\*day or mg P/m2\*hr   | 0.05    | 0.001-0.10  |
| [ben\_nh3n](nutrients.cha/ben_nh3n.md)          | Benthic source rate for NH3-N in the channel at 20ºC                                                   | real    | mg N/m2\*day or mg N/m2\*hr   | 0.50    | 0.0-1.0     |
| [ptln\_stl](nutrients.cha/ptln_stl.md)          | Organic N settling rate in the channel at 20ºC                                                         | real    | 1/day or 1/hr                 | 0.05    | 0.001-0.1   |
| [ptlp\_stl](nutrients.cha/ptlp_stl.md)          | Organic P settling rate in the channel at 20ºC                                                         | real    | 1/day or 1/hr                 | 0.05    | 0.001-0.10  |
| [cst\_stl](nutrients.cha/cst_stl.md)            | Arbitrary non-conservative constituent settling rate in the channel at 20ºC                            | real    | 1/day                         | 2.50    | 0.01-10.0   |
| [ben\_cst](nutrients.cha/ben_cst.md)            | Benthic source rate for arbitrary non-conservative constituents in the channel at 20ºC                 | real    | mg /m^2\*day                  | 2.50    | 0.01-10.0   |
| [cbn\_bod\_co](nutrients.cha/cbn_bod_co.md)     | Carbonaceous biological oxygen demand deoxygenation rate in the channel at 20ºC                        | real    | 1/day or 1/hr                 | 1.71    | 0.02-3.40   |
| [air\_rt](nutrients.cha/air_rt.md)              | Reaeration rate in accordance with Fickian diffusion in the channel at 20ºC                            | real    | 1/day or 1/hr                 | 50.0    | 0.0-100.0   |
| [cbn\_bod*\_*stl](nutrients.cha/cbn_bod_stl.md) | Rate of loss of CBOD due to settling in the channel at 20ºC                                            | real    | 1/day or 1/hr                 | 0.36    | -0.36-0.36  |
| [ben\_bod](nutrients.cha/ben_bod.md)            | Sediment oxygen demand rate in the channel at 20ºC                                                     | real    | mg O2/m2\*day or mg O2/m2\*hr | 2.0     | 0.0-100.0   |
| [bact\_die](nutrients.cha/bact_die.md)          | Coliform die-off rate in the channel at 20ºC                                                           | real    | 1/day                         | 2.0     | 0.05-4.0    |
| [cst\_decay ](nutrients.cha/cst_decay.md)       | Decay rate for arbitrary non-conservative constituents in the channel at 20ºC                          | real    | 1/day                         | 1.71    | 0.0-10.0    |
| [nh3n\_no2n](nutrients.cha/nh3n_no2n.md)        | Biological oxidation rate of NH3 to NO2 in the channel at 20ºC in well-aerated conditions              | real    | 1/day or 1/hr                 | 0.55    | 0.10-1.0    |
| [no2n\_no3n](nutrients.cha/no2n_no3n.md)        | Biological oxidation rate of NO2 to NO3 in the channel at 20ºC in well-aerated conditions              | real    | 1/day or 1/hr                 | 1.10    | 0.20-2.0    |
| [ptln\_nh3n](nutrients.cha/ptln_nh3n.md)        | Hydrolysis rate of organic N to ammonia in the channel at 20ºC                                         | real    | 1/day or 1/hr                 | 0.21    | 0.20-0.40   |
| [ptlp\_solp](nutrients.cha/ptlp_solp.md)        | Mineralization rate of organic P to dissolved P in the channel at 20ºC                                 | real    | 1/day or 1/hr                 | 0.35    | 0.01-0.70   |
| [q2e\_lt](nutrients.cha/q2e_lt.md)              | Qual2E light averaging option                                                                          | integer | n/a                           | 2       | 1-4         |
| [q2e\_alg](nutrients.cha/q2e_alg.md)            | Qual2E option for calculating the local specific growth rate of algae                                  | integer | n/a                           | 2       | 1-3         |
| [chla\_alg](nutrients.cha/chla_alg.md)          | Ratio of chlorophyll-a to algal biomass                                                                | real    | μg chla/mg alg                | 50.0    | 10.0-100.0  |
| [alg\_n](nutrients.cha/alg_n.md)                | Fraction of algal biomass that is N                                                                    | real    | mg N/mg alg                   | 0.08    | 0.07-0.09   |
| [alg\_p](nutrients.cha/alg_p.md)                | Fraction of algal biomass that is P                                                                    | real    | mg P/mg alg                   | 0.02    | 0.01-0.02   |
| [alg\_o2\_prod](nutrients.cha/alg_o2_prod.md)   | Oxygen production rate per unit of algal photosynthesis                                                | real    | mg O2/mg alg                  | 1.60    | 1.40-1.80   |
| [alg\_o2\_resp](nutrients.cha/alg_o2_resp.md)   | Oxygen uptake rate per unit of algae respiration                                                       | real    | mg O2/mg alg                  | 2.0     | 1.60-2.30   |
| [o2\_nh3n](nutrients.cha/o2_nh3n.md)            | Oxygen uptake rate per unit of NH3-N oxidation                                                         | real    | mg O2/mg N                    | 3.50    | 3.00-4.00   |
| [o2\_no2n](nutrients.cha/o2_no2n.md)            | Oxygen uptake rate per unit of NO2-N oxidation                                                         | real    | mg O2/mg N                    | 1.07    | 1.00-1.40   |
| [alg\_grow](nutrients.cha/alg_grow.md)          | Maximum specific algal growth rate at 20ºC                                                             | real    | 1/day                         | 2.0     | 1.00-3.00   |
| [alg\_resp](nutrients.cha/alg_resp.md)          | Algal respiration rate at 20ºC                                                                         | real    | 1/day or 1/hr                 | 2.50    | 0.05-5.0    |
| [slr\_act](nutrients.cha/slr_act.md)            | Fraction of solar radiation computed in the temperature heat balance that is photosynthetically active | real    | fraction                      | 0.30    | 0.0-1.0     |
| [lt\_co](nutrients.cha/lt_co.md)                | Half-saturation coefficient for light                                                                  | real    | MJ/(m^2\*hr)                  | 0.75    | 0.223-1.135 |
| [const\_n](nutrients.cha/const_n.md)            | Michaelis-Menton half-saturation constant for N                                                        | real    | mg N/L                        | 0.02    | 0.01-0.30   |
| [const\_p](nutrients.cha/const_p.md)            | Michaelis-Menton half saturation constant for P                                                        | real    | mg P/L                        | 0.03    | 0.001-0.05  |
| [lt\_nonalg](nutrients.cha/lt_nonalg.md)        | Non-algal portion of the light extinction coefficient                                                  | real    | 1/m                           | 1.0     | 0.0-10.0    |
| [alg\_shd\_l](nutrients.cha/alg_shd_l.md)       | Linear algal self-shading coefficient                                                                  | real    | 1/(m\*ug chla/L)              | 0.03    | 0.006-0.065 |
| [alg\_shd\_nl](nutrients.cha/alg_shd_nl.md)     | Nonlinear algal self-shading coefficient                                                               | real    | (1/m)(ug chla/L)^(-2/3)       | 0.05    | 0.0-1.0     |
| [nh3\_pref](nutrients.cha/nh3_pref.md)          | Algal preference factor for ammonia                                                                    | real    | none                          | 0.50    | 0.0-1.0     |

Last updated 1 year ago
