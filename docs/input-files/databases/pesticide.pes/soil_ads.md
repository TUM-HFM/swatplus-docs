# soil_ads

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/databases/pesticide.pes/soil_ads -->

Pesticides in the soil environment can be transported in solution or attached to sediment. The partitioning of a pesticide between the solution and soil phases is defined by the soil adsorption coefficient for the pesticide. The soil adsorption coefficient is the ratio of the pesticide concentration in the soil or solid phase to the pesticide concentration in the solution or liquid phase:

Kp=CsolidphaseCsolutionK\_p=\frac{C\_{solidphase}}{C\_{solution}} Kp​=Csolution​Csolidphase​​

where KpK\_pKp​ is the soil adsorption coefficient ((mg/kg)/(mg/L) or m3/ton), CsolidphaseC\_{solidphase}Csolidphase​ is the concentration of the pesticide sorbed to the solid phase (mg chemical/kg solid material or g/ton), and CsolutionC\_{solution}Csolution​ is the concentration of the pesticide in solution (mg chemical/L solution or g/ton). The definition of the soil adsorption coefficient in this equation assumes that the pesticide sorption process is linear with concentration and instantaneously reversible. Because the partitioning of pesticide is dependent upon the amount of organic material in the soil, the soil adsorption coefficient input to the model is normalized for soil organic carbon content. The relationship between the soil adsorption coefficient and the soil adsorption coefficient normalized for soil organic carbon content is:

Kp=Koc∗orgC100K\_p=K\_{oc}\*\frac{orgC}{100}Kp​=Koc​∗100orgC​

where KpK\_pKp​ is the soil adsorption coefficient ((mg/kg)/(mg/L)), KocK\_{oc}Koc​ is the soil adsorption coefficient normalized for soil organic carbon content ((mg/kg)/(mg/L) or m3/ton), and orgCorgCorgC is the percent organic carbon present in the soil.

Last updated 1 year ago
