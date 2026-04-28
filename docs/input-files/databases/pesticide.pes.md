# pesticide.pes

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/databases/pesticide.pes -->

| Field                                                                        | Description                                                            | Type   | Unit           | Default | Range           |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------ | -------------- | ------- | --------------- |
| [name](pesticide.pes/name_pestdb.md)          | Name of the pesticide record                                           | string | n/a            | n/a     | n/a             |
| [soil\_ads](pesticide.pes/soil_ads.md)        | Soil adsorption coefficient normalized for soil organic carbon content | real   | (mg/kg)/(mg/L) | 0.0     | 1.0-999999999.0 |
| [frac\_wash](pesticide.pes/frac_wash.md)      | Fraction of pesticide on foliage that is washed off by rainfall event  | real   | fraction       | 0.0     | 0.0-1.0         |
| [hl\_foliage](pesticide.pes/hl_foliage.md)    | Half-life of the pesticide on the foliage                              | real   | days           | 0.0     | 0.0-10000.0     |
| [hl\_soil](pesticide.pes/hl_soil.md)          | Half-life of the pesticide in the soil                                 | real   | days           | 0.0     | 0.0-100000.0    |
| [solub](pesticide.pes/solub.md)               | Solubility of the pesticide in water                                   | real   | mg/L (ppm)     | 0.0     |                 |
| [aq\_reac](pesticide.pes/aq_reac.md)          | Aquatic pesticide reaction coefficient                                 | real   | 1/day          | 0.0     |                 |
| [aq\_volat](pesticide.pes/aq_volat.md)        | Aquatic volatilization coefficient                                     | real   | m/day          | 0.0     |                 |
| [mol\_wt](pesticide.pes/mol_wt.md)            | Molecular weight to calculate mixing velocity                          | real   | g/mol          | 0.0     |                 |
| [aq\_resus](pesticide.pes/aq_resus.md)        | Aquatic resuspension velocity for pesticide sorbed to sediment         | real   | m/day          | 0.0     |                 |
| [aq\_settle](pesticide.pes/aq_settle.md)      | Aquatic settling velocity for pesticide sorbed to sediment             | real   | m/day          | 0.0     |                 |
| [ben\_act\_dep](pesticide.pes/ben_act_dep.md) | Depth of the active benthic layer                                      | real   | m/day          | 0.0     |                 |
| [ben\_bury](pesticide.pes/ben_bury.md)        | Burial velocity in the benthic sediment                                | real   | m/day          | 0.0     |                 |
| [ben\_reac](pesticide.pes/ben_reac.md)        | Reaction coefficient in the benthic sediment                           | real   | 1/day          | 0.0     |                 |

Last updated 1 year ago
