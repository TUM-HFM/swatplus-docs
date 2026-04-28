# Recall

<!-- Source: https://swatplus.gitbook.io/io-docs/swat+-output-files/recall -->

The printing of recall object output is controlled by entering "y" or "n" in the *recall* line in [print.prt](../input-files/simulation-settings/print.prt.md). In addition, a basin average of all recall objects can be printed by entering "y" in the *basin\_psc* line in [print.prt](../input-files/simulation-settings/print.prt.md). Recall object output can be printed at daily, monthly, yearly, and average annual time steps. The names of the recall object output files are as follows:

- recall\_day.txt
- recall\_mon.txt
- recall\_yr.txt
- recall\_aa.txt
- basin\_psc\_day.txt
- basin\_psc\_mon.txt
- basin\_psc\_yr.txt
- basin\_psc\_aa.txt

| **Field** | **Description**                                      | **Unit** |
| --------- | ---------------------------------------------------- | -------- |
| jday      | Julian Day                                           | n/a      |
| mon       | Month                                                | n/a      |
| day       | Day of the month                                     | n/a      |
| yr        | Year                                                 | n/a      |
| name      | Name of the object or SWAT+ setup (basin outputs)    | n/a      |
| type      |                                                      |          |
| flo       | Recall object flow                                   | m3/s     |
| sed       | Recall object sediment                               | tons     |
| orgn      | Recall object organic nitrogen                       | kg       |
| sedp      | Recall object sediment phosphorus                    | kg       |
| no3       | Recall object nitrate nitrogen                       | kg       |
| solp      | Recall object soluble phosphorus                     | kg       |
| chla      | Recall object Chlorophyll-a                          | kg       |
| nh3       | Recall object ammonia nitrogen                       | kg       |
| no2       | Recall object nitrite nitrogen                       | kg       |
| cbod      | Recall object carbonaceous biochemical oxygen demand | kg       |
| dox       | Recall object dissolved oxygen                       | kg       |
| san       | Recall object sand                                   | tons     |
| sil       | Recall object silt                                   | tons     |
| cla       | Recall object clay                                   | tons     |
| sag       | Recall object small aggregates                       | tons     |
| lag       | Recall object large aggregates                       | tons     |
| grv       | Recall object gravel                                 | tons     |
| null      |                                                      |          |

Last updated 3 years ago
