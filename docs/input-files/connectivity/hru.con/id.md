# id

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/connectivity/hru.con/id -->

The unique ID of the object is a primary key that is referenced by [obj\_id](obj_id.md).

Please be aware that the unique ID of the object is not necessarily the same as the ID in QSWAT+. The GIS interface numbers the objects when they are first created. Later in the process, some objects might be replaced by others, e.g. channels that are located within reservoirs. When the SWAT+ Editor writes the SWAT+ input files, it assigns consecutive ID numbers to those objects that are still included in the final setup of the model. It is extremely important to pay attention to this when identifying the channels that streamflow gauges are located on for comparing simulated and observed data.

Last updated 1 year ago
