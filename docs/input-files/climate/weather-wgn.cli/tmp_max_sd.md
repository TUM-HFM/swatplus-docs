# tmp_max_sd

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/climate/weather-wgn.cli/tmp_max_sd -->

This parameter quantifies the variability in maximum temperature for each month. The standard deviation is calculated as

σmxmon=(∑d=1N∗(Tmx,mon−μmxmon)2N−1)σmx\_{mon}=\sqrt{(\frac{∑\_{d=1}^N\*(T\_{mx,mon}-μmx\_{mon} )^2 }{N-1}})σmxmon​=(N−1∑d=1N​∗(Tmx,mon​−μmxmon​)2​​)

where σmxmonσmx\_{mon}σmxmon​is the standard deviation for daily maximum temperature in month monmonmon (ºC), Tmx,monT\_{mx,mon}Tmx,mon​ is the daily maximum temperature on day ddd in month monmonmon (ºC), μmxmonμmx\_{mon}μmxmon​ is the average daily maximum temperature for the month monmonmon (ºC), and NNN is the total number of daily maximum temperature records for month monmonmon.

Last updated 1 year ago
