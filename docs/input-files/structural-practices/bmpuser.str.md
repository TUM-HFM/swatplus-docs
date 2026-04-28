# bmpuser.str

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/structural-practices/bmpuser.str -->

There are many conservation practices that are not implemented in SWAT+, but for which approximate removal efficiencies have been established. To allow these practices to be included, this generic Best Management Practice (BMP) operation allows fixed removal efficiencies to be specified by constituent.

| Field                                                                          | Description                   | Type    | Unit    | Range     |
| ------------------------------------------------------------------------------ | ----------------------------- | ------- | ------- | --------- |
| [name](bmpuser.str/name_bmpdb.md)    | ​Name of BMP record           | string  | n/a     | n/a       |
| flag\_bmp                                                                      | Currently not used            | integer |         |           |
| [sed\_eff](bmpuser.str/sed_eff.md)   | Sediment removal by BMP       | real    | percent | 0.0-100.0 |
| [ptlp\_eff](bmpuser.str/ptlp_eff.md) | ​Particulate P removal by BMP | real    | percent | 0.0-100.0 |
| [solp\_eff](bmpuser.str/solp_eff.md) | ​Soluble P removal by BMP     | real    | percent | 0.0-100.0 |
| [ptln\_eff](bmpuser.str/ptln_eff.md) | Particulate N removal by BMP  | real    | percent | 0.0-100.0 |
| [soln\_eff](bmpuser.str/soln_eff.md) | Soluble N removal by BMP      | real    | percent | 0.0-100.0 |
| [bact\_eff](bmpuser.str/bact_eff.md) | Bacteria removal by BMP       | real    | percent | 0.0-100.0 |

Last updated 1 year ago
