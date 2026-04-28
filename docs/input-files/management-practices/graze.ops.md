# graze.ops

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/management-practices/graze.ops -->

This operation removes plant biomass at a specified rate and allows simultaneous application of manure.

The parameter values of the pre-defined grazing operations are very rough estimates. If grazing is relevant in a watershed, the user should research their own values based on the stocking rate and type of animal.

| Field                                                                          | Description                                                  | Type   | Unit        | Default | Range      |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------ | ------ | ----------- | ------- | ---------- |
| [name](graze.ops/name_graze.md)      | Grazing operation name                                       | string | n/a         | n/a     | n/a        |
| [fertname](graze.ops/fertnm.md)      | Fertilizer database name for manure deposited during grazing | string | n/a         | n/a     | n/a        |
| [bm\_eat](graze.ops/eat.md)          | Dry weight of biomass removed by grazing daily               | real   | (kg/ha)/day | 0.0     | 0.0-500.0  |
| [bm\_tramp](graze.ops/tramp.md)      | Dry weight of biomass removed by trampling daily             | real   | (kg/ha)/day | 0.0     | 0.0-500.0  |
| [man\_amt](graze.ops/manure.md)      | Dry weight of manure deposited daily                         | real   | (kg/ha)/day | 0.0     | 0.0-500.0  |
| [grz\_bm\_min](graze.ops/bio_min.md) | Minimum plant biomass for grazing to occur                   | real   | kg/ha       | 0.0     | 0.0-5000.0 |

Last updated 1 year ago
