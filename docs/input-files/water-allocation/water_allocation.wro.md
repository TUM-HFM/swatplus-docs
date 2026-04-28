# water_allocation.wro

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/water-allocation/water_allocation.wro -->

The structure of the water allocation file is different than that of most other SWAT+ input files. As usual, the first line is reserved for a title. The second line in the file specifies the total number of water allocation tables included in the file.

Each water allocation table has three parts, which all have their own headers. First, the name of the water allocation table, the rule type, the number of source and demand objects, and whether or not one of the source objects is a channel are specified.

| Field                                                                               | Description                        | Type    |
| ----------------------------------------------------------------------------------- | ---------------------------------- | ------- |
| name                                                                                | Name of the water allocation table | string  |
| [rule\_typ](water_allocation.wro/rule_typ.md) | Rule type to allocate water        | string  |
| src\_obs                                                                            | Number of source objects           | integer |
| dmd\_obs                                                                            | Number of demand objects           | integer |
| [cha\_ob](water_allocation.wro/cha_ob.md)     | Channel as source object           | string  |

Next, the source objects and their monthly limits are defined. Source objects can be channels, reservoirs, aquifers, or an unlimited source. There needs to be one line per source object.

| Field                                                                                  | Description                      | Type    |
| -------------------------------------------------------------------------------------- | -------------------------------- | ------- |
| num                                                                                    | Source object number             | integer |
| [ob\_typ](water_allocation.wro/ob_typ-source.md) | Object type of the source object | string  |
| ob\_num                                                                                | ID of the source object          | integer |
| [limit\_mon](water_allocation.wro/limit_mon.md)  | Monthly limits                   | real    |

Finally, the demand objects are defined. Demand can be irrigation demand from an HRU, municipal demand, or demand to transfer to another object.There needs to be one line per demand object.

| Field                                                                                  | Description                                              | Type    |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------- | ------- |
| num                                                                                    | Demand object number                                     | integer |
| [ob\_typ](water_allocation.wro/ob_typ-demand.md) | Object type of the demand object                         | string  |
| ob\_num                                                                                | ID of the demand object                                  | integer |
| [withdr](water_allocation.wro/withdr.md)         | Withdrawal type                                          | string  |
| [amount](water_allocation.wro/amount.md)         | Withdrawal amount                                        | real    |
| [right](water_allocation.wro/right.md)           | Water right                                              | string  |
| treat\_typ                                                                             | Currently not functional                                 | string  |
| treatment                                                                              | Currently not functional                                 | string  |
| [rcv\_ob](water_allocation.wro/rcv_ob.md)        | Object type of the receiving object                      | string  |
| [rcv\_num](water_allocation.wro/rcv_num.md)      | ID of the receiving object                               | integer |
| rcv\_dtl                                                                               | Currently not used                                       | string  |
| [srcs](water_allocation.wro/srcs.md)             | Number of source objects available for the demand object | integer |
| [src](water_allocation.wro/src.md)               | Source object ID                                         | integer |
| [frac](water_allocation.wro/frac.md)             | Fraction of demand to be met by source object            | real    |
| [comp](water_allocation.wro/comp.md)             | Compensation from source object                          | string  |

Last updated 1 year ago
