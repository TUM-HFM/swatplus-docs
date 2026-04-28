# slr.cli and slr data files

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/climate/slr.cli-and-solar-radiation-data-files -->

The **solar radiation data files** contain the observed precipitation input data. They are named by the user and must have the file ending \*.slr. There must be one file per station used in the simulation. As in all SWAT+ input files, the first line in the solar radiation data files is reserved for user comments. The second line contains the column headers for the third line, which lists basic information about the station.

| Field | Description                               | Type    | Unit            |
| ----- | ----------------------------------------- | ------- | --------------- |
| nbyr  | Length of the solar radiation time series | integer | years           |
| tstep | Time step of the solar radiation data     | integer | n/a             |
| lat   | Latitude of the solar radiation station   | real    | Decimal Degrees |
| lon   | Longitude of the solar radiation station  | real    | Decimal Degrees |
| elev  | Elevation of the solar radiation station  | real    | m               |

Starting in the fourth line, the year, Julian day, and solar radiation are listed. There are no headers for these columns.

| Field | Description                   | Type    | Unit       |
| ----- | ----------------------------- | ------- | ---------- |
| year  | Year of the observation       | integer | n/a        |
| jday  | Julian day of the observation | integer | n/a        |
| slr   | Observed solar radiation      | real    | MJ/m^2/day |

The **slr.cli** file lists the names of the solar radiation data files used in the simulation. The first line is reserved for user comments. The second line is reserved for the column header "filename". The user can list as many solar radiation data file names as needed for the simulation. Only one file name should be listed per line. All file names listed in [**weather-sta.cli**](weather-sta-cli.md) must be listed here. For every file name listed in **slr.cli**, a file with that name must be provided by the user that contains the solar radiation data measured at the station.

Last updated 1 year ago
