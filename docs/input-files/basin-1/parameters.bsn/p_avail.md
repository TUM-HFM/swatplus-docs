# p_avail

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/basin-1/parameters.bsn/p_avail -->

Many studies have shown that after an application of soluble P fertilizer, solution P concentration decreases rapidly with time due to reaction with the soil. This initial "fast" reaction is followed by a much slower decrease in solution P that may continue for several years (Barrow and Shaw, 1975; Munns and Fox, 1976; Rajan and Fox, 1972; Sharpley, 1982). In order to account for the initial rapid decrease in solution P, SWAT+ assumes a rapid equilibrium exists between solution P and an "active" mineral pool. The subsequent slow reaction is simulated by the slow equilibrium assumed to exist between the "active" and "stable" mineral pools. The algorithms governing movement of inorganic phosphorus between these three pools are taken from Jones et al. (1984).

Equilibration between the solution and active mineral pool is governed by the phosphorus availability index. This index specifies the fraction of fertilizer P which is in solution after an incubation period, i.e. after the rapid reaction period.

A number of methods have been developed to measure the phosphorus availability index. Jones et al. (1984) recommends a method outlined by Sharpley et al. (1984) in which various amounts of phosphorus are added in solution to the soil as K2HPO4. The soil is wetted to field capacity and then dried slowly at 25°C. When dry, the soil is rewetted with deionized water. The soil is exposed to several wetting and drying cycles over a 6-month incubation period. At the end of the incubation period, solution phosphorus is determined by extraction with anion exchange resin.

The P availability index is then calculated as:

pai=Psolution,f−Psolution,ifertminPpai=\frac{P\_{solution,f}-P\_{solution,i}}{fert\_{minP}}pai=fertminP​Psolution,f​−Psolution,i​​

where *pai* is the phosphorus availability index, Psolution,fP\_{solution,f}Psolution,f​ is the amount of phosphorus in solution after fertilization and incubation, Psolution,iP\_{solution,i}Psolution,i​ is the amount of phosphorus in solution before fertilization, and fertminPfert\_{minP}fertminP​ is the amount of soluble P fertilizer added to the sample.

#### References

Barrow, N.J. and T.C. Shaw. 1975. The slow reactions between soil and anions. 2. Effect of time and temperature on the decrease in phosphate concentration in soil solution. Soil Science 119(2): 167-177. [Link](https://journals.lww.com/soilsci/abstract/1975/02000/the_slow_reactions_between_soil_and_anions__2_.10.aspx)

Jones et al. 1984

Munns and Fox. 1976

Rajan and Fox. 1972

Sharpley. 1982

Sharpley et al. 1984

Last updated 1 year ago
