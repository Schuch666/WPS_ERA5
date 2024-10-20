# WPS_ERA5
documentation to use ERA5 data in WPS

DATA: https://cds.climate.copernicus.eu/requests?tab=all
API: https://cds.climate.copernicus.eu/how-to-api

Video with tutorial: https://www.youtube.com/watch?v=M91ec7EdCic
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

&ungrib
 out_format = 'WPS',
 prefix = 'PL',
/

and link only the *PRESSURE.grib files and do ./ungrib.exe
this will prepare the files with name of PL

Then do ./geogrid.exe and ./metgrid.exe using the namelist.wps I am sharing as there is the below thing mentioned

&metgrid
 fg_name = 'SFC', 'PL'
 io_form_metgrid = 2,
 opt_output_from_metgrid_path = '/home/cas/phd/asz198067/scratch/FDDA_TEST/',

/

