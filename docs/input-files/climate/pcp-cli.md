# pcp.cli and pcp data files

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/climate/pcp.cli-and-precipitation-data-files -->

The **precipitation data files** contain the observed precipitation input data. They are named by the user and must have the file ending \*.pcp. There must be one file per station used in the simulation. As in all SWAT+ input files, the first line in the precipitation data files is reserved for user comments. The second line contains the column headers for the third line, which lists basic information about the station.

| Field | Description                             | Type    | Unit            |
| ----- | --------------------------------------- | ------- | --------------- |
| nbyr  | Length of the precipitation time series | integer | years           |
| tstep | Time step of the precipitation data     | integer | n/a             |
| lat   | Latitude of the precipitation station   | real    | Decimal Degrees |
| lon   | Longitude of the precipitation station  | real    | Decimal Degrees |
| elev  | Elevation of the precipitation station  | real    | m               |

Starting in the fourth line, the year, Julian day, and precipitation amount are listed. There are no headers for these columns.

| Field | Description                   | Type    | Unit |
| ----- | ----------------------------- | ------- | ---- |
| year  | Year of the observation       | integer | n/a  |
| jday  | Julian day of the observation | integer | n/a  |
| pcp   | Observed precipitation        | real    | mm   |

If the user wishes to run simulations at a sub-daily time step, precipitation data has to be provided at the simulation time step. Currently, the model is able to run at an hourly time step. Smaller time steps have not been tested yet. Three additional columns need to be included in the hourly precipitation files:

| Field | Description                   | Type    | Unit |
| ----- | ----------------------------- | ------- | ---- |
| year  | Year of the observation       | integer | n/a  |
| jday  | Julian day of the observation | integer | n/a  |
| mon   | Month of the observation      | integer | n/a  |
| day   | Day of the observation        | integer | n/a  |
| hr    | Time of the observation       | integer | n/a  |
| pcp   | Observed precipitation        | real    | mm   |

The **pcp.cli** file lists the names of the precipitation data files used in the simulation. The first line is reserved for user comments. The second line is reserved for the column header "filename". The user can list as many precipitation data file names as needed for the simulation. Only one file name should be listed per line. All file names listed in [**weather-sta.cli**](weather-sta-cli.md) must be listed here. For every file name listed in **pcp.cli**, a file with that name must be provided by the user that contains the precipitation data measured at the station.

Last updated 1 year ago
