# Calibration

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/calibration -->

The soft calibration requires 10-12 simulations and is a simple, heuristic, one-at-a-time procedure. Each process has one or two parameters and each is looped through a couple of times. After the soft calibration is complete, the hard (daily gage) calibration should only require some adjustments of the peaks and recessions.

Three files are needed for soft calibration of the water balance:

## codes.sft

You can turn the water balance soft calibration on (“y”) and off (“n”) in the HYD\_HRU column. The others are still a work in progress.

[codes.sft](codes.sft.md)

## wb\_parms.sft

Shows all the parameters that can be used with max/min ranges and max/min absolute values. It is fixed and you shouldn’t have to change it.

[wb\_parms.sft](wb_parms.sft.md)

## water\_balance.sft

Gives each component of the water balance we are soft calibrating as a fraction of precipitation.

[water\_balance.sft](water_balance.sft.md)

Last updated 1 year ago
