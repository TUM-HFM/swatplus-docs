# Spatial Objects

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction/basin/spatial-objects -->

## Landscape Unit

A Landscape Unit is a collection of HRUs. A Landscape Unit can be equivalent to a subbasin, a floodplain or upland unit, or a grid cell with multiple HRUs. Landscape Units are only used for output. Two input files are required to define which HRUs belong to which Landscape Unit: 1) landscape elements and, 2) landscape define. The elements file includes HRUs and their corresponding LSU fraction and basin fractions. The define file specifies which HRUs are contained in each LSU.

## Routing Unit

The routing unit is the spatial unit in SWAT+ that allows us to lump outputs and route them to any other spatial object. The routing unit can be configured as a subbasin, then total flow (surface, lateral and tile flow) from the routing unit can be sent to a channel and all recharge from the routing unit sent to an aquifer. This is analogous to the current approach in SWAT. However, SWAT+ gives us much more flexibility in configuring a routing unit. For example, in CEAP, we are routing each HRU (field) through a small channel (gully or grass waterway) before it reaches the main channel. In this case, the routing unit is a collection of flow from the small channels. We also envision simulating multiple representative hillslopes to define a routing unit. Also, we are setting up scenarios that define a routing unit using tile flow from multiple fields and sending that flow to a wetland. Routing units will continue to be a convenient way of spatial lumping until we can simulate individual fields or cells in each basin.

Last updated 1 year ago
