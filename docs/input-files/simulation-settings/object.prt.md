# object.prt

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/simulation-settings/object.prt -->

The **object.prt** file is commonly used to:

- Print daily channel outflow to compare to observed streamflow a stream gage
- Print daily flow to a file that can be read in as a point source from another SWAT+ simulation

The only timestep output can be printed at using this file is daily. A description of the output files is provided in the [SWAT+ Output Files](../../output-files/output-file-format.md) section.

| Field                                                                             | Description                              | Type    |
| --------------------------------------------------------------------------------- | ---------------------------------------- | ------- |
| id                                                                                | ID of the object print record            | integer |
| [obj\_typ](object.prt/obj_typ.md)        | Type of object to print output for       | string  |
| [obj\_typ\_no](object.prt/obj_typ_no.md) | Number of the object to print output for | integer |
| [hyd\_typ](object.prt/hyd_typ.md)        | Type of hydrograph to print              | string  |
| filename                                                                          | User-defined name of output file         | string  |

Last updated 1 year ago
