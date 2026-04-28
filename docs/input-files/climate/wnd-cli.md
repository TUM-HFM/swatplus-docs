# wnd.cli and wnd data files

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/climate/wnd.cli-and-wind-speed-data-files -->

The **wind speed data files** contain the observed precipitation input data. They are named by the user and must have the file ending \*.wnd. There must be one file per station used in the simulation. As in all SWAT+ input files, the first line in the wind speed data files is reserved for user comments. The second line contains the column headers for the third line, which lists basic information about the station.

| Field | Description                          | Type    | Unit            |
| ----- | ------------------------------------ | ------- | --------------- |
| nbyr  | Length of the wind speed time series | integer | years           |
| tstep | Time step of the wind speed data     | integer | n/a             |
| lat   | Latitude of the wind speed station   | real    | Decimal Degrees |
| lon   | Longitude of the wind speed station  | real    | Decimal Degrees |
| elev  | Elevation of the wind speed station  | real    | m               |

Starting in the fourth line, the year, Julian day, and wind speed are listed. There are no headers for these columns.

| Field | Description                   | Type    | Unit |
| ----- | ----------------------------- | ------- | ---- |
| year  | Year of the observation       | integer | n/a  |
| jday  | Julian day of the observation | integer | n/a  |
| wnd   | Observed wind speed           | real    | m/s  |

The **wnd.cli** file lists the names of the wind speed data files used in the simulation. The first line is reserved for user comments. The second line is reserved for the column header "filename". The user can list as many wind speed data file names as needed for the simulation. Only one file name should be listed per line. All file names listed in [**weather-sta.cli**](weather-sta-cli.md) must be listed here. For every file name listed in **wnd.cli**, a file with that name must be provided by the user that contains the wind speed data measured at the station.

Last updated 1 year ago
