# plants.plt

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/databases/plants.plt -->

| Field                                                                       | Description                                                                                                     | Type    | Unit             | Default | Range         |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------- | ---------------- | ------- | ------------- |
| [name](plants.plt/untitled.md)               | Name of the plant/landcover                                                                                     | ​string | ​n/a             | n/a     | n/a           |
| [plnt\_typ](plants.plt/untitled-21.md)       | Plant/landcover type                                                                                            | ​string | n/a              | n/a     | n/a           |
| [gro\_trig](plants.plt/untitled-20.md)       | Phenology trigger                                                                                               | string  | n/a              | n/a     | n/a           |
| [nfix\_co](plants.plt/untitled-19.md)        | Nitrogen fixation coefficient                                                                                   | real​   | none             | 0.0     | n/a           |
| [days\_mat](plants.plt/untitled-18.md)       | Days to maturity                                                                                                | real    | days             | 110.0   | 0.0-300.0     |
| [bm\_e](plants.plt/untitled-17.md)           | Biomass-energy ratio                                                                                            | real    | (kg/ha/(MJ/m^2)  | 15.0    | 10.0-90.0     |
| [harv\_idx](plants.plt/untitled-16.md)       | Harvest index for optimal growth conditions                                                                     | real    | (kg/ha)/(kg/ha)  | 0.76    | 0.01-1.25     |
| [lai\_pot](plants.plt/untitled-15.md)        | Maximum potential leaf area index                                                                               | real    | none             | 5.0     | 0.50-10.0     |
| [frac\_hu1](plants.plt/untitled-14.md)       | Fraction of the growing season heat units corresponding to the 1st point on optimal leaf area development curve | real    | fraction         | 0.05    | 0.0-1.0       |
| [lai\_max1](plants.plt/untitled-13.md)       | Fraction of the maximum leaf area index corresponding to the 1st point on optimal leaf area development curve   | real    | fraction         | 0.05    | 0.0-1.0       |
| [frac\_hu2](plants.plt/untitled-12.md)       | Fraction of the growing season heat units corresponding to the 2nd point on optimal leaf area development curve | real    | fraction         | 0.40    | 0.0-1.0       |
| [lai\_max2](plants.plt/untitled-11.md)       | Fraction of the maximum leaf area index corresponding to the 2nd point on optimal leaf area development curve   | real    | fraction         | 0.95    | 0.0-1.0       |
| [hu\_lai\_decl](plants.plt/untitled-10.md)   | Fraction of growing season when leaf area begins to decline                                                     | real    | fraction         | 0.99    | 0.2-1.0       |
| [dlai\_rate](plants.plt/untitled-9.md)       | Exponent that governs the LAI decline rate                                                                      | real    | n/a              | 1.0     |               |
| [can\_ht\_max](plants.plt/untitled-8.md)     | Maximum canopy height                                                                                           | real    | m                | 6.0     | 0.1-20.0      |
| [rt\_dp\_max](plants.plt/untitled-7.md)      | Maximum rooting depth                                                                                           | real    | m                | 3.50    | 0.0-3.0       |
| [tmp\_opt](plants.plt/untitled-6.md)         | Optimal temperature for plant growth                                                                            | real    | deg c            | 30.0    | 11.0-38.0     |
| [tmp\_base](plants.plt/tmp_base.md)          | Minimum temperature for plant growth                                                                            | real    | deg c            | 10.0    | 0.0-18.0      |
| [frac\_n\_yld](plants.plt/frac_n_yld.md)     | Normal fraction of N in yield                                                                                   | real    | kg N/kg yield    | 0.0015  | 0.0015-0.075  |
| [frac\_p\_yld](plants.plt/frac_p_yld.md)     | Normal fraction of P in yield                                                                                   | real    | kg P/kg yield    | 0.0003  | 0.0015-0.0075 |
| [frac\_n\_em](plants.plt/frac_n_em.md)       | Normal fraction of N in plant biomass at emergence                                                              | real    | kg N/kg biomass  | 0.006   | 0.004-0.07    |
| [frac\_n\_50](plants.plt/frac_n_50.md)       | Normal fraction of N in plant biomass at 50% maturity                                                           | real    | kg N/kg biomass  | 0.002   | 0.002-0.05    |
| [frac\_n\_mat](plants.plt/frac_n_mat.md)     | Normal fraction of N in plant biomass at maturity                                                               | real    | kg N/kg biomass  | 0.0015  | 0.001-0.27    |
| [frac\_p\_em](plants.plt/frac_p_em.md)       | Normal fraction pf P in plant biomass at emergence                                                              | real    | kg P/kg biomass  | 0.0007  | 0.0005-0.01   |
| [frac\_p\_50](plants.plt/frac_p_50.md)       | Normal fraction of P in plant at 50% maturity                                                                   | real    | kg P/kg biomass  | 0.0004  | 0.0002-0.007  |
| [frac\_p\_mat](plants.plt/frac_p_mat.md)     | Normal fraction of P in plant at maturity                                                                       | real    | kg P/kg biomass  | 0.0003  | 0.0003-0.0004 |
| [harv\_idx\_ws](plants.plt/harv_idx_ws.md)   | Harvest index that represents the lowest harvest index expected due to water stress                             | real    | (kg/ha)/(kg/ha)  | 0.01    | -0.2-1.1      |
| [usle\_c\_min](plants.plt/usle_c_min.md)     | Minimum value of the USLE C factor for water erosion                                                            | real    | none             | 0.001   | 0.001-0.50    |
| [stcon\_max](plants.plt/stcon_max.md)        | Maximum stomatal conductance                                                                                    | real    | m/s              | 0.002   | 0.0-0.50      |
| [vpd](plants.plt/vpd.md)                     | Vapor pressure deficit corresponding to the 2nd point on the stomatal conductance curve                         | real    | kPa              | 4.0     | 1.5-6.0       |
| [frac\_stcon](plants.plt/frac_stcon.md)      | Fraction of maximum stomatal conductance corresponding to the 2nd point on the stomatal conductance curve       | read    | fraction         | 0.75    | 0.0-1.0       |
| [ru\_vpd](plants.plt/ru_vpd.md)              | Rate of decline in radiation use efficiency per unit increase in vapor pressure deficit                         | real    | none             | 8.0     | 0.0-50.0      |
| [co2\_hi](plants.plt/co2_hi.md)              | Elevated CO2 atmospheric concentration corresponding the 2nd point on the radiation use efficiency curve        | real    | μL CO2/L air     | 660.0   | 300.0-1000.0  |
| [bm\_e\_hi](plants.plt/bm_e_hi.md)           | Biomass-energy ratio corresponding to the 2nd point on the radiation use efficiency curve                       | real    | (kg/ha)/(MJ/m^2) | 16.0    | 5.0-100.0     |
| [plnt\_decomp](plants.plt/plnt_decomp.md)    | Plant residue decomposition coefficient                                                                         | real    | none             | 0.05    | 0.01-0.099    |
| [lai\_min](plants.plt/lai_min.md)            | Minimum LAI during dormant period                                                                               | real    | m^2/m^2          | 0.75    | 0.00-0.99     |
| [bm\_tree\_acc](plants.plt/bm_tree_acc.md)   | Fraction of biomass accumulated each year                                                                       | real    | fraction         | 0.30    | 0.0-1.0       |
| [yrs\_mat](plants.plt/yrs_mat.md)            | Years to maturity                                                                                               | integer | years            | 10      | 0-100         |
| [bm\_tree\_max](plants.plt/bm_tree_max.md)   | Maximum forest biomass                                                                                          | real    | metric tons/ha   | 1000.0  | 0.0-5000.0    |
| [ext\_co](plants.plt/ext_co.md)              | Light extinction coefficient                                                                                    | real    | none             | 0.65    | 0.0-2.0       |
| [leaf\_tov\_min](plants.plt/leaf_tov_min.md) | Perennial leaf turnover rate with minimum stress                                                                | real    |                  | 12.0    |               |
| [leaf\_tov\_max](plants.plt/leaf_tov_max.md) | Perennial leaf turnover rate with maximum stress                                                                | real    |                  | 3.0     |               |
| [bm\_dieoff](plants.plt/bm_dieoff.md)        | Above-ground biomass that dies off at dormancy                                                                  | real    | fraction         | 1.0     | 0.0-1.0       |
| [rt\_st\_beg](plants.plt/rt_st_beg.md)       | Root to shoot ratio at the beginning of the growing season                                                      | real    | fraction         | 0.      |               |
| [rt\_st\_end](plants.plt/rt_st_end.md)       | Root to shoot ratio at the end of the growing season                                                            | real    | fraction         | 0.      |               |
| [plnt\_pop1](plants.plt/plnt_pop1.md)        | Plant population corresponding to the 1st point on the population LAI curve                                     | real    | plants/m^2       | 0.      |               |
| [frac\_lai1](plants.plt/frac_la1.md)         | Fraction of the maximum leaf area index corresponding to the 1st point on the leaf area development curve       | real    | fraction         | 0.      | 0.0-1.0       |
| [plnt\_pop2](plants.plt/plnt_pop2.md)        | Plant population corresponding to the 2nd point on the population LAI curve                                     | real    | plants/m^2       | 0.0     |               |
| [frac\_lai2](plants.plt/frac_lai2.md)        | Fraction of the maximum leaf area index corresponding to the 2nd point on the leaf area development curve       | real    | fraction         | 0.0     | 0.0-1.0       |
| [frac\_sw\_gro](plants.plt/untitled-5.md)    | Fraction of field capacity to initiate growth of tropical plants during monsoon season                          | real    | fraction         | 0.5     | 0.0-1.0       |
| [aeration](plants.plt/untitled-4.md)         | Aeration stress factor                                                                                          | real    |                  | 0.0     |               |
| [rsd\_pctcov](plants.plt/untitled-3.md)      | Residue factor for percent cover equation                                                                       | real    |                  | 0.0     |               |
| [rsd\_covfac](plants.plt/untitled-2.md)      | Residue factor for surface cover (C factor) equation                                                            | real    |                  | 0.0     |               |

Last updated 1 year ago
