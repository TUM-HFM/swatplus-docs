# denit_frac

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/basin-1/parameters.bsn/denit_frac -->

This parameter defines the fraction of field capacity water content above which denitrification takes place. Denitrification is the bacterial reduction of nitrate (NO3) to N2 or N2O gases under anaerobic (reduced) conditions. Because SWAT+ does not track the redox status of the soil layers, the presence of anaerobic conditions in a soil layer is defined by this variable. If the soil water content calculated as a fraction of field capacity is ≥ *denit\_frac*, then anaerobic conditions are assumed to be present and denitrification is modeled. If the soil water content calculated as a fraction of field capacity is < *denit\_frac*, then aerobic conditions are assumed to be present and denitrification is not modeled.

Last updated 1 year ago
