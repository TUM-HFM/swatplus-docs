# Plant and Weather

<!-- Source: https://swatplus.gitbook.io/io-docs/swat+-output-files/plant-and-weather -->

Plant and weather output can be printed at basin, LSU, HRU, and HRU-lte level by entering "y" in the *basin\_wb*, *lsunit\_wb*, *hru\_wb*, and *hru-lte\_wb* lines in [**print.prt**](../input-files/simulation-settings/print.prt.md), respectively. Plant and weather output can be printed at daily, monthly, yearly, and average annual time steps. The names of the plant and weather output files are as follows:

- basin\_pw\_day.txt
- basin\_pw\_mon.txt
- basin\_pw\_yr.txt
- basin\_pw\_aa.txt
- lsunit\_pw\_day.txt
- lsunit\_pw\_mon.txt
- lsunit\_pw\_yr.txt
- lsunit\_pw\_aa.txt
- hru\_pw\_day.txt
- hru\_pw\_mon.txt
- hru\_pw\_yr.txt
- hru\_pw\_aa.txt
- hru-lte\_pw\_day.txt
- hru-lte\_pw\_mon.txt
- hru-lte\_pw\_yr.txt
- hru-lte\_pw\_aa.txt

We are aware that the current SWAT+ revision does no print average wind speed and relative humidity correctly. This has been fixed and the correct values will be printed by the new revision to be released in late September.

| **Field** | **Description**                                      | **Unit**    |
| --------- | ---------------------------------------------------- | ----------- |
| jday      | Julian day                                           | n/a         |
| mon       | Month                                                | n/a         |
| day       | Day of the month                                     | n/a         |
| yr        | Year                                                 | n/a         |
| unit      | ID of the object                                     | n/a         |
| gis\_id   | Object ID in GIS                                     | n/a         |
| name      | Name of the object or SWAT+ setup (basin outputs)    | n/a         |
| lai       | Average leaf area index                              | m2/m2       |
| bioms     | Average total plant biomass                          | kg/ha       |
| yield     | Harvested biomass yield (dry weight)                 | kg/ha       |
| residue   | Average residue on surface                           | kg/ha       |
| sol\_tmp  | Average temperature of soil layer 2                  | deg C       |
| strsw     | Water stress                                         | n/a         |
| strsa     | Aeration stress                                      | n/a         |
| strstmp   | Temperature stress                                   | n/a         |
| strsn     | Nitrogen stress                                      | n/a         |
| strsp     | Phosphorus stress                                    | n/a         |
| nplt      | Plant uptake of nitrogen                             | kg/ha       |
| percn     | Nitrate nitrogen leached from bottom of soil profile | kg/ha       |
| pplnt     | Plant uptake of phosphorus                           | kg/ha       |
| tmx       | Average maximum temperature                          | deg C       |
| tmn       | Average minimum temperature                          | deg C       |
| tmpav     | Average mean temperature                             | deg C       |
| solarad   | Average solar radiation                              | mJ/m2       |
| wndspd    | Average wind speed                                   | m/s         |
| rhum      | Average relative humidity                            | frac        |
| phubas0   | Base zero potential heat units                       | deg C/deg C |
| lai\_max  | Maximum leaf area index                              | m2/m2       |
| bm\_max   | Maximum total plant biomass                          | kg/ha       |
| bm\_grow  | Total plant biomass growth                           | kg/ha       |
| c\_gro    | Total plant carbon growth                            | kg/ha       |

Last updated 3 years ago
