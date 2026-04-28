# Nutrient Balance

<!-- Source: https://swatplus.gitbook.io/io-docs/swat+-output-files/nutrient-balance -->

Nutrient balance output can be printed at basin, LSU, HRU, and HRU-lte level by entering "y" in the *basin\_nb*, *lsunit\_nb*, *hru\_nb*, and *hru-lte\_nb* lines in [print.prt](../input-files/simulation-settings/print.prt.md), respectively. Nutrient balance output can be printed at daily, monthly, yearly, and average annual time steps. The names of the nutrient balance output files are as follows:

- basin\_nb\_day.txt
- basin\_nb\_mon.txt
- basin\_nb\_yr.txt
- basin\_nb\_aa.txt
- lsunit\_nb\_day.txt
- lsunit\_nb\_mon.txt
- lsunit\_nb\_yr.txt
- lsunit\_nb\_aa.txt
- hru\_nb\_day.txt
- hru\_nb\_mon.txt
- hru\_nb\_yr.txt
- hru\_nb\_aa.txt

| **Field**      | **Description**                                                                                           | **Unit** |
| -------------- | --------------------------------------------------------------------------------------------------------- | -------- |
| jday           | Julian day                                                                                                | n/a      |
| mon            | Month                                                                                                     | n/a      |
| day            | Day of the month                                                                                          | n/a      |
| yr             | Year                                                                                                      | n/a      |
| unit           | ID of the object                                                                                          | n/a      |
| gis\_id        | Object ID in GIS                                                                                          | n/a      |
| name           | Name of the object or SWAT+ setup (basin outputs)                                                         | n/a      |
| grzn           | Total nitrogen added to soil from grazing                                                                 | kg/ha    |
| grzp           | Total phosphorus added to soil from grazing                                                               | kg/ha    |
| lab\_min\_p    | Phosphorus moving from the labile mineral pool to the active mineral pool                                 | kg/ha    |
| act\_sta\_p    | Phosphorus moving from the active mineral pool to the stable mineral pool                                 | kg/ha    |
| fertn          | Total nitrogen applied to soil through fertilization                                                      | kg/ha    |
| fertp          | Total phosphorus applied to soil through fertilization                                                    | kg/ha    |
| fixn           | Nitrogen added to plant biomass via fixation                                                              | kg/ha    |
| denit          | Nitrogen lost from nitrate pool by denitrification                                                        | kg/ha    |
| act\_nit\_n    | Nitrogen moving from active organic pool to nitrate pool                                                  | kg/ha    |
| act\_sta\_n    | Nitrogen moving from active organic pool to stable pool                                                   | kg/ha    |
| org\_lab\_p    | Phosphorus moving from the organic pool to labile pool                                                    | kg/ha    |
| rsd\_nitorg\_n | Nitrogen moving from the fresh organic pool (residue) to the nitrate (80%) and active organic (20%) pools | kg/ha    |
| rsd\_laborg\_p | Phosphorus moving from the fresh organic pool (residue) to the labile (80%) and organic (20%) pools       | kg/ha    |
| no3atmo        | Nitrate added to the soil from atmospheric deposition                                                     | kg/ha    |
| nh4atmo        | Ammonia added to the soil from atmospheric deposition                                                     | kg/ha    |
| nuptake        | Plant nitrogen uptake                                                                                     | kg/ha    |
| puptake        | Plant phosphorus uptake                                                                                   | kg/ha    |
| gwtrann        | Nitrate added to the soil from the aquifer (gwflow module)                                                | kg/ha    |
| gwtranp        | Phosphorus added to the soil from the aquifer (gwflow module)                                             | kg/ha    |

Last updated 11 months ago
