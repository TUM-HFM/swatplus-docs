# weather-wgn.cli

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/climate/weather-wgn.cli -->

The weather generator file contains weather generator data for any number of stations. For each weather generator station, there will be one line specifying the name of the station, its latitude, longitude, and elevation, and the number of years of maximum monthly 0.5 h rainfall data used to define values for [pcp\_hhr](weather-wgn.cli/pcp_hhr.md). There are no headers for this line. These variables are listed in the first table below. The second line for each weather generator station contains the headers for the following 12 lines, which list the weather generator data for each month of the year. An overview of the weather generator data variables is given in the second table below.

| Field                                                                        | Description                                                                               | Type    | Unit            |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------- | --------------- |
| [name](weather-wgn.cli/name-weather_wgn.cli.md) | Name of weather generator station                                                         | string  | n/a             |
| latitude                                                                     | Latitude of weather generator station                                                     | real    | Decimal Degrees |
| longitude                                                                    | Longitude of weather generator station                                                    | real    | Decimal Degrees |
| elevation                                                                    | Elevation of weather generator station                                                    | real    | m               |
| [yrs\_pcp](weather-wgn.cli/yrs_pcp.md)          | Number of years of maximum monthly 0.5 h rainfall data used to define values for pcp\_hhr | integer | years           |

| Field                                                                        | Description                                                                             | Type | Unit           | Range     |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ---- | -------------- | --------- |
| [tmp\_max\_ave](weather-wgn.cli/tmp_max_ave.md) | Average or mean daily maximum air temperature for month                                 | real | °C             | -30 - 50  |
| [tmp\_min\_ave](weather-wgn.cli/tmp_min_ave.md) | Average or mean daily minimum air temperature for month                                 | real | °C             | -40 - 40  |
| [tmp\_max\_sd](weather-wgn.cli/tmp_max_sd.md)   | Standard deviation for daily maximum air temperature in month                           | real | °C             | 0.1 - 100 |
| [tmp\_min\_sd](weather-wgn.cli/tmp_min_sd.md)   | Standard deviation for daily minimum air temperature in month                           | real | °C             | 0.1 - 30  |
| [pcp\_ave](weather-wgn.cli/pcp_ave.md)          | Average or mean total monthly precipitation                                             | real | mm             | 0 - 600   |
| [pcp\_sd](weather-wgn.cli/pcp_sd.md)            | Standard deviation for daily precipitation in month                                     | real | mm/day         | 0.1 - 50  |
| [pcp\_skew](weather-wgn.cli/pcp_skew.md)        | Skew coefficient for daily precipitation in month                                       | real | mm             | -50 - 20  |
| [wet\_dry](weather-wgn.cli/wet_dry.md)          | Probability of a wet day following a dry day in the month                               | real | n/a            | 0 - 0.95  |
| [wet\_wet](weather-wgn.cli/wet_wet.md)          | Probability of a wet day following a wet day in the month                               | real | n/a            | 0 - 0.95  |
| [pcp\_days](weather-wgn.cli/pcp_days.md)        | Average number of days of precipitation in month                                        | real | n/a            | 0 - 31    |
| [pcp\_hhr](weather-wgn.cli/pcp_hhr.md)          | Maximum 0.5-hour rainfall in month                                                      | real | mm             | 0 - 125   |
| [slr\_ave](weather-wgn.cli/slr_ave.md)          | Average daily solar radiation for month                                                 | real | MJ/m^2/day     | 0 - 750   |
| [dew\_ave](weather-wgn.cli/dew_ave.md)          | Average daily dew point temperature for each month (ºC) or relative humidity (fraction) | real | °C or fraction | -50 - 25  |
| [wnd\_ave](weather-wgn.cli/wnd_ave.md)          | Average daily wind speed in month                                                       | real | m/s            | 0 - 100   |

Last updated 1 year ago
