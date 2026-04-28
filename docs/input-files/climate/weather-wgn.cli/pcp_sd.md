# pcp_sd

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/climate/weather-wgn.cli/pcp_sd -->

This parameter quantifies the variability in precipitation for each month. The standard deviation is calculated as

$$
σ_{mon}=\sqrt{(\frac{∑_{d=1}^N*(R_{day,mon}-R_{mon} )^2 }{N-1}})
$$

where $σ_{mon}$ is the standard deviation for daily precipitation in month $mon$ (mm H2O), $R_{day,mon}$ is the amount of precipitation for day $d$ in month $mon$ (mm H2O), $R_{mon}$ is the average precipitation for the month (mm H2O), and $N$ is the total number of daily precipitation records for month $mon$. Daily precipitation values of 0 mm are included in the standard deviation calculation.

Last updated 1 year ago
