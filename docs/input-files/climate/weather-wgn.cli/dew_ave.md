# dew_ave

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/climate/weather-wgn.cli/dew_ave -->

If all twelve months are < 1.0, the model assumes the data provided is relative humidity. Relative humidity is defined as the amount of water vapor in the air as a fraction of saturation humidity. If any month has a value > 1.0, the model assumes the data provided is dewpoint temperature.

Dew point temperature is the temperature at which the actual vapor pressure present in the atmosphere is equal to the saturation vapor pressure. This value is calculated by summing the dew point temperature for every day in the month for all years of record and dividing the sum by the number of days:

μdewmon=∑d=1N∗Tdew,monNμdew\_{mon}=\frac{∑\_{d=1}^N\*T\_{dew,mon}}{N}μdewmon​=N∑d=1N​∗Tdew,mon​​

where μdewmonμdew\_{mon}μdewmon​ is the mean daily dew point temperature for the month (ºC), Tdew,monT\_{dew,mon}Tdew,mon​ is the dew point temperature for day ddd in month monmonmon (ºC), and NNNis the total number of daily dew point records for month monmonmon. Please refer to the SWAT+ Theoretical Documentation for the equations used to convert dew point to relative humidity.

Last updated 1 year ago
