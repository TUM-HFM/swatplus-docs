# plant.ini

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/landuse-and-management/plant.ini -->

A plant community can consist of plants growing at the same time or plants growing in rotation.

The structure of the file **plant.ini** is different than that of most other SWAT+ input files. The first line for each plant community specifies how many plants there are in the community and what the initial year of the rotation is. It is followed by one line per plant in the community.

| Field                                                                               | Description                                      | Type    | Unit     | Default  | Range       |
| ----------------------------------------------------------------------------------- | ------------------------------------------------ | ------- | -------- | -------- | ----------- |
| [name](plant.ini/name_pcom.md)          | Plant community name                             | string  | n/a      | n/a      | n/a         |
| [plnt\_cnt](plant.ini/plnt_cnt.md)      | Number of plants in the community                | integer | n/a      |          |             |
| [rot\_yr\_ini](plant.ini/rot_yr_ini.md) | Initial rotation year                            | integer | n/a      |          |             |
| [plnt\_name](plant.ini/plnt_name.md)    | Plant name as in plant database                  | string  | n/a      |          | n/a         |
| [lc\_status](plant.ini/lc_status.md)    | Land cover status at start of simulation         | string  | n/a      |          | n/a         |
| [lai\_init](plant.ini/lai_init.md)      | Initial Leaf Area Index                          | real    | m^2/m^2  | 0.0      | 0.0-8.0     |
| [bm\_init](plant.ini/bm_init.md)        | Initial plant biomass                            | real    | kg/ha    | 0.0      | 0.0-1000.0  |
| [phu\_init](plant.ini/phu_init.md)      | Initial fraction of plant heat units accumulated | real    | fraction | 0.0      | 0.0-100.0   |
| [plnt\_pop](plant.ini/plnt_pop.md)      | Plant population                                 | real    | n/a      | 0.0      |             |
| [yrs\_init](plant.ini/yrs_init.md)      | Age of plant at start of simulation              | real    | years    | 0.0      |             |
| [rsd\_init](plant.ini/rsd_init.md)      | Initial residue cover                            | real    | kg/ha    | 10000.00 | 0.0-10000.0 |

Last updated 1 year ago
