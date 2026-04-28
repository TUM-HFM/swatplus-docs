# Calibration

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction/calibration -->

Seibert and McDonnell (2002) suggested the use of “hard” and “soft” data for multi-criteria model calibration. Hard data are defined as measured time series, typically at a point (e.g., streamflow, groundwater levels, or soil moisture) that is commonly used in regression-based calibration techniques. Soft data are defined as information on individual processes within a balance that may not be directly measured in the study area, may be an average annual estimate, and may entail considerable uncertainty. Examples of soft data include regional estimates of baseflow ratios or ET, average depths of groundwater tables, average annual runoff coefficients for various land uses, annual rates of denitrification from research plots found in the literature, event mean concentrations, nutrient/sediment export coefficients, sediment deposition from reservoir sedimentation studies, average crop/vegetation LAI, and county crop yields (Arnold et al., 2015).

## Soft calibration procedure

Seibert and McDonnell (2002) argued that soft data represent a new dimension to the model calibration process that could: (1) enable dialog between experimentalists and modelers, (2) be a formal check on the reasonableness and consistency of internal model structures and simulations, and (3) specify realistic parameter ranges often ignored in today’s automatic calibration routines.

Misrepresented processes (water balance, nutrient balance, sediment source/sinks) within a watershed can cause errors when running management scenarios (Arnold et al., 2015). To ensure proper process representation, a soft calibration routine for water balance was added to SWAT+ code. The processes calibrated are surface runoff, lateral soil flow, percolation, and ET. Tile flow variables are not adjusted, if subsurface tiles are present, tile flow is simulated as the remainder of the water balance when all other processes are calibrated. The processes are input as the ratio to precipitation, thus minimizing the impact of different periods of record or different sources of precipitation. The procedure is a simple, heuristic approach with one variable for each process. The variables, associated process, change type, change limits, and total limits are listed in the table below.

| Variable | Process           | Change Type | Lower Change Limit | Upper Change Limit | Lower Limit | Upper Limit |
| -------- | ----------------- | ----------- | ------------------ | ------------------ | ----------- | ----------- |
| esco     | ET                | absolute    | -1.                | 1.                 | 0.          | 1.          |
| petco    | PET               | percent     | -20.               | 20.                | 0.8         | 1.2         |
| cn3\_swf | Surface runoff    | absolute    | -1.                | 1.                 | 0.          | 1.          |
| latq\_co | Lateral soil flow | absolute    | -1.                | 1.                 | 0.          | 1.          |
| perco    | Percolation       | absolute    | -0.7               | 0.7                | 0.          | 1.          |

The algorithm uses one variable at a time in the following order: 1) esco, 2) petco, 3) cn3\_swf, 4) latq\_co, 5) perco, and 6) cn3\_swf is calibrated again to ensure surface runoff is accurate. The first iteration with each variable is an initial guess calculated as shown in the table below. In each case, the initial change in each variable is a function of the difference (mm) in the soft ratio multiplied by precipitation minus the modeled process output. For example, if the surface runoff ratio input by the user is 0.2 and the simulated precipitation and surface runoff are 800 mm and 120 mm, respectively, the difference is 0.2\*800 – 120 = 40 mm.

| Variable | Initial Change               |
| -------- | ---------------------------- |
| esco     | (ETsoft – ETsim) / 500.      |
| petco    | (ETsoft – ETsim) / ETsoft    |
| cn3\_swf | -(SURQsoft – SURQsim) / 100. |
| latq\_co | (LATQsoft – LATQsim) / 400.  |
| perco    | (PERCsoft – PERCsim) / 1000. |

After the initial variable change, two additional iterations are performed using linear interpolation between the previous two simulations. Although the process response to the variable change is nonlinear, as the model iterates and approaches the soft data value, the linear interpolation is able to reasonably approximate the soft data. For the surface runoff example, with an initial difference of 40 mm, the next value of cn3\_swf used in the calibration would be set to cn3\_swf –0.4.

After the soft calibration is complete, the hard calibration of streamflow should only require some adjustments of the peaks and recessions.

Last updated 1 year ago
