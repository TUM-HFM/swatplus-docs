# dew_ave

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/climate/weather-wgn.cli/dew_ave -->

If all twelve months are < 1.0, the model assumes the data provided is relative humidity. Relative humidity is defined as the amount of water vapor in the air as a fraction of saturation humidity. If any month has a value > 1.0, the model assumes the data provided is dewpoint temperature.

Dew point temperature is the temperature at which the actual vapor pressure present in the atmosphere is equal to the saturation vapor pressure. This value is calculated by summing the dew point temperature for every day in the month for all years of record and dividing the sum by the number of days:

$$
μdew_{mon}=\frac{∑_{d=1}^N*T_{dew,mon}}{N}
$$

where $μdew_{mon}$ is the mean daily dew point temperature for the month (ºC), $T_{dew,mon}$ is the dew point temperature for day $d$ in month $mon$ (ºC), and $N$is the total number of daily dew point records for month $mon$. Please refer to the SWAT+ Theoretical Documentation for the equations used to convert dew point to relative humidity.

Last updated 1 year ago
