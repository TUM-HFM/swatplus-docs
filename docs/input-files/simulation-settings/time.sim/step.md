# step

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/simulation-settings/time.sim/step -->

SWAT+ is able to run at the following time steps:

| Code | Time Step  |
| ---- | ---------- |
| 0    | day        |
| 2    | 12 hours   |
| 24   | hour       |
| 96   | 15 minutes |
| 1440 | minute     |

When using the Green & Ampt method ([gampt](../../basin-1/codes.bsn/abstr_init.md) in [**codes.bsn**](../../basin-1/codes.bsn.md)) for calculating surface runoff, the time step of the precipitation data must match the simulation time step.

Last updated 1 year ago
