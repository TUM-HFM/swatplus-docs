# Aquifer

<!-- Source: https://swatplus.gitbook.io/io-docs/swat+-output-files/aquifer -->

The printing of aquifer output is controlled by entering "y" or "n" in the *aquifer* line in [print.prt](../input-files/simulation-settings/print.prt.md). In addition, a basin average of all aquifers can be printed by entering "y" in the *basin\_aqu* line in [print.prt](../input-files/simulation-settings/print.prt.md). Aquifer output can be printed at daily, monthly, yearly, and average annual time steps. The names of the aquifer output files are as follows:

- aquifer\_day.txt
- aquifer\_mon.txt
- aquifer\_yr.txt
- aquifer\_aa.txt
- basin\_aqu\_day.txt
- basin\_aqu\_mon.txt
- basin\_aqu\_yr.txt
- basin\_aqu\_aa.txt

| **Field** | **Description**                                   | **Unit** |
| --------- | ------------------------------------------------- | -------- |
| jday      | Julian Day                                        | n/a      |
| mon       | Month                                             | n/a      |
| day       | Day of the month                                  | n/a      |
| yr        | Year                                              | n/a      |
| unit      | ID of the object                                  | n/a      |
| gis\_id   | Object ID in GIS                                  | n/a      |
| name      | Name of the object or SWAT+ setup (basin outputs) | n/a      |
| flo       | Groundwater flow                                  | mm       |
| dep\_wt   | Depth from surface to aquifer water table         | m        |
| stor      | Aquifer storage                                   | mm       |
| rchrg     | Aquifer recharge                                  | mm       |
| seep      | Seepage out of the aquifer                        | mm       |
| revap     | Revap from the aquifer                            | mm       |
| no3\_st   |                                                   | kg N/ha  |
| minp      | Mineral phosphorus in the groundwater             | kg       |
| orgn      | Organic nitrogen in the groundwater               | kg N/ha  |
| orgp      | Organic phosphorus in the groundwater             | kg P/ha  |
| rchrgn    |                                                   | kg N/ha  |
| nloss     | Nitrogen losses in the aquifer                    | kg N/ha  |
| no3gw     |                                                   | kg N/ha  |
| seepno3   |                                                   | kg       |
| flo\_cha  | Groundwater flow to channels                      | mm       |
| flo\_res  | Groundwater flow to reservoirs                    | mm       |
| flo\_ls   | Groundwater flow to other aquifers                | mm       |

Last updated 3 years ago
