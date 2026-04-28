# tmp.cli and tmp data files

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/climate/tmp.cli-and-temperature-data-files -->

The **temperature data files** contain the observed temperature input data. They are named by the user and must have the file ending \*.tmp. There must be one file per station used in the simulation. As in all SWAT+ input files, the first line in the temperature data files is reserved for user comments. The second line contains the column headers for the third line, which lists basic information about the station.

| Field | Description                           | Type    | Unit            |
| ----- | ------------------------------------- | ------- | --------------- |
| nbyr  | Length of the temperature time series | integer | years           |
| tstep | Time step of the temperature data     | integer | n/a             |
| lat   | Latitude of the temperature station   | real    | Decimal Degrees |
| lon   | Longitude of the temperature station  | real    | Decimal Degrees |
| elev  | Elevation of the temperature station  | real    | m               |

Starting in the fourth line, the year, Julian day, and the maximum and minimum temperatures are listed. There are no headers for these columns.

| Field  | Description                   | Type    | Unit |
| ------ | ----------------------------- | ------- | ---- |
| year   | Year of the observation       | integer | n/a  |
| jday   | Julian day of the observation | integer | n/a  |
| tmpmax | Observed maximum temperature  | real    | °C   |
| tmpmin | Observed minimum temperature  | real    | °C   |

The **tmp.cli** file lists the names of the temperature data files used in the simulation. The first line is reserved for user comments. The second line is reserved for the column header "filename". The user can list as many temperature data file names as needed for the simulation. Only one file name should be listed per line. All file names listed in [**weather-sta.cli**](weather-sta-cli.md) must be listed here. For every file name listed in **tmp.cli**, a file with that name must be provided by the user that contains the temperature data measured at the station.

Last updated 1 year ago
