# "name".dtl

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/decision-tables/lum.dtl -->

The structure of the decision table files is different than that of most other SWAT+ input files. As usual, the first line is reserved for a title. The second line in the file specifies the total number of decision tables included in the file.

Each decision table has three parts, which all have their own headers. First, the name of the decision table and the number of conditions, alternatives, and actions are specified.

| Field | Description                | Type    |
| ----- | -------------------------- | ------- |
| name  | Name of the decision table | string  |
| conds | Number of conditions       | integer |
| alts  | Number of alternatives     | integer |
| acts  | Number of actions          | integer |

Next, the conditions and alternatives are defined. The number of lines used for this part of the decision table depends on the number of conditions.

| Field                                                                   | Description        | Type    |
| ----------------------------------------------------------------------- | ------------------ | ------- |
| [var](lum.dtl/var.md)              | Condition variable | string  |
| [obj](lum.dtl/obj.md)              | Object type        | string  |
| [obj\_num](lum.dtl/obj_num.md)     | Object ID          | integer |
| [lim\_var](lum.dtl/lim_var.md)     | Limit variable     | string  |
| [lim\_op](lum.dtl/lim_op.md)       | Limit operator     | string  |
| [lim\_const](lum.dtl/lim_const.md) | Limit constant     | real    |
| [alt](lum.dtl/alt.md)              | Alternative        | string  |

Finally, the outcomes and actions are defined. The number of lines used for this part of the decision table depends on the number of actions.

| Field                                                                 | Description                    | Type    |
| --------------------------------------------------------------------- | ------------------------------ | ------- |
| [act\_typ](lum.dtl/act_typ.md)   | Type of action                 | string  |
| [obj](lum.dtl/obj-1.md)          | Object type                    | string  |
| [obj\_num](lum.dtl/obj_num-1.md) | Object ID                      | integer |
| [name](lum.dtl/name.md)          | Name of the action             | string  |
| [option](lum.dtl/option.md)      | Action option                  | string  |
| [const](lum.dtl/const.md)        | Action constant                | real    |
| [const2](lum.dtl/const2.md)      | Action constant                | real    |
| [fp](lum.dtl/fp.md)              | File pointer for action option | string  |
| [outcome](lum.dtl/outcome.md)    | Outcome                        | string  |

Last updated 1 year ago
