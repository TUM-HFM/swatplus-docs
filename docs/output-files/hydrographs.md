# Hydrographs

<!-- Source: https://swatplus.gitbook.io/io-docs/swat+-output-files/hydrographs -->

SWAT+ prints two hydrograph output files per time step, one for incoming and one for outgoing hydrographs. The printing of hydrographs is controlled by entering "y" or "n" in the *hyd* line in [print.prt](../input-files/simulation-settings/print.prt.md). Hydrographs can be printed at daily, monthly, yearly, and average annual time steps. The names of the hydrograph output files are as follows:

- hydin\_day.txt
- hydout\_day.txt
- hydin\_mon.txt
- hydout\_mon.txt
- hydin\_yr.txt
- hydout\_yr.txt
- hydin\_aa.txt
- hydout\_aa.txt

The number of lines in the hydrograph output files depends on the number of connections between spatial objects defined in the SWAT+ setup. In the incoming hydrograph files, for each receiving object there will be one line per source object it receives a hydrograph from. The number of lines per source object in the outgoing hydrograph files equals the number of receiving objects it sends hydrographs to.

In

Out

| **Field** | **Description**                                 | **Unit** |
| --------- | ----------------------------------------------- | -------- |
| jday      | Julian Day                                      | n/a      |
| mon       | Month                                           | n/a      |
| day       | Day of the month                                | n/a      |
| yr        | Year                                            | n/a      |
| name      | Name of the receiving object                    | n/a      |
| type      | Type of the receiving object                    |          |
| objtyp    | Type of the source object                       |          |
| typ\_no   | ID of the source object                         |          |
| hyd\_typ  | Type of the incoming hydrograph                 |          |
| fraction  | Fraction of the incoming hydrograph             |          |
| flo       | Incoming flow                                   | m3/s     |
| sed       | Incoming sediment                               | tons     |
| orgn      | Incoming organic nitrogen                       | kg       |
| sedp      | Incoming sediment phosphorus                    | kg       |
| no3       | Incoming nitrate nitrogen                       | kg       |
| solp      | Incoming soluble phosphorus                     | kg       |
| chla      | Incoming Chlorophyll-a                          | kg       |
| nh3       | Incoming ammonia nitrogen                       | kg       |
| no2       | Incoming nitrite nitrogen                       | kg       |
| cbod      | Incoming carbonaceous biochemical oxygen demand | kg       |
| dox       | Incoming dissolved oxygen                       | kg       |
| san       | Incoming sand                                   | tons     |
| sil       | Incoming silt                                   | tons     |
| cla       | Incoming clay                                   | tons     |
| sag       | Incoming small aggregates                       | tons     |
| lag       | Incoming large aggregates                       | tons     |
| grv       | Incoming gravel                                 | tons     |
| null      |                                                 |          |

| **Field** | **Description**                                 | **Unit** |
| --------- | ----------------------------------------------- | -------- |
| jday      | Julian Day                                      | n/a      |
| mon       | Month                                           | n/a      |
| day       | Day of the month                                | n/a      |
| yr        | Year                                            | n/a      |
| name      | Name of the source object                       | n/a      |
| type      | Type of the source object                       |          |
| objtyp    | Type of the receiving object                    |          |
| typ\_no   | ID of the receiving object                      |          |
| hyd\_typ  | Type of the outgoing hydrograph                 |          |
| fraction  | Fraction of the outgoing hydrograph             |          |
| flo       | Outgoing flow                                   | m3/s     |
| sed       | Outgoing sediment                               | tons     |
| orgn      | Outgoing organic nitrogen                       | kg       |
| sedp      | Outgoing sediment phosphorus                    | kg       |
| no3       | Outgoing nitrate nitrogen                       | kg       |
| solp      | Outgoing soluble phosphorus                     | kg       |
| chla      | Outgoing Chlorophyll-a                          | kg       |
| nh3       | Outgoing ammonia nitrogen                       | kg       |
| no2       | Outgoing nitrite nitrogen                       | kg       |
| cbod      | Outgoing carbonaceous biochemical oxygen demand | kg       |
| dox       | Outgoing dissolved oxygen                       | kg       |
| san       | Outgoing sand                                   | tons     |
| sil       | Outgoing silt                                   | tons     |
| cla       | Outgoing clay                                   | tons     |
| sag       | Outgoing small aggregates                       | tons     |
| lag       | Outgoing large aggregates                       | tons     |
| grv       | Outgoing gravel                                 | tons     |
| null      |                                                 |          |

Last updated 3 years ago
