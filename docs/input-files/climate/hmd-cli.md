# hmd.cli and hmd data files

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/climate/hmd.cli-and-humidity-data-files -->

The **relative humidity data files** contain the observed relative humidity input data. They are named by the user and must have the file ending \*.hmd. There must be one file per station used in the simulation. As in all SWAT+ input files, the first line in the relative humidity data files is reserved for user comments. The second line contains the column headers for the third line, which lists basic information about the station.

| Field | Description                                 | Type    | Unit            |
| ----- | ------------------------------------------- | ------- | --------------- |
| nbyr  | Length of the relative humidity time series | integer | years           |
| tstep | Time step of the relative humidity data     | integer | n/a             |
| lat   | Latitude of the relative humidity station   | real    | Decimal Degrees |
| lon   | Longitude of the relative humidity station  | real    | Decimal Degrees |
| elev  | Elevation of the relative humidity station  | real    | m               |

Starting in the fourth line, the year, Julian day, and the relative humidity are listed. There are no headers for these columns.

| Field | Description                   | Type    | Unit     |
| ----- | ----------------------------- | ------- | -------- |
| year  | Year of the observation       | integer | n/a      |
| jday  | Julian day of the observation | integer | n/a      |
| hmd   | Observed relative humidity    | real    | fraction |

The **hmd.cli** file lists the names of the relative humidity data files used in the simulation. The first line is reserved for user comments. The second line is reserved for the column header "filename". The user can list as many relative humidity data file names as needed for the simulation. Only one file name should be listed per line. All file names listed in [**weather-sta.cli**](weather-sta-cli.md) must be listed here. For every file name listed in **hmd.cli**, a file with that name must be provided by the user that contains the relative humidity data measured at the station.

Last updated 1 year ago
