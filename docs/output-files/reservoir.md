# Reservoir

<!-- Source: https://swatplus.gitbook.io/io-docs/swat+-output-files/reservoir -->

The printing of reservoir output is controlled by entering "y" or "n" in the *reservoir* line in [print.prt](../input-files/simulation-settings/print.prt.md). In addition, a basin average of all reservoirs can be printed by entering "y" in the *basin\_res* line in [print.prt](../input-files/simulation-settings/print.prt.md). Reservoir output can be printed at daily, monthly, yearly, and average annual time steps. The names of the reservoir output files are as follows:

- reservoir\_day.txt
- reservoir\_mon.txt
- reservoir\_yr.txt
- reservoir\_aa.txt
- basin\_res\_day.txt
- basin\_res\_mon.txt
- basin\_res\_yr.txt
- basin\_res\_aa.txt

| **Field**  | **Description**                                                 | **Unit** |
| ---------- | --------------------------------------------------------------- | -------- |
| jday       | Julian Day                                                      | n/a      |
| mon        | Month                                                           | n/a      |
| day        | Day of the month                                                | n/a      |
| yr         | Year                                                            | n/a      |
| unit       | ID of the object                                                | n/a      |
| gis\_id    | Object ID in GIS                                                | n/a      |
| name       | Name of the object or SWAT+ setup (basin outputs)               | n/a      |
| area       | Area of the reservoir                                           | ha       |
| precip     | Precipitation on the reservoir surface                          | ha-m     |
| evap       | Evaporation from the reservoir surface                          | ha-m     |
| seep       | Seepage out of the reservoir bottom                             | ha-m     |
| flo\_stor  | Flow storage in the reservoir                                   | m3       |
| sed\_stor  | Sediment storage in the reservoir                               | tons     |
| orgn\_stor | Organic nitrogen storage in the reservoir                       | kg       |
| sedp\_stor | Sediment phosphorus storage in the reservoir                    | kg       |
| no3\_stor  | Nitrate nitrogen storage in the reservoir                       | kg       |
| solp\_stor | Soluble phosphorus storage in the reservoir                     | kg       |
| chla\_stor | Chlorophyll-a storage in the reservoir                          | kg       |
| nh3\_stor  | Ammonia nitrogen storage in the reservoir                       | kg       |
| no2\_stor  | Nitrite nitrogen storage in the reservoir                       | kg       |
| cbod\_stor | Carbonaceous Biochemical Oxygen Demand storage in the reservoir | kg       |
| dox\_stor  | Dissolved oxygen storage in the reservoir                       | kg       |
| san\_stor  | Sand storage in the reservoir                                   | tons     |
| sil\_stor  | Silt storage in the reservoir                                   | tons     |
| cla\_stor  | Clay storage in the reservoir                                   | tons     |
| sag\_stor  | Small aggregate storage in the reservoir                        | tons     |
| lag\_stor  | Large aggregate storage in the reservoir                        | tons     |
| grv\_stor  | Gravel storage in the reservoir                                 | tons     |
| null       |                                                                 |          |
| flo\_in    | Flow into the reservoir                                         | m3       |
| sed\_in    | Sediment entering the reservoir                                 | tons     |
| orgn\_in   | Organic nitrogen entering the reservoir                         | kg       |
| sedp\_in   | Sediment phosphorus entering the reservoir                      | kg       |
| no3\_in    | Nitrate nitrogen entering the reservoir                         | kg       |
| solp\_in   | Soluble phosphorus entering the reservoir                       | kg       |
| chla\_in   | Chlorophyll-a entering the reservoir                            | kg       |
| nh3\_in    | Ammonia nitrogen entering the reservoir                         | kg       |
| no2\_in    | Nitrite nitrogen entering the reservoir                         | kg       |
| cbod\_in   | Carbonaceous Biochemical Oxygen Demand entering the reservoir   | kg       |
| dox\_in    | Dissolved oxygen entering the reservoir                         | kg       |
| san\_in    | Sand entering the reservoir                                     | tons     |
| sil\_in    | Silt entering the reservoir                                     | tons     |
| cla\_in    | Clay entering the reservoir                                     | tons     |
| sag\_in    | Small aggregates entering the reservoir                         | tons     |
| lag\_in    | Large aggregates entering the reservoir                         | tons     |
| grv\_in    | Gravel entering the reservoir                                   | tons     |
| null       |                                                                 |          |
| flo\_out   | Flow out of the reservoir                                       | m3       |
| sed\_out   | Sediment leaving the reservoir                                  | tons     |
| orgn\_out  | Organic nitrogen leaving the reservoir                          | kg       |
| sedp\_out  | Sediment phosphorus leaving the reservoir                       | kg       |
| no3\_out   | Nitrate nitrogen leaving the reservoir                          | kg       |
| solp\_out  | Soluble phosphorus leaving the reservoir                        | kg       |
| chla\_out  | Chlorophyll-a leaving the reservoir                             | kg       |
| nh3\_out   | Ammonia nitrogen leaving the reservoir                          | kg       |
| no2\_out   | Nitrite nitrogen leaving the reservoir                          | kg       |
| cbod\_out  | Carbonaceous Biochemical Oxygen Demand leaving the reservoir    | kg       |
| dox\_out   | Dissolved oxygen leaving the reservoir                          | kg       |
| san\_out   | Sand leaving the reservoir                                      | tons     |
| sil\_out   | Silt leaving the reservoir                                      | tons     |
| cla\_out   | Clay leaving the reservoir                                      | tons     |
| sag\_out   | Small aggregates leaving the reservoir                          | tons     |
| lag\_out   | Large aggregates leaving the reservoir                          | tons     |
| grv\_out   | Gravel leaving the reservoir                                    | tons     |
| null       |                                                                 |          |

Last updated 3 years ago
