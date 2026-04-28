# q2e_alg

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/channels/nutrients.cha/q2e_alg -->

Qual2E provides three different options for computing the algal growth rate:

1. Multiplicative: The multiplicative option multiplies the growth factors for light, nitrogen and phosphorus together to determine their net effect on the local algal growth rate. This option has its biological basis in the multiplicative effects of enzymatic processes involved in photosynthesis.
2. Limiting nutrient: The limiting nutrient option calculates the local algal growth rate as limited by light and either nitrogen or phosphorus. The nutrient/light effects are multiplicative, but the nutrient/nutrient effects are alternate. The algal growth rate is controlled by the nutrient with the smaller growth limitation factor. This approach mimics Liebig’s law of the minimum.
3. Harmonic mean: The harmonic mean is mathematically analogous to the total resistance of two resistors in parallel and can be considered a compromise between the multiplicative and limiting nutrient options. The algal growth rate is controlled by a multiplicative relation between light and nutrients, while the nutrient/nutrient interactions are represented by a harmonic mean.

Last updated 1 year ago
