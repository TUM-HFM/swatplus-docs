# pcp_skew

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/climate/weather-wgn.cli/pcp_skew -->

This parameter quantifies the symmetry of the precipitation distribution around the monthly mean. The skew coefficient is calculated as

gmon=N∗∑d=1N∗(Rday,mon−Rmon)3(N−1)∗(N−2)∗(σmon)3g\_{mon}=\frac{N\*∑\_{d=1}^N\*(R\_{day,mon}-R\_{mon})^3 }{(N-1)\*(N-2)\*(σ\_{mon})^3}gmon​=(N−1)∗(N−2)∗(σmon​)3N∗∑d=1N​∗(Rday,mon​−Rmon​)3​

where gmong\_{mon}gmon​ is the skew coefficient for precipitation in the month, NNN is the total number of daily precipitation records for month monmonmon, Rday,monR\_{day,mon}Rday,mon​ is the amount of precipitation for day ddd in month monmonmon (mm H2O), RmonR\_{mon}Rmon​ is the average precipitation for the month (mm H2O), and σmonσ\_{mon}σmon​ is the standard deviation for daily precipitation in month monmonmon (mm H2O). Daily precipitation values of 0 mm are included in the skew coefficient calculation.

Last updated 1 year ago
