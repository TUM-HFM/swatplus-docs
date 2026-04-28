# alg_shd_l

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/channels/nutrients.cha/alg_shd_l -->

The light extinction coefficient, klk\_lkl​, is calculated as a function of the algal density using the nonlinear equation:

kl=kl,0+kl,1∗α0∗algae+kl,2∗(α0∗algae)2/3k\_l=k\_{l,0}+k\_{l,1}\*\alpha\_0\*algae+k\_{l,2}\*(\alpha\_0\*algae)^{2/3}kl​=kl,0​+kl,1​∗α0​∗algae+kl,2​∗(α0​∗algae)2/3

where kl,0k\_{l,0}kl,0​ is the non-algal portion of the light extinction coefficient (m−1m^{-1}m−1), kl,1k\_{l,1}kl,1​ is the linear algal self shading coefficient (m−1(μg−chla/L)−1)m^{-1}(\mu g - chla/L)^{-1})m−1(μg−chla/L)−1), kl,2k\_{l,2}kl,2​ is the nonlinear algal self shading coefficient m−1(μg−chla/L)−2/3)m^{-1}(\mu g - chla/L)^{-2/3})m−1(μg−chla/L)−2/3), α0\alpha\_0 α0​is the ratio of chlorophyll *a* to algal biomass (μg\mu g μg chla/mg alg), and algaealgaealgae is the algal biomass concentration (mg alg/L).

This equation allows a variety of algal, self-shading, light extinction relationships to be modeled. When both kl,1k\_{l,1}kl,1​ and kl,2k\_{l,2}kl,2​ are set to 0, no algal self-shading is simulated. When kl,1k\_{l,1}kl,1​ is set to a value other than 0 and kl,2k\_{l,2}kl,2​ is set to 0, linear algal self-shading is modeled. When both kl,1k\_{l,1}kl,1​ and kl,2k\_{l,2}kl,2​ are set to a value other than 0, non-linear algal self-shading is modeled.

The Riley equation (Bowie et al., 1985) defines kl,1=0.0088m−1(μg−chla/L)−1k\_{l,1} = 0.0088 m^{-1}(\mu g - chla/L)^{-1}kl,1​=0.0088m−1(μg−chla/L)−1 and kl,2=0.054m−1(μg−chla/L)−2/3)k\_{l,2} = 0.054 m^{-1}(\mu g - chla/L)^{-2/3})kl,2​=0.054m−1(μg−chla/L)−2/3).

#### Relevant chapter in the Theoretical Documentation:

[Local Specific Growth Rate of Algae](https://swatplus.gitbook.io/io-docs/theoretical-documentation/section-7-main-channel-processes/in-stream-nutrient-processes/algae/algal-growth/local-specific-growth-rate-of-algae)

#### References

> Bowie, G.L., W.B. Mills, D.B. Porcella, C.L. Campbell, J.R. Pagenkopt, G.L. Rupp, K.M. Johnson, P.W.H. Chan, and S.A. Gherini. 1985. Rates, constants, and kinetic formulations in surface water quality modeling, 2nd ed. EPA/600/3-85/040, U.S. Environmental Protection Agency, Athens, GA.

Last updated 1 year ago
