# hru-lte.hru

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/hydrologic-response-units/hru-lte.hru -->

| Field                                                                                    | Description                                                                                  | Type    | Unit     | Default      | Range      |
| ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------- | -------- | ------------ | ---------- |
| [id](hru-lte.hru/id-hru-lte.hru.md)       | ID of the HRU-lte                                                                            | integer | n/a      |              |            |
| [name](hru-lte.hru/name_hrulte_db.md)     | Name of HRU-lte                                                                              | string  | n/a      | n/a          | n/a        |
| [area](hru-lte.hru/area.md)               | HRU-lte drainage area                                                                        | real    | km^2     | 0.0          |            |
| [cn2](hru-lte.hru/cn2.md)                 | Condition II Curve Number                                                                    | real    | none     | 80.0         |            |
| [cn3\_swf](hru-lte.hru/cn3_swf.md)        | Soil water factor for CN3                                                                    | real    | none     | 1.0          |            |
| [t\_conc](hru-lte.hru/t_conc.md)          | Time of concentration                                                                        | real    | min      | 26.0         |            |
| [soil\_dp](hru-lte.hru/soil_dp.md)        | Soil profile depth                                                                           | real    | mm       | 1500.0       |            |
| [perco\_co](hru-lte.hru/perco_co.md)      | Soil percolation coefficient                                                                 | real    | none     | 0.0          | 0.0-6000.0 |
| [slp](hru-lte.hru/slp.md)                 | Land surface slope                                                                           | real    | m/m      | 0.04         | 0.0-0.60   |
| [slp\_len](hru-lte.hru/slp_len.md)        | Land surface slope length                                                                    | real    | m        | 64.20        |            |
| [et\_co](hru-lte.hru/et_co.md)            | ET coefficient                                                                               | real    | none     |              |            |
| [aqu\_sp\_yld](hru-lte.hru/aqu_sp_yld.md) | Specific yield of the shallow aquifer                                                        | real    | mm       | 0.05         |            |
| [alpha\_bf](hru-lte.hru/alpha_bf.md)      | Baseflow alpha factor                                                                        | real    |          | 0.05         |            |
| [revap](hru-lte.hru/revap.md)             | Revap coefficient                                                                            | real    | none     | 0.0          |            |
| [rchg\_dp](hru-lte.hru/rchg_dp.md)        | Percolation coefficient from shallow to deep aquifer                                         | real    | none     | 0.01         |            |
| [sw\_init](hru-lte.hru/sw_init.md)        | Initial soil water (fraction of available water capacity)                                    | real    | fraction | 0.50         | 0.0-1.0    |
| [aqu\_init](hru-lte.hru/aqu_init.md)      | Initial shallow aquifer storage                                                              | real    | mm       | 3.00         |            |
| [aqu\_sh\_flo](hru-lte.hru/aqu_sh_flo.md) | Initial shallow aquifer flow                                                                 | real    | mm       | 0.0          |            |
| [aqu\_dp\_flo](hru-lte.hru/aqu_dp_flo.md) | Initial deep aquifer flow                                                                    | real    | mm       | 300.0        |            |
| [snow\_h20](hru-lte.hru/snow_h2o.md)      | Initial snow water equivalent                                                                | real    | mm       | 0.0          |            |
| [lat](hru-lte.hru/lat.md)                 | Latitude                                                                                     | real    |          | 31.60        |            |
| [soil\_text](hru-lte.hru/soil_text.md)    | Soil texture                                                                                 | string  | n/a      | n/a          | n/a        |
| [trop\_flag](hru-lte.hru/trop_flag.md)    | Tropical flag                                                                                | string  | n/a      | non\_trop    | n/a        |
| [grow\_start](hru-lte.hru/grow_start.md)  | Start of growing season for non-tropical/start of monsoon initialization period for tropical | string  | n/a      | n/a          | n/a        |
| [grow\_end](hru-lte.hru/grow_end.md)      | End of growing season for non-tropical/start of monsoon initialization period for tropical   | string  | n/a      | n/a          | n/a        |
| [plnt\_typ](hru-lte.hru/plnt_typ.md)      | Plant type                                                                                   | string  | n/a      | agrl         | n/a        |
| [stress](hru-lte.hru/stress.md)           | Plant stress                                                                                 | real    | fraction | 1            | 0.0-1.0    |
| [pet\_flag](hru-lte.hru/pet_flag.md)      | Potential ET method                                                                          | string  | n/a      | harg         | n/a        |
| [irr\_flag](hru-lte.hru/irr_flag.md)      | Irrigation code                                                                              | string  | n/a      | no\_irr      | n/a        |
| [irr\_src](hru-lte.hru/irr_src.md)        | Irrigation source                                                                            | string  | n/a      | outside\_bsn | n/a        |
| [t\_drain](hru-lte.hru/t_drain.md)        | Design subsurface tile drain time                                                            | real    | hr       | 0.0          |            |
| [usle\_k](hru-lte.hru/usle_k.md)          | USLE soil erodibility factor K                                                               | real    | n/a      | 0.32         |            |
| [usle\_c](hru-lte.hru/usle_c.md)          | USLE cover factor C                                                                          | real    | n/a      | 0.20         |            |
| [usle\_p](hru-lte.hru/usle_p.md)          | USLE support practice factor P                                                               | real    | n/a      | 0.80         |            |
| [usle\_ls](hru-lte.hru/usle_ls.md)        | USLE slope length and slope factor LS                                                        | real    | n/a      | 0.53         |            |

Last updated 1 year ago
