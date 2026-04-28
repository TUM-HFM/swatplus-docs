# pcp_sd

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/climate/weather-wgn.cli/pcp_sd -->

This parameter quantifies the variability in precipitation for each month. The standard deviation is calculated as

σmon=(∑d=1N∗(Rday,mon−Rmon)2N−1)σ\_{mon}=\sqrt{(\frac{∑\_{d=1}^N\*(R\_{day,mon}-R\_{mon} )^2 }{N-1}})σmon​=(N−1∑d=1N​∗(Rday,mon​−Rmon​)2​​)

where σmonσ\_{mon}σmon​ is the standard deviation for daily precipitation in month monmonmon (mm H2O), Rday,monR\_{day,mon}Rday,mon​ is the amount of precipitation for day ddd in month monmonmon (mm H2O), RmonR\_{mon}Rmon​ is the average precipitation for the month (mm H2O), and NNN is the total number of daily precipitation records for month monmonmon. Daily precipitation values of 0 mm are included in the standard deviation calculation.

Last updated 1 year ago
