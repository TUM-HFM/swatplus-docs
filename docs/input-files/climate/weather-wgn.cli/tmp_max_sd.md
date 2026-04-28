# tmp_max_sd

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/climate/weather-wgn.cli/tmp_max_sd -->

This parameter quantifies the variability in maximum temperature for each month. The standard deviation is calculated as

$$
σmx_{mon}=\sqrt{(\frac{∑_{d=1}^N*(T_{mx,mon}-μmx_{mon} )^2 }{N-1}})
$$

where $σmx_{mon}$is the standard deviation for daily maximum temperature in month $mon$ (ºC), $T_{mx,mon}$ is the daily maximum temperature on day $d$ in month $mon$ (ºC), $μmx_{mon}$ is the average daily maximum temperature for the month $mon$ (ºC), and $N$ is the total number of daily maximum temperature records for month $mon$.

Last updated 1 year ago
