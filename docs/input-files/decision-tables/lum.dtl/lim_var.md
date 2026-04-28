# lim_var

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/decision-tables/lum.dtl/lim_var -->

The condition variables, for which a limit variable must be specified, are listed in the table below. Some limit variables must be used in combination with a limit operator (see [lim\_op](lim_op.md)).

| Condition variable | Limit variable | Description                      | Limit operator? |
| ------------------ | -------------- | -------------------------------- | --------------- |
| soil\_water        | wp             | Wilting point                    | yes             |
| soil\_water        | fc             | Field capacity                   | yes             |
| soil\_water        | ul             | Upper limit                      | yes             |
| plant\_gro         | y              | Plant growing                    | no              |
| plant\_name\_gro   |                |                                  | no              |
| hyd\_soil\_group   |                |                                  | no              |
| land\_use          |                |                                  | no              |
| tillage            |                |                                  | no              |
| plant              |                |                                  | no              |
| ch\_use            |                |                                  | no              |
| vol                | evol           | Emergency volume                 | yes             |
| vol                | pvol           | Principal volume                 | yes             |
| vol                | e-pv           | Emergency minus principal volume | no              |
| wet\_depth         |                |                                  | no              |
| vol\_wet           | evol           | Emergency volume                 | yes             |
| vol\_wet           | pvol           | Principal volume                 | yes             |

Last updated 1 year ago
