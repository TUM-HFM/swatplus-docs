# 'object'.con

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/connectivity/hru.con -->

| Field                                                            | Description                                             | Type    | Unit        | Default | Range        |
| ---------------------------------------------------------------- | ------------------------------------------------------- | ------- | ----------- | ------- | ------------ |
| [id](hru.con/id.md)            | Unique ID of the object                                 | integer | n/a         | n/a     | n/a          |
| [name](hru.con/name.md)        | Name of the object                                      | string  | n/a         | n/a     | n/a          |
| [gis\_id](hru.con/gis_id.md)   | Object number in QSWAT+                                 | integer | n/a         | n/a     | n/a          |
| [area](hru.con/area.md)        | Area of the object                                      | real    | ha          | n/a     | n/a          |
| [lat](hru.con/lat.md)          | Latitude of the object                                  | real    | dec degrees | n/a     | -90.0-90.0   |
| [lon](hru.con/long.md)         | Longitude of the object                                 | real    | dec degrees | n/a     | -180.0-180.0 |
| [elev](hru.con/elev.md)        | Elevation of the object                                 | real    | m           | n/a     | 0-7000       |
| [hru](hru.con/hru.md)          | Pointer to the object data file                         | integer | n/a         | n/a     | n/a          |
| [wst](hru.con/wst.md)          | Pointer to the weather station file                     | string  | n/a         | n/a     | n/a          |
| [cst](hru.con/cst.md)          | Currently not used                                      | integer | n/a         | n/a     | n/a          |
| [ovfl](hru.con/ovfl.md)        | Currently not used                                      | integer | n/a         | n/a     | n/a          |
| [rule](hru.con/rule.md)        | Currently not used                                      | integer | n/a         | n/a     | n/a          |
| [out\_tot](hru.con/out_tot.md) | Total number of outgoing hydrographs                    | integer | n/a         | n/a     | 1-12         |
| [obj\_typ](hru.con/obj_typ.md) | Type of the receiving object                            | string  | n/a         | n/a     | n/a          |
| [obj\_id](hru.con/obj_id.md)   | ID of the receiving object                              | integer | n/a         | n/a     | n/a          |
| [hyd\_typ](hru.con/hyd_typ.md) | Type of hydrograph that is sent to the receiving object | string  | n/a         | n/a     | n/a          |
| [frac](hru.con/frac.md)        | Fraction of hydrograph sent to the receiving object     | real    | fraction    | n/a     | 0.0-1.0      |

Last updated 1 year ago
