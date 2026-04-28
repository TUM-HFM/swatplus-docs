# lt_nonalg

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/channels/nutrients.cha/lt_nonalg -->

The light extinction coefficient, $k_l$, is calculated as a function of the algal density using the nonlinear equation:

$k_l=k_{l,0}+k_{l,1}*\alpha_0*algae+k_{l,2}*(\alpha_0*algae)^{2/3}$

where $k_{l,0}$ is the non-algal portion of the light extinction coefficient ($m^{-1}$), $k_{l,1}$ is the linear algal self shading coefficient ($m^{-1}(\mu g - chla/L)^{-1})$, $k_{l,2}$ is the nonlinear algal self shading coefficient $m^{-1}(\mu g - chla/L)^{-2/3})$, $\alpha_0$is the ratio of chlorophyll *a* to algal biomass ($\mu g$ chla/mg alg), and $algae$ is the algal biomass concentration (mg alg/L).

#### Relevant chapter in the Theoretical Documentation:

[Local Specific Growth Rate of Algae](https://swatplus.gitbook.io/io-docs/theoretical-documentation/section-7-main-channel-processes/in-stream-nutrient-processes/algae/algal-growth/local-specific-growth-rate-of-algae)

Last updated 1 year ago
