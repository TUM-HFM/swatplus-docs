# Output File Format

<!-- Source: https://swatplus.gitbook.io/io-docs/swat+-output-files/output-file-format -->

There a some output files that the user can choose to print or not to print and some that can be printed at daily, monthly, yearly, and average annual time steps. This can be controlled in the [**print.prt**](../input-files/simulation-settings/print.prt.md) file. In addition, selected output for individual spatial objects can be printed using the [**object.prt**](../input-files/simulation-settings/object.prt.md) file. Finally, there are a few output files that will be printed for every SWAT+ run. These are used by the SWAT+ developers for debugging.

All SWAT+ output files are free format and space delimited. The first line in each output file is reserved for a title. If the files were written using the SWAT+ Editor, the title will specify the name of the SWAT+ setup and the date and number of the SWAT+ revision that was used to run the simulation. The second line in all SWAT+ output files is used for the header, i.e. the names of the variables listed in the file. The third line is used for the units of the output variables.

Last updated 1 year ago
