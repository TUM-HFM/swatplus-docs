# alg_shd_nl

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/channels/nutrients.cha/alg_shd_nl -->

The light extinction coefficient, $k_l$, is calculated as a function of the algal density using the nonlinear equation:

$k_l=k_{l,0}+k_{l,1}*\alpha_0*algae+k_{l,2}*(\alpha_0*algae)^{2/3}$

where $k_{l,0}$ is the non-algal portion of the light extinction coefficient ($m^{-1}$), $k_{l,1}$ is the linear algal self shading coefficient ($m^{-1}(\mu g - chla/L)^{-1})$, $k_{l,2}$ is the nonlinear algal self shading coefficient $m^{-1}(\mu g - chla/L)^{-2/3})$, $\alpha_0$is the ratio of chlorophyll *a* to algal biomass ($\mu g$ chla/mg alg), and $algae$ is the algal biomass concentration (mg alg/L).

This equation allows a variety of algal, self-shading, light extinction relationships to be modeled. When both $k_{l,1}$ and $k_{l,2}$ are set to 0, no algal self-shading is simulated. When $k_{l,1}$ is set to a value other than 0 and $k_{l,2}$ is set to 0, linear algal self-shading is modeled. When both $k_{l,1}$ and $k_{l,2}$ are set to a value other than 0, non-linear algal self-shading is modeled.

The Riley equation (Bowie et al., 1985) defines $k_{l,1} = 0.0088 m^{-1}(\mu g - chla/L)^{-1}$ and $k_{l,2} = 0.054 m^{-1}(\mu g - chla/L)^{-2/3})$.

#### Relevant chapter in the Theoretical Documentation:

[Local Specific Growth Rate of Algae](https://swatplus.gitbook.io/io-docs/theoretical-documentation/section-7-main-channel-processes/in-stream-nutrient-processes/algae/algal-growth/local-specific-growth-rate-of-algae)

#### References

> Bowie, G.L., W.B. Mills, D.B. Porcella, C.L. Campbell, J.R. Pagenkopt, G.L. Rupp, K.M. Johnson, P.W.H. Chan, and S.A. Gherini. 1985. Rates, constants, and kinetic formulations in surface water quality modeling, 2nd ed. EPA/600/3-85/040, U.S. Environmental Protection Agency, Athens, GA.

Last updated 1 year ago
