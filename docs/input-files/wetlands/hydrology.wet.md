# hydrology.wet

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/wetlands/hydrology.wet -->

| Field                                                                       | Description                                                                       | Type   | Unit     | Default | Range |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------ | -------- | ------- | ----- |
| [name](hydrology.wet/name.md)                 | Name of the wetland hydrology record                                              | string | n/a      | n/a     | n/a   |
| [hru\_ps](hydrology.wet/hru_ps.md)            | Fraction of HRU area at principal spillway (when surface inlet riser flow starts) | real   | frac     | 0       |       |
| [dp\_ps](hydrology.wet/dp_ps.md)              | Average depth of water at principal spillway                                      | real   | mm       | 0       |       |
| [hru\_es](hydrology.wet/hru_es.md)            | Fraction of HRU area at emergency spillway (when starts to spill into ditch)      | real   | frac     | 0       |       |
| [dp\_es](hydrology.wet/dp_es.md)              | Average depth of water at emergency spillway                                      | real   | mm       | 0       |       |
| [k](../reservoirs/hydrology.res/k.md)                     | Hydraulic conductivity of the wetland bottom                                      | real   | mm/hr    | 0.01    |       |
| [evap](hydrology.wet/evap.md)                 | Wetland evaporation coefficient                                                   | real   | n/a      | 0.70    |       |
| [vol\_area\_co](hydrology.wet/vol_area_co.md) | Volume surface area coefficient for HRU impoundment                               | real   | n/a      | 1.0     |       |
| [vol\_dp\_a](hydrology.wet/vol_dp_a.md)       | Volume depth coefficient for HRU impoundment                                      | real   | n/a      | 1.0     |       |
| [vol\_dp\_b](hydrology.wet/vol_dp_b.md)       | Volume depth coefficient for HRU impoundment                                      | real   | n/a      | 1.0     |       |
| [hru\_frac](hydrology.wet/hru_frac.md)        | Fraction of HRU that drains into wetland                                          | real   | fraction | 0.5     |       |

Last updated 1 year ago
