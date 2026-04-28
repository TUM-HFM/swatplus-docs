# Channel

<!-- Source: https://swatplus.gitbook.io/io-docs/swat+-output-files/channel -->

SWAT+ prints two channel output files per time step, one for general channel output and one for channel morphology output. The printing of channel output is controlled by entering "y" or "n" in the *channel\_sd* line in [print.prt](../input-files/simulation-settings/print.prt.md). In addition, a basin average of all channels can be printed by entering "y" in the *basin\_sd\_cha* line in [print.prt](../input-files/simulation-settings/print.prt.md). Channel output can be printed at daily, monthly, yearly, and average annual time steps. The names of the channel output files are as follows:

- channel\_sd\_day.txt
- channel\_sd\_mon.txt
- channel\_sd\_yr.txt
- channel\_sd\_aa.txt
- channel\_sdmorph\_day.txt
- channel\_sdmorph\_mon.txt
- channel\_sdmorph\_yr.txt
- channel\_sdmorph\_aa.txt
- basin\_sd\_cha\_day.txt
- basin\_sd\_cha\_mon.txt
- basin\_sd\_cha\_yr.txt
- basin\_sd\_cha\_aa.txt
- basin\_sd\_chamorph\_day.txt
- basin\_sd\_chamorph\_mon.txt
- basin\_sd\_chamorph\_yr.txt
- basin\_sd\_chamorph\_aa.txt

General

Morphology

| **Field**  | **Description**                                               | **Unit** |
| ---------- | ------------------------------------------------------------- | -------- |
| jday       | Julian Day                                                    | n/a      |
| mon        | Month                                                         | n/a      |
| day        | Day of the month                                              | n/a      |
| yr         | Year                                                          | n/a      |
| unit       | ID of the object                                              | n/a      |
| gis\_id    | Object ID in GIS                                              | n/a      |
| name       | Name of the object or SWAT+ setup (basin outputs)             | n/a      |
| area       | Area of the channel                                           | ha       |
| precip     | Precipitation on the channel surface                          | ha-m     |
| evap       | Evaporation from the channel surface                          | ha-m     |
| seep       | Seepage out of the channel bottom                             | ha-m     |
| flo\_stor  | Flow storage in the channel                                   | m3       |
| sed\_stor  | Sediment storage in the channel                               | tons     |
| orgn\_stor | Organic nitrogen storage in the channel                       | kg       |
| sedp\_stor | Sediment phosphorus storage in the channel                    | kg       |
| no3\_stor  | Nitrate nitrogen storage in the channel                       | kg       |
| solp\_stor | Soluble phosphorus storage in the channel                     | kg       |
| chla\_stor | Chlorophyll-a storage in the channel                          | kg       |
| nh3\_stor  | Ammonia nitrogen storage in the channel                       | kg       |
| no2\_stor  | Nitrite nitrogen storage in the channel                       | kg       |
| cbod\_stor | Carbonaceous Biochemical Oxygen Demand storage in the channel | kg       |
| dox\_stor  | Dissolved oxygen storage in the channel                       | kg       |
| san\_stor  | Sand storage in the channel                                   | tons     |
| sil\_stor  | Silt storage in the channel                                   | tons     |
| cla\_stor  | Clay storage in the channel                                   | tons     |
| sag\_stor  | Small aggregate storage in the channel                        | tons     |
| lag\_stor  | Large aggregate storage in the channel                        | tons     |
| grv\_stor  | Gravel storage in the channel                                 | tons     |
| null       |                                                               |          |
| flo\_in    | Flow into the channel                                         | m3       |
| sed\_in    | Sediment entering the channel                                 | tons     |
| orgn\_in   | Organic nitrogen entering the channel                         | kg       |
| sedp\_in   | Sediment phosphorus entering the channel                      | kg       |
| no3\_in    | Nitrate nitrogen entering the channel                         | kg       |
| solp\_in   | Soluble phosphorus entering the channel                       | kg       |
| chla\_in   | Chlorophyll-a entering the channel                            | kg       |
| nh3\_in    | Ammonia nitrogen entering the channel                         | kg       |
| no2\_in    | Nitrite nitrogen entering the channel                         | kg       |
| cbod\_in   | Carbonaceous Biochemical Oxygen Demand entering the channel   | kg       |
| dox\_in    | Dissolved oxygen entering the channel                         | kg       |
| san\_in    | Sand entering the channel                                     | tons     |
| sil\_in    | Silt entering the channel                                     | tons     |
| cla\_in    | Clay entering the channel                                     | tons     |
| sag\_in    | Small aggregates entering the channel                         | tons     |
| lag\_in    | Large aggregates entering the channel                         | tons     |
| grv\_in    | Gravel entering the channel                                   | tons     |
| null       |                                                               |          |
| flo\_out   | Flow out of the channel                                       | m3       |
| sed\_out   | Sediment leaving the channel                                  | tons     |
| orgn\_out  | Organic nitrogen leaving the channel                          | kg       |
| sedp\_out  | Sediment phosphorus leaving the channel                       | kg       |
| no3\_out   | Nitrate nitrogen leaving the channel                          | kg       |
| solp\_out  | Soluble phosphorus leaving the channel                        | kg       |
| chla\_out  | Chlorophyll-a leaving the channel                             | kg       |
| nh3\_out   | Ammonia nitrogen leaving the channel                          | kg       |
| no2\_out   | Nitrite nitrogen leaving the channel                          | kg       |
| cbod\_out  | Carbonaceous Biochemical Oxygen Demand leaving the channel    | kg       |
| dox\_out   | Dissolved oxygen leaving the channel                          | kg       |
| san\_out   | Sand leaving the channel                                      | tons     |
| sil\_out   | Silt leaving the channel                                      | tons     |
| cla\_out   | Clay leaving the channel                                      | tons     |
| sag\_out   | Small aggregates leaving the channel                          | tons     |
| lag\_out   | Large aggregates leaving the channel                          | tons     |
| grv\_out   | Gravel leaving the channel                                    | tons     |
| null       |                                                               |          |

| **Field**    | **Description**                                   | **Unit** |
| ------------ | ------------------------------------------------- | -------- |
| jday         | Julian Day                                        | n/a      |
| mon          | Month                                             | n/a      |
| day          | Day of the month                                  | n/a      |
| yr           | Year                                              | n/a      |
| unit         | ID of the object                                  | n/a      |
| gis\_id      | Object ID in GIS                                  | n/a      |
| name         | Name of the object or SWAT+ setup (basin outputs) | n/a      |
| flo\_in      | Channel inflow                                    | m3/s     |
| geo\_bf      |                                                   | m3/s     |
| flo\_out     | Channel outflow                                   | m3/s     |
| peakr        | Peak rate                                         | m3/s     |
| sed\_in      | Sediment inflow                                   | tons     |
| sed\_out     | Sediment outflow                                  | tons     |
| washld       | Washload                                          | tons     |
| bedld        | Bedload                                           | tons     |
| dep          | Deposition                                        | tons     |
| deg\_btm     | Channel bottom degradation sediment               | tons     |
| deg\_bank    | Channel bank degradation sediment                 | tons     |
| hc\_sed      | Headcut sediment                                  | tons     |
| width        | Channel width                                     | m        |
| depth        | Channel depth                                     | m        |
| slope        | Channel slope                                     | m/m      |
| deg\_btm     |                                                   | m        |
| deg\_bank    |                                                   | m        |
| hc\_len      | Headcut length                                    | m        |
| flo\_in\_mm  | Channel inflow                                    | mm       |
| aqu\_in\_mm  |                                                   | mm       |
| flo\_out\_mm | Channel outflow                                   | mm       |

Last updated 3 years ago
