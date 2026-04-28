# grassedww.str

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/structural-practices/grassedww.str -->

Grassed waterways are vegetated channels that transport runoff from a field. Vegetation within the waterways reduces flow velocities and protects the waterway from the scouring potential of concentrated flow. Grassed waterways are generally broad and shallow channels; the channel simulated in SWAT+ has a side slope of 8:1. Grassed waterways trap sediment and other contaminants by reducing flow velocities, which increases deposition of particulate contaminates.

| Field                                                                         | Description                         | Type    | Unit | Range       |
| ----------------------------------------------------------------------------- | ----------------------------------- | ------- | ---- | ----------- |
| [name](grassedww.str/name_grwdb.md) | Name of the grassed waterway record | string  | n/a  | n/a         |
| flag\_grww                                                                    | ​Currently not used                 | integer |      |             |
| [mann](grassedww.str/mann.md)       | Manning's n for grassed waterway    | real    | n/a  | 0.001-0.50  |
| [sed\_co](grassedww.str/sed_co.md)  | Sediment transport coefficient      | real    | n/a  | 0.0-1.0     |
| [dp](tiledrain.str/dp.md)           | Depth of grassed waterway           | real    | m    | 0.0-10.0    |
| [wd](grassedww.str/wd.md)           | Width of grassed waterway           | real    | m    | 0.0-1000.0  |
| [len](grassedww.str/len.md)         | Length of grassed waterway          | real    | km   | 0.0-10000.0 |
| [slp](grassedww.str/slp.md)         | Slope of grassed waterway           | real    | m/m  | 0.0-1.0     |

Last updated 1 year ago
