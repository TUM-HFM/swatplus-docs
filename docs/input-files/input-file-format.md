# Input File Format

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/input-file-format -->

All SWAT+ input files are free format and space delimited.

The first line in each input file is reserved for a title. If the files were written using the SWAT+ Editor, the title will specify the name of the file, the version of the SWAT+ Editor, and the date and time the file was written. While this line is required, it is not read in by SWAT+ and may be modified or left blank. The title is limited to 80 spaces.

The second line in all SWAT+ input files except for file.cio is reserved for the header, i.e. the names of the variables listed in the file. Some files will have additional header lines (e.g., print.prt).

Last updated 1 year ago
