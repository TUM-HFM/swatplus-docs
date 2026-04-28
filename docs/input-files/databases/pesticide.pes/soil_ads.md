# soil_ads

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/databases/pesticide.pes/soil_ads -->

Pesticides in the soil environment can be transported in solution or attached to sediment. The partitioning of a pesticide between the solution and soil phases is defined by the soil adsorption coefficient for the pesticide. The soil adsorption coefficient is the ratio of the pesticide concentration in the soil or solid phase to the pesticide concentration in the solution or liquid phase:

$K_p=\frac{C_{solidphase}}{C_{solution}}$

where $K_p$ is the soil adsorption coefficient ((mg/kg)/(mg/L) or m3/ton), $C_{solidphase}$ is the concentration of the pesticide sorbed to the solid phase (mg chemical/kg solid material or g/ton), and $C_{solution}$ is the concentration of the pesticide in solution (mg chemical/L solution or g/ton). The definition of the soil adsorption coefficient in this equation assumes that the pesticide sorption process is linear with concentration and instantaneously reversible. Because the partitioning of pesticide is dependent upon the amount of organic material in the soil, the soil adsorption coefficient input to the model is normalized for soil organic carbon content. The relationship between the soil adsorption coefficient and the soil adsorption coefficient normalized for soil organic carbon content is:

$K_p=K_{oc}*\frac{orgC}{100}$

where $K_p$ is the soil adsorption coefficient ((mg/kg)/(mg/L)), $K_{oc}$ is the soil adsorption coefficient normalized for soil organic carbon content ((mg/kg)/(mg/L) or m3/ton), and $orgC$ is the percent organic carbon present in the soil.

Last updated 1 year ago
