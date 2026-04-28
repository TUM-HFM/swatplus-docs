# days_mat

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/databases/plants.plt/untitled-18 -->

The PHU program was incorporated directly into SWAT+. The heat units to maturity were changed to days to maturity (*days\_mat*). The concept of heat units to maturity was developed for annual crops and we use heat units for the entire growing season for native perennials and native annuals. By inputting days to maturity, we can include different crop varieties as defined by length of growing season (e.g., 120-, 110-, 100- and 90-day varieties for corn). The heat units to maturity calculation in the model first computes base zero heat units for the entire year and assumes a planting date when heat units exceed 0.15 \* base zero. Then, the model calculates heat units from planting date through the days to maturity using the crop's base temperature as specified by [tmp\_base](tmp_base.md). If the maximum days for a crop are input, e.g., 120 days for corn, and the growing season is less than 120 days, the model essentially sums heat units for the entire growing season which represents (and estimates) the maximum days to maturity.

The algorithm currently uses monthly weather generator parameters but could be modified to alternatively use daily temperature inputs. The model provides heat unit estimates in both the northern and southern hemispheres.

There are several advantages to incorporating the heat unit program into SWAT+ including:

1. It eliminates the need for running an external program when developing inputs,
2. allows input of a commonly understood variable (days) instead of a variable that is not commonly known at every location (heat units),
3. allows the model to calculate heat units for native perennials and annuals that are location dependent,
4. a database (plants.plt) can be maintained and supported that includes different crop varieties, and
5. by inputting the maximum growing season for a crop, the model will calculate appropriate heat units for that crop anywhere in the northern or southern hemisphere.

Last updated 1 year ago
