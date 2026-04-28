# hyd-sed-lte.cha

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/channels/hyd-sed-lte.cha -->

| Field                                                                    | Description                                                   | Type   | Unit     | Default              | Range |
| ------------------------------------------------------------------------ | ------------------------------------------------------------- | ------ | -------- | -------------------- | ----- |
| [name](hyd-sed-lte.cha/name.md)            | Name of the channel hydrology and sediment record             | string | n/a      | n/a                  | n/a   |
| [wd](hyd-sed-lte.cha/wd.md)                | Channel width                                                 | real   | m        | calculated by QSWAT+ |       |
| [dp](hyd-sed-lte.cha/dp.md)                | Channel depth                                                 | real   | m        | calculated by QSWAT+ |       |
| [slp](hyd-sed-lte.cha/slp.md)              | Channel slope                                                 | real   | m/m      | calculated by QSWAT+ |       |
| [len](hyd-sed-lte.cha/len.md)              | Channel length                                                | real   | km       | calculated by QSWAT+ |       |
| [mann](hyd-sed-lte.cha/mann.md)            | Channel Manning's n value                                     | real   | none     | 0.05                 |       |
| [k](hyd-sed-lte.cha/k.md)                  | Effective hydraulic conductivity of the channel alluvium      | real   | mm/h     | 1.0                  |       |
| [erod\_fact](hyd-sed-lte.cha/erod_fact.md) | Channel erodibility factor                                    | real   | none     | 0.01                 |       |
| [cov\_fact](hyd-sed-lte.cha/cov_fact.md)   | Channel cover factor                                          | real   | none     | 0.01                 | 0-1   |
| [sinu](hyd-sed-lte.cha/wd_rto.md)          | Channel sinuosity                                             | real   | none     | 6.0                  |       |
| [eq\_slp](hyd-sed-lte.cha/eq_slp.md)       | Equilibrium channel slope                                     | real   | m/m      | 0                    |       |
| [d50](hyd-sed-lte.cha/d50.md)              | Channel median sediment size                                  | real   | mm       | 12.0                 |       |
| [clay](hyd-sed-lte.cha/clay.md)            | Clay content of channel bank and bed                          | real   | %        | 50.00                | 0-100 |
| [carbon](hyd-sed-lte.cha/carbon.md)        | Carbon content of channel bank and bed                        | real   | %        | 0                    | 0-100 |
| [dry\_bd](hyd-sed-lte.cha/dry_bd.md)       | Dry bulk density of the channel                               | real   | t/m3     | 0                    |       |
| [side\_slp](hyd-sed-lte.cha/side_slp.md)   | Channel side slope                                            | real   | m        | 0.50                 |       |
| [bed\_load](hyd-sed-lte.cha/bed_load.md)   | Percent of sediment entering the channel that is bed material | real   | m        | 0.50                 |       |
| [fps](hyd-sed-lte.cha/fps.md)              | Floodplain slope                                              | real   | m/m      | 10.0                 |       |
| [fpn](hyd-sed-lte.cha/fpn.md)              | Floodplain Manning's n                                        | real   | none     |                      |       |
| [n\_conc](hyd-sed-lte.cha/hc_erod.md)      | Nitrogen concentration in channel bank                        | real   | mg/kg    | 0.10                 |       |
| [p\_conc](hyd-sed-lte.cha/hc_ht.md)        | Phosphorus concentration in channel bank                      | real   | mg/kg    | 0.30                 |       |
| [p\_bio](hyd-sed-lte.cha/hc_len.md)        | Fraction of phosphorus in bank that is bioavailable           | real   | fraction | 0.30                 |       |

Last updated 1 year ago
