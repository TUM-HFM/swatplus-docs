# name (cntable.lum)

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/landuse-and-management/cntable.lum/name_cn -->

The name of the Curve Number class is a primary key referenced by [cn2](../landuse.lum/cn2.md) in [**landuse.lum**](../landuse.lum.md). All names in the **cntable.lum** file must be unique.

The name describes the land use type, treatment, and cover condition the Curve Number Values are valid for.

| Name             | Land use type                                                   | Treatment                           | Cover condition |
| ---------------- | --------------------------------------------------------------- | ----------------------------------- | --------------- |
| fal\_bare        | Fallow                                                          | Bare soil                           |                 |
| fal\_res\_p      | Fallow                                                          | Crop residue                        | Poor            |
| fal\_res\_g      | Fallow                                                          | Crop residue                        | Good            |
| rc\_strow\_p     | Row Crops                                                       | Straight row                        | Poor            |
| rc\_strow\_g     | Row Crops                                                       | Straight row                        | Good            |
| rc\_strowres\_p  | Row Crops                                                       | Straight row with residue           | Poor            |
| rc\_strowres\_g  | Row Crops                                                       | Straight row with residue           | Good            |
| rc\_cont\_p      | Row Crops                                                       | Contoured                           | Poor            |
| rc\_cont\_g      | Row Crops                                                       | Contoured                           | Good            |
| rc\_contres\_p   | Row Crops                                                       | Contoured with residue              | Poor            |
| rc\_contres\_g   | Row Crops                                                       | Contoured with residue              | Good            |
| rc\_contter\_p   | Row Crops                                                       | Contoured and terraced              | Poor            |
| rc\_contter\_g   | Row Crops                                                       | Contoured and terraced              | Good            |
| rc\_conterres\_p | Row Crops                                                       | Contoured and terraced with residue | Poor            |
| rc\_conterres\_g | Row Crops                                                       | Contoured and terraced with residue | Good            |
| sg\_strow\_p     | Small Grains                                                    | Straight row                        | Poor            |
| sg\_strow\_g     | Small Grains                                                    | Straight row                        | Good            |
| sg\_strowres\_p  | Small Grains                                                    | Straight row with residue           | Poor            |
| sg\_strowres\_g  | Small Grains                                                    | Straight row with residue           | Good            |
| sg\_cont\_p      | Small Grains                                                    | Contoured                           | Poor            |
| sg\_cont\_g      | Small Grains                                                    | Contoured                           | Good            |
| sg\_contres\_p   | Small Grains                                                    | Contoured with residue              | Poor            |
| sg\_contres\_g   | Small Grains                                                    | Contoured with residue              | Good            |
| sg\_contter\_p   | Small Grains                                                    | Contoured and terraced              | Poor            |
| sg\_contter\_g   | Small Grains                                                    | Contoured and terraced              | Good            |
| sg\_conterres\_p | Small Grains                                                    | Contoured and terraced with residue | Poor            |
| sg\_conterres\_g | Small Grains                                                    | Contoured and terraced with residue | Good            |
| legr\_strow\_p   | Close-seeded or Broadcast Legumes or Rotation                   | Straight row                        | Poor            |
| legr\_strow\_g   | Close-seeded or Broadcast Legumes or Rotation                   | Straight row                        | Good            |
| legr\_cont\_p    | Close-seeded or Broadcast Legumes or Rotation                   | Contoured                           | Poor            |
| legr\_cont\_g    | Close-seeded or Broadcast Legumes or Rotation                   | Contoured                           | Good            |
| legr\_contter\_p | Close-seeded or Broadcast Legumes or Rotation                   | Contoured and terraced              | Poor            |
| legr\_contter\_g | Close-seeded or Broadcast Legumes or Rotation                   | Contoured and terraced              | Good            |
| pastg\_p         | Pasture, grassland, or range                                    | ---                                 | Poor            |
| pastg\_f         | Pasture, grassland, or range                                    | ---                                 | Fair            |
| pastg\_g         | Pasture, grassland, or range                                    | ---                                 | Good            |
| pasth            | Meadow or continuous grass, no grazing, mowed for hay           | ---                                 | ---             |
| brush\_p         | Brush-weed-grass mixture with brush the major element           | ---                                 | Poor            |
| brush\_f         | Brush-weed-grass mixture with brush the major element           | ---                                 | Fair            |
| brush\_g         | Brush-weed-grass mixture with brush the major element           | ---                                 | Good            |
| woodgr\_p        | Woods-grass combination (orchard or tree farm)                  | ---                                 | Poor            |
| woodgr\_f        | Woods-grass combination (orchard or tree farm)                  | ---                                 | Fair            |
| woodgr\_g        | Woods-grass combination (orchard or tree farm)                  | ---                                 | Good            |
| wood\_p          | Forest                                                          | ---                                 | Poor            |
| wood\_f          | Forest                                                          | ---                                 | Fair            |
| wood\_g          | Forest                                                          | ---                                 | Good            |
| farm             | Farmsteads (buildings, lanes, driveways, and surrounding lots)  | ---                                 | ---             |
| open\_p          | Open spaces (lawns, parks, golf courses, cemeteries, etc.)      | ---                                 | Poor            |
| urban            | Paved parking lots, roofs, driveways, etc. (excl. right-of-way) | ---                                 | ---             |
| paveroad         | Paved streets and roads, open ditches (incl. right-of-way)      | ---                                 | ---             |
| gravroad         | Gravel streets and roads (incl. right-of-way)                   | ---                                 | ---             |
| dirtroad         | Dirt streets and roads (incl. right-of-way)                     | ---                                 | ---             |

Last updated 1 year ago
