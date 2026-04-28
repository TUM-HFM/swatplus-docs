# Master File (file.cio)

<!-- Source: https://swatplus.gitbook.io/io-docs/introduction-1/master-file-file.cio -->

This file lists the names of all input files used in a simulation run. The files are grouped in different categories and there is one line for each category. The first column lists the names of the categories. The number of columns per line depends on the number of files in a category. Most files are required for all SWAT+ runs, i.e. they have to be listed in file.cio and the corresponding file has to be present in the TxtInOut folder of the SWAT+ project. There are also some optional files that are only required for specific SWAT+ applications. The category names and their files are listed below.

#### Simulation

1. [time.sim](simulation-settings/time.sim.md)
2. [print.prt](simulation-settings/print.prt.md)
3. [object.prt](simulation-settings/object.prt.md)
4. [object.cnt](simulation-settings/object.cnt.md)
5. constituents.cs

#### Basin

1. [codes.bsn](basin-1/codes.bsn.md)
2. [parameters.bsn](basin-1/parameters.bsn.md)

#### Climate

1. [weather-sta.cli](climate/weather-sta-cli.md)
2. [weather-wgn.cli](climate/weather-wgn-cli.md)
3. wind-dir.cli (currently not used)
4. [pcp.cli](climate/pcp-cli.md)
5. [tmp.cli](climate/tmp-cli.md)
6. [slr.cli](climate/slr-cli.md)
7. [hmd.cli](climate/hmd-cli.md)
8. [wnd.cli](climate/wnd-cli.md)
9. [atmo.cli](climate/atmo-cli.md)

#### Connect

1. [hru.con](connectivity/hru.con.md)
2. [hru-lte.con](connectivity/hru.con.md)
3. [rout\_unit.con](connectivity/hru.con.md)
4. gwflow.con (a description of the gwflow module and all related input files will be added asap)
5. [aquifer.con](connectivity/hru.con.md)
6. aquifer2d.con (currently not used)
7. channel.con (currently not used)
8. [reservoir.con](connectivity/hru.con.md)
9. [recall.con](connectivity/hru.con.md)
10. [exco.con](connectivity/hru.con.md)
11. [delratio.con](connectivity/hru.con.md)
12. [outlet.con](connectivity/hru.con.md)
13. [chandeg.con](connectivity/hru.con.md)

#### Channel

1. [initial.cha](channels/initial.cha.md)
2. channel.cha (currently not used)
3. hydrology.cha (currently not used)
4. sediment.cha (currently not used)
5. [nutrients.cha](channels/nutrients.cha.md)
6. [channel-lte.cha](channels/channel-lte.cha.md)
7. [hyd-sed-lte.cha](channels/hyd-sed-lte.cha.md)
8. temperature.cha

#### Reservoir

1. [initial.res](reservoirs/initial.res.md)
2. [reservoir.res](reservoirs/reservoir.res.md)
3. [hydrology.res](reservoirs/hydrology.res.md)
4. [sediment.res](reservoirs/sediment.res.md)
5. [nutrients.res](reservoirs/nutrients.res.md)
6. [weir.res](reservoirs/weir.res.md)
7. [wetland.wet](wetlands/wetland.wet.md)
8. [hydrology.wet](wetlands/hydrology.wet.md)

#### Routing Unit

1. [rout\_unit.def](routing-units/untitled-1.md)
2. [rout\_unit.ele](routing-units/untitled-2.md)
3. [rout\_unit.rtu](routing-units/untitled.md)
4. rout\_unit.dr (currently not used)

#### HRU

1. [hru-data.hru](hydrologic-response-units/hru-data.hru.md)
2. [hru-lte.hru](hydrologic-response-units/hru-lte.hru.md)

#### Export Coefficient

1. exco.exc
2. exco\_om.exc
3. exco\_pest.exc (currently not used)
4. exco\_path.exc (currently not used)
5. exco\_hmet.exc (currently not used)
6. exco\_salt.exc (currently not used)

#### Recall

1. recall.rec

#### Delivery Ratio

1. del\_ratio.del (currently not used)
2. dr\_om.del (currently not used)
3. dr\_pest.del (currently not used)
4. dr\_path.del (currently not used)
5. dr\_hmet.del (currently not used)
6. dr\_salt.del (currently not used)

The delivery ratio files will be removed in future versions of SWAT+.

#### Aquifer

1. [initial.aqu](aquifers/initial.aqu.md)
2. [aquifer.aqu](aquifers/aquifer.aqu.md)

#### Herd

1. animal.hrd (currently not used)
2. herd.hrd (currently not used)
3. ranch.hrd (currently not used)

There are no plans to work on the animal herd module in the foreseeable future unless there is a demand for it in the user community.

#### Water Rights

1. water\_allocation.wro

The SWAT+ Water Allocation Module is work in progress and not fully functional in the current revision. A description of the general approach as well as input/output files will be added before the release of the next SWAT+ revision.

#### Link

1. chan-surf.lin
2. aqu\_cha.lin

#### Hydrology

1. [hydrology.hyd](hydrology/hydrology.hyd.md)
2. [topography.hyd](hydrology/topography.hyd.md)
3. [field.fld](hydrology/field.fld.md)

#### Structural

1. [tiledrain.str](structural-practices/tiledrain.str.md)
2. [septic.str](structural-practices/septic.str.md)
3. [filterstrip.str](structural-practices/filterstrip.str.md)
4. [grassedww.str](structural-practices/grassedww.str.md)
5. [bmpuser.str](structural-practices/bmpuser.str.md)

#### HRU Databases

1. [plants.plt](databases/plants.plt.md)
2. [fertilizer.frt](databases/fertilizer.frt.md)
3. [tillage.til](databases/tillage.til.md)
4. [pesticide.pes](databases/pesticide.pes.md)
5. pathogens.pth (currently not used)
6. metals.mtl (currently not used)
7. salt.slt (currently not used)
8. [urban.urb](databases/urban.urb.md)
9. [septic.sep](databases/septic.sep.md)
10. [snow.sno](hydrology/snow.sno.md)

The salt routines are work in progress and will be added soon. However, there are no plans to work on the pathogen and metal routines in the foreseeable future unless there is a demand for it in the user community.

#### Operation Scheduling

1. [harv.ops](management-practices/harv.ops.md)
2. [graze.ops](management-practices/graze.ops.md)
3. [irr.ops](management-practices/irr.ops.md)
4. [chem\_app.ops](management-practices/chem_app.ops.md)
5. [fire.ops](management-practices/fire.ops.md)
6. [sweep.ops](management-practices/sweep.ops.md)

#### Land Use Management

1. [landuse.lum](landuse-and-management/landuse.lum.md)
2. [management.sch](landuse-and-management/management.sch.md)
3. [cntable.lum](landuse-and-management/cntable.lum.md)
4. [cons\_practice.lum](landuse-and-management/cons_practice.lum.md)
5. [ovn\_table.lum](landuse-and-management/ovn_table.lum.md)

#### Change

1. cal\_parms.cal
2. calibration.cal
3. codes.sft
4. wb\_parms.sft
5. water\_balance.sft
6. ch\_sed\_budget.sft (currently not used)
7. ch\_sed\_parms.sft (currently not used)
8. plant\_parms.sft
9. plant\_gro.sft

#### Initial

1. [plant.ini](landuse-and-management/plant.ini.md)
2. [soil\_plant.ini](initialization/soil_plant.ini.md)
3. om\_water.ini
4. pest\_hru.ini
5. pest\_water.ini
6. path\_hru.ini (currently not used)
7. path\_water.ini (currently not used)
8. hmet\_hru.ini (currently not used)
9. hmet\_water.ini (currently not used)
10. salt\_hru.ini (currently not used)
11. salt\_water.ini (currently not used)

#### Soils

1. [soils.sol](soils/soils.sol.md)
2. [nutrients.sol](soils/nutrients.sol.md)
3. soils\_lte.sol (currently not used)

#### Conditional

1. [lum.dtl](decision-tables/lum.dtl.md)
2. res\_rel.dtl
3. scen\_lu.dtl
4. flo\_con.dtl

#### Regions

1. [ls\_unit.ele](landscape-units/ls_unit.ele.md)
2. [ls\_unit.def](landscape-units/ls_unit.def.md)
3. ls\_reg.ele
4. ls\_reg.def
5. ls\_cal.reg
6. ch\_catunit.ele
7. ch\_catunit.def
8. ch\_reg.def
9. aqu\_catunit.ele
10. aqu\_catunit.def
11. aqu\_reg.def
12. res\_catunit.ele
13. res\_catunit.def
14. res\_reg.def
15. rec\_catunit.ele
16. rec\_catunit.def
17. rec\_reg.def

The definition of regions in SWAT+ besides the Landscape Units will be revised in the near future and a description of the region files will be added to this documentation as soon as that has happened.

The last five rows in file.cio are used to specify the climate file directories if these are stored in a folder other than the project TxtInOut folder.

Last updated 1 year ago
