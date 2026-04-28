# management.sch

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/landuse-and-management/management.sch -->

Management operations can be scheduled by heat units/dates or by Decision Tables.

The structure of the **management.sch** file is different than that of most other SWAT+ input files. The first line for each management schedule specifies the name of the schedule and the number of scheduled and/or automatic operations. When using scheduled operations, it is followed by one line per operation listing operation-specific data. The operations must be scheduled by date (Heat Unit scheduling must be done using a Decision Table) listed in chronological order. For automatic operations, the names of the Decision Tables in lum.dtl are listed (one name per line). Behind the name of a Decision Table, the user may list the crop(s) used in the Decision Table, which can be useful when the same Decision Table is used for different crop rotations (see xxx in yyy).

The user may use both scheduled operations and Decision Tables for the same land use. If doing so, the names of the DTs should be listed first.

| Field                                                                                     | Description                               | Type    |
| ----------------------------------------------------------------------------------------- | ----------------------------------------- | ------- |
| [name](management.sch/name-management.sch.md) | Name of the management schedule           | string  |
| numb\_ops                                                                                 | Number of scheduled management operations | integer |
| numb\_auto                                                                                | Number of automatic operations            | integer |
| [op\_typ](management.sch/op_typ.md)           | Type of management operation              | string  |
| mon                                                                                       | Month operation is scheduled for          | integer |
| day                                                                                       | Day operation is scheduled for            | integer |
| hu\_sch                                                                                   | Currently not used                        | real    |
| [op\_data1](management.sch/op_data1.md)       | Operation data 1                          | string  |
| [op\_data2](management.sch/op_data2.md)       | Operation data 2                          | string  |
| [op\_data3](management.sch/op_data3.md)       | Operation data 3                          | real    |

Last updated 1 year ago
