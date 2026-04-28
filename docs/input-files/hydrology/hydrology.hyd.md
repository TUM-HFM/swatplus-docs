# hydrology.hyd

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/hydrology/hydrology.hyd -->

| Field                                                                       | Description                                                 | Type   | Unit | Default | Range   |
| --------------------------------------------------------------------------- | ----------------------------------------------------------- | ------ | ---- | ------- | ------- |
| [name](hydrology.hyd/name.md)                | Name of the hydrology record                                | string | n/a  | n/a     | n/a     |
| [lat\_time](hydrology.hyd/lat_time.md)       | Lateral flow travel time                                    | real   | days | 0       | 0-180   |
| [lat\_sed](hydrology.hyd/lat_sed.md)         | Sediment concentration in lateral and groundwater flow      | real   | mg/L | 0       | 0-5000  |
| [can\_max](hydrology.hyd/can_max.md)         | Maximum canopy storage                                      | real   | mm   | 1       | 0-100   |
| [esco](hydrology.hyd/esco.md)                | Soil evaporation compensation factor                        | real   | none | 0.5     | 0.01-1  |
| [epco](hydrology.hyd/epco.md)                | Plant uptake compensation factor                            | real   | none | 0       | 0.01-1  |
| [orgn\_enrich](hydrology.hyd/orgn_enrich.md) | Organic nitrogen enrichment ratio for loading with sediment | real   | none | 0       | 0-1     |
| [orgp\_enrich](hydrology.hyd/orgp_enrich.md) | Phosphorus enrichment ratio for loading with sediment       | real   | none | 0       | 0-1     |
| [cn3\_swf](hydrology.hyd/cn3_swf.md)         | Soil water adjustment factor for CN3                        | real   | none |         | 0-1     |
| [bio\_mix](hydrology.hyd/bio_mix.md)         | Biological mixing efficiency                                | real   |      | 0.2     |         |
| [perco](hydrology.hyd/perco.md)              | Percolation coefficient                                     | real   | none |         | 0-1     |
| [lat\_orgn](hydrology.hyd/lat_orgn.md)       | Organic nitrogen concentration in lateral flow              | real   | mg/L |         | 0-200   |
| [lat\_orgp](hydrology.hyd/lat_orgp.md)       | Organic phosphorus concentration in lateral flow            | real   | mg/L |         | 0-200   |
| [pet\_co](hydrology.hyd/harg_pet.md)         | Linear adjustment factor for PET equations                  | real   | none | 1       | 0.8-1.2 |
| [latq\_co](hydrology.hyd/cn_plntet.md)       | Lateral flow coefficient                                    | real   | none |         | 0-1     |

Last updated 1 year ago
