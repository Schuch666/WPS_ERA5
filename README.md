# WPS_ERA5
Documentation to use ERA5 data in WPS

## 1. Download inputs using Python:
   
## 2. Process using WPS:

### a. Create a namelist with the simulation information and run geogrid.exe (no modifications are needed)

`cd geogrid; ln -sf GEOGRID.TBL.ARW_CHEM GEOGRID.TBL; cd ..`

`./ungrib.exe`

### b. link the inputs for *pressure level* using link_grib.csh

`./link_grib.csh /scratch/${USER}/DATA/ERA5/level.grib .`

change &ungrib session of the namelist.wps to produce PL files

```
&ungrib
 out_format = 'WPS',
 prefix = 'PL',
/
```

run ungrib.exe

`./ungrib.exe`

### c. link the inputs for *surface level* using link_grib.csh

`./link_grib.csh /scratch/${USER}/DATA/ERA5/single.grib .`

change &ungrib session of the namelist.wps to produce SFC files

```
\&ungrib
 out_format = 'WPS',
 prefix = 'SFC',
/
```

run ungrib.exe

`./ungrib.exe`

### d. run ungrib.exe to combine `PL` and `SFC` in `met_em` files

```
&metgrid
 fg_name = 'SFC', 'PL'
 io_form_metgrid = 2,
/
```

run metgrid.exe

`./metgrid.exe`

----------------------------

Info:
Access to ERA5 surface data: cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=form
Access to ERA5 pressure level data: cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-pressure-levels?tab=form
Access to CDS API (python module to get ERA5 data): cds.climate.copernicus.eu/api-how-to
Access to ERA5 download codes to run the WRF model: github.com/anikfal/atmospheric_science/tree/main

This is some notes from internet (will remove):
ERA5 data on single level (ERA5 atmospheric surface analysis [GRIB1])
https://rda.ucar.edu/datasets/ds633.0/index.html#sfol-wl-/data/ds633.0?g=9
download for all variable for your required time and save them in a fordel named ERA5_SURFACE


ERA5 data on pressure levels (ERA5 atmospheric pressure level analysis [GRIB1])
https://rda.ucar.edu/datasets/ds633.0/index.html#sfol-wl-/data/ds633.0?g=6
download for all variable for your required time and save them in a folder named ERA5_PRESSURE

first in WPS in namelist.wps

&ungrib
 out_format = 'WPS',
 prefix = 'SFC',
/

and link only the *SURFACE.grib files and do ./ungrib.exe
this will prepare the files with name of SFC

second in WPS in namelist.wps


and link only the *PRESSURE.grib files and do ./ungrib.exe
this will prepare the files with name of PL

Then do ./geogrid.exe and ./metgrid.exe using the namelist.wps I am sharing as there is the below thing mentioned

&metgrid
 fg_name = 'SFC', 'PL'
 io_form_metgrid = 2,
 opt_output_from_metgrid_path = '/home/cas/phd/asz198067/scratch/FDDA_TEST/',

/

----------------------

Additional information:

ERA5 download page: https://cds.climate.copernicus.eu/requests?tab=all

ERA5 download API: https://cds.climate.copernicus.eu/how-to-api

Video tutorial: https://www.youtube.com/watch?v=M91ec7EdCic
