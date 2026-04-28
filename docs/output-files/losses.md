# Losses

<!-- Source: https://swatplus.gitbook.io/io-docs/swat+-output-files/losses -->

Losses output can be printed at basin, LSU, HRU, and HRU-lte level by entering "y" in the *basin\_wb*, *lsunit\_wb*, *hru\_wb*, and *hru-lte\_wb* lines in [print.prt](../input-files/simulation-settings/print.prt.md), respectively. Losses output can be printed at daily, monthly, yearly, and average annual time steps. The names of the losses output files are as follows:

- basin\_ls\_day.txt
- basin\_ls\_mon.txt
- basin\_ls\_yr.txt
- basin\_ls\_aa.txt
- lsunit\_ls\_day.txt
- lsunit\_ls\_mon.txt
- lsunit\_ls\_yr.txt
- lsunit\_ls\_aa.txt
- hru\_ls\_day.txt
- hru\_ls\_mon.txt
- hru\_ls\_yr.txt
- hru\_ls\_aa.txt
- hru-lte\_ls\_day.txt
- hru-lte\_ls\_mon.txt
- hru-lte\_ls\_yr.txt
- hru-lte\_ls\_aa.txt

| **Field** | **Description**                                               | **Unit** |
| --------- | ------------------------------------------------------------- | -------- |
| jday      | Julian day                                                    | n/a      |
| mon       | Month                                                         | n/a      |
| day       | Day of the month                                              | n/a      |
| yr        | Year                                                          | n/a      |
| unit      | ID of the object                                              | n/a      |
| gis\_id   | Object ID in GIS                                              | n/a      |
| name      | Name of the object or SWAT+ setup (basin outputs)             | n/a      |
| sedyld    | Sediment yield leaving the landscape through water erosion    | t/ha     |
| sedorgn   | Organic nitrogen transported in surface runoff                | kg/ha    |
| sedorgp   | Organic phosphorus transported in surface runoff              | kg/ha    |
| surqno3   | Nitrate nitrogen transported in surface runoff                | kg/ha    |
| lat3no3   | Nitrate nitrogen transported in lateral flow                  | kg/ha    |
| surqsolp  | Soluble phosphorus transported in surface runoff              | kg/ha    |
| usle      | Sediment yield predicted with the USLE equation               | t/ha     |
| sedmin    | Mineral phosphorus leaving the landscape attached to sediment | kg/ha    |
| tileno3   | Nitrate nitrogen transported in tile flow                     | kg/ha    |
| lchlabp   | Soluble (labile) phosphorus leaching past bottom soil layer   | kg/ha    |
| tilelabp  | soluble (labile) phosphorus in tile flow                      | kg/ha    |
| satexn    | Nitrate nitrogen in saturation excess surface runoff          | kg/ha    |

Last updated 3 years ago
