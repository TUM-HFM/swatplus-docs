# pcp_skew

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/climate/weather-wgn.cli/pcp_skew -->

This parameter quantifies the symmetry of the precipitation distribution around the monthly mean. The skew coefficient is calculated as

$$
g_{mon}=\frac{N*∑_{d=1}^N*(R_{day,mon}-R_{mon})^3 }{(N-1)*(N-2)*(σ_{mon})^3}
$$

where $g_{mon}$ is the skew coefficient for precipitation in the month, $N$ is the total number of daily precipitation records for month $mon$, $R_{day,mon}$ is the amount of precipitation for day $d$ in month $mon$ (mm H2O), $R_{mon}$ is the average precipitation for the month (mm H2O), and $σ_{mon}$ is the standard deviation for daily precipitation in month $mon$ (mm H2O). Daily precipitation values of 0 mm are included in the skew coefficient calculation.

Last updated 1 year ago
