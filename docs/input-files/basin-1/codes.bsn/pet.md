# pet

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/basin-1/codes.bsn/pet -->

Numerous methods exist to calculate potential evapotranspiration. Three of the most widely-used ones are included in SWAT+, the Priestley-Taylor, Penman/Monteith, and Hargreaves equations. The codes for the three methods are listed in the table below. If a method other than Priestley-Taylor, Penman/Monteith, or Hargreaves is recommended for the area, in which the watershed is located, the user can calculate daily PET values with the recommended method and import them into SWAT+ (using [pet](../../climate/weather-sta.cli/pet.md) in [**weather-sta.cli**](../../climate/weather-sta-cli.md)).

| Code | Option                  |
| ---- | ----------------------- |
| 0    | Priestley-Taylor method |
| 1    | Penman/Monteith method  |
| 2    | Hargreaves method       |

Last updated 1 year ago
