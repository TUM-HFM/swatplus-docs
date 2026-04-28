# op_typ

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/landuse-and-management/management.sch/op_typ -->

| Code | Operation                            | Description                                                                                                                                                                  |
| ---- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| pcom | Plant community                      | This operation initializes the plant community in the HRU                                                                                                                    |
| plnt | Planting/beginning of growing season | This operation initializes the growth of a specific land cover/plant type in the HRU                                                                                         |
| harv | Harvest                              | This operation harvests the portion of the plant designated as yield and removes the yield from the HRU, but allows the plant to continue to grow (e.g. hay cuttings)        |
| hvkl | Harvest and kill                     | This operation harvests the portion of the plant designated as yield, removes the yield from the HRU and converts the remaining plant biomass to residue on the soil surface |
| kill | Kill                                 | This operation kills the plant and converts the plant biomass to residue on the soil surface                                                                                 |
| till | Tillage                              | This operation mixes the upper soil layers and redistributes the nutrients/chemicals within those layers                                                                     |
| irrm | Scheduled irrigation                 | This operation applies water to the HRU on the specified day                                                                                                                 |
| fert | Fertilizer application               | This operation adds nutrients to the soil in the specified day                                                                                                               |
| pest | Pesticide application                | This operation applies a pesticide to the plant and/or soil on the specified day                                                                                             |
| graz | Grazing                              | This operation removes plant biomass at a specified rate and allows simultaneous application of manure                                                                       |
| burn | Burning                              | This operation records the biomass, residue and phosphorus that is burned                                                                                                    |
| swep | Street sweeping                      | This operation removes sediment and nutrient build-up on impervious areas in the HRU; can only be used when the urban build-up/wash-off routines are activated for the HRU   |
| skip | Skipping                             | This operation skips to the end of the year                                                                                                                                  |

Last updated 1 year ago
