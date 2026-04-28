# nutrients.res

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/reservoirs/nutrients.res -->

| Field                                                                      | Description                                                            | Type    | Unit  | Default | Range    |
| -------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------- | ----- | ------- | -------- |
| [name](nutrients.res/untitled.md)          | Name of the reservoir and wetland nutrient record                      | string  | n/a   | n/a     | n/a      |
| [mid\_start](nutrients.res/untitled-7.md)  | Beginning month of the mid-year nutrient settling period               | integer | n/a   | 5       | 0-12     |
| [mid\_end](nutrients.res/untitled-6.md)    | Ending month of the mid-year nutrient settling period                  | integer | n/a   | 10      | 0-12     |
| [mid\_n\_stl](nutrients.res/untitled-5.md) | Nitrogen settling rate during the mid-year nutrient settling period    | real    | m/day | 5.50    | 1.0-15.0 |
| [n\_stl](nutrients.res/untitled-4.md)      | Nitrogen settling rate outside the mid-year nutrient settling period   | real    | m/day | 5.50    | 1.0-15.0 |
| [mid\_p\_stl](nutrients.res/untitled-3.md) | Phosphorus settling rate during the mid-year nutrient settling period  | real    | m/day | 10.0    | 2.0-20.0 |
| [p\_stl](nutrients.res/untitled-2.md)      | Phosphorus settling rate outside the mid-year nutrient settling period | real    | m/day | 10.0    | 2.0-20.0 |
| [chla\_co](nutrients.res/untitled-1.md)    | Chlorophyll-a production coefficient for the reservoir                 | real    | n/a   | 1.0     | 0.0-1.0  |
| [secchi\_co](nutrients.res/secchi_co.md)   | Water clarity coefficient for the reservoir                            | real    | n/a   | 1.0     | 0.50-2.0 |
| [theta\_n](nutrients.res/theta_n.md)       | Temperature adjustment for nitrogen loss (settling)                    | real    | n/a   | 1.0     |          |
| [theta\_p](nutrients.res/theta_p.md)       | Temperature adjustment for phosphorus loss (settling)                  | real    | n/a   | 1.0     |          |
| [n\_min\_stl](nutrients.res/n_min_stl.md)  | Minimum nitrogen concentration for settling                            | real    | ppm   | 0.10    |          |
| [p\_min\_stl](nutrients.res/p_min_stl.md)  | Minimum phosphorus concentration for settling                          | real    | ppm   | 0.01    |          |

Last updated 1 year ago
