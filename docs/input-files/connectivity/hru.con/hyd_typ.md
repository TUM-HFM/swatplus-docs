# hyd_typ

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/connectivity/hru.con/hyd_typ -->

The types of hydrographs that can be sent depend on the sending object. The code tot is used for several spatial objects, but its meaning differs between objects. The table below lists the available codes and their definition depending on the type of object.

| Code | Object                                | Definition                                  |
| ---- | ------------------------------------- | ------------------------------------------- |
| tot  | Channel                               | Streamflow                                  |
| tot  | Aquifer                               | Groundwater flow                            |
| tot  | Reservoir                             | Reservoir outflow                           |
| tot  | Outlet                                | Flow at the outlet                          |
| tot  | Recall                                | Flow from point source or inlet             |
| tot  | HRU, Routing Unit                     | Surface runoff + lateral flow + tile flow   |
| sur  | HRU, Routing Unit                     | Surface runoff                              |
| lat  | HRU, Routing Unit                     | Lateral flow                                |
| til  | HRU, Routing Unit                     | Tile flow                                   |
| rhg  | HRU, Routing Unit, aquifer, reservoir | Seepage that recharges the receiving object |

Last updated 1 year ago
