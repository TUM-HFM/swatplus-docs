# Water Balance

<!-- Source: https://swatplus.gitbook.io/io-docs/swat+-output-files/water-balance -->

Water balance output can be printed at basin, LSU, HRU, and HRU-lte level by entering "y" in the *basin\_wb*, *lsunit\_wb*, *hru\_wb*, and *hru-lte\_wb* lines in [print.prt](../input-files/simulation-settings/print.prt.md), respectively. Water balance output can be printed at daily, monthly, yearly, and average annual time steps. The names of the water balance output files are as follows:

- basin\_wb\_day.txt
- basin\_wb\_mon.txt
- basin\_wb\_yr.txt
- basin\_wb\_aa.txt
- lsunit\_wb\_day.txt
- lsunit\_wb\_mon.txt
- lsunit\_wb\_yr.txt
- lsunit\_wb\_aa.txt
- hru\_wb\_day.txt
- hru\_wb\_mon.txt
- hru\_wb\_yr.txt
- hru\_wb\_aa.txt
- hru-lte\_wb\_day.txt
- hru-lte\_wb\_mon.txt
- hru-lte\_wb\_yr.txt
- hru-lte\_wb\_aa.txt

| **Field**   | **Description**                                      | **Unit** |
| ----------- | ---------------------------------------------------- | -------- |
| jday        | Julian day                                           | n/a      |
| mon         | Month                                                | n/a      |
| day         | Day of the month                                     | n/a      |
| yr          | Year                                                 | n/a      |
| unit        | ID of the object                                     | n/a      |
| gis\_id     | Object ID in GIS                                     | n/a      |
| name        | Name of the object or SWAT+ setup (basin outputs)    | n/a      |
| precip      | Precipitation                                        | mm       |
| snofall     | Snowfall                                             | mm       |
| snomlt      | Snowmelt                                             | mm       |
| surq\_gen   | Generated surface runoff                             | mm       |
| latq        | Lateral flow                                         | mm       |
| wateryld    | Water yield                                          | mm       |
| perc        | Percolation                                          | mm       |
| et          | Actual evapotranspiration                            | mm       |
| ecanopy     | Canopy evaporation                                   | mm       |
| eplant      | Plant transpiration                                  | mm       |
| esoil       | Soil evaporation                                     | mm       |
| surq\_cont  | Contributing surface runoff                          | mm       |
| cn          | Curve Number                                         | n/a      |
| sw\_init    | Initial soil water content                           | mm       |
| sw\_final   | Final soil water content                             | mm       |
| sw\_ave     | Average soil water content                           | mm       |
| sw\_300     | Average soil water content in the top 300 mm of soil | mm       |
| sno\_init   | Initial snow water content                           | mm       |
| sno\_final  | Final snow water content                             | mm       |
| snopac      | Average snow water content                           | mm       |
| pet         | Potential Evapotranspiration                         | mm       |
| qtile       | Tile flow                                            | mm       |
| irr         | Irrigation                                           | mm       |
| surq\_runon | Surface runoff run-on                                | mm       |
| latq\_runon | Later flow run-on                                    | mm       |
| overbank    | Overbank flow                                        | mm       |
| surq\_cha   | Surface runoff to channels                           | mm       |
| surq\_res   | Surface runoff to reservoirs                         | mm       |
| surq\_ls    | Surface runoff to Landscape Units                    | mm       |
| latq\_cha   | Lateral flow to channels                             | mm       |
| latq\_res   | Lateral flow to reservoirs                           | mm       |
| latq\_ls    | Lateral flow to Landscape Units                      | mm       |
| gwtranq     | GWFlow module output                                 | mm       |
| satex       | GWFlow module output                                 | mm       |
| satex\_chan | GWFlow module output                                 | mm       |
| sw\_change  | Change in soil water content                         | mm       |
| lagsurf     | Surface runoff lag                                   | mm       |
| laglatq     | Lateral flow runoff lag                              | mm       |
| lagsatex    | Surface runoff lag                                   | mm       |

Last updated 3 years ago
