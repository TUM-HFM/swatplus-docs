# urb_ro

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/landuse-and-management/landuse.lum/urb_ro-1 -->

Most large watersheds and river basins contain areas of urban land use. Estimates of the quantity and quality of runoff in urban areas are required for comprehensive management analysis. SWAT+ calculates runoff from urban areas with the SCS curve number method or the Green & Ampt equation. Loadings of sediment and nutrients are determined using one of two options. The first is a set of linear regression equations developed by the USGS (Driver and Tasker, 1988) for estimating storm runoff volumes and constituent loads. The other option is to simulate the build-up and wash-off mechanisms, similar to SWMM (Storm Water Management Model; Huber and Dickinson, 1988).

| Option           | Description                 |
| ---------------- | --------------------------- |
| usgs\_reg        | USGS regression equations   |
| buildup\_washoff | build-up/wash-off algorithm |

#### References

> Driver and Tasker (1988)
>
> Huber and Dickinson (1988)

Last updated 1 year ago
