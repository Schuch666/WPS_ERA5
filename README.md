# WPS_ERA5
Documentation to use ERA5 data in WPS

## 1. Download inputs using Python:
   
## 2. Process using WPS:

### a. GEOGRID

Create a namelist with the simulation information and run geogrid.exe (no modifications are needed)

`cd geogrid; ln -sf GEOGRID.TBL.ARW_CHEM GEOGRID.TBL; cd ..`

`./ungrib.exe`

### b. UNGRIB for PRESSURE LEVEL 

link the variable table for *pressure level* (or change to *model level*) and *pressure level* inputs using link_grib.csh

`ln -sf ungrib/Variable_Tables/Vtable.ERA-interim.pl Vtable`

`./link_grib.csh /scratch/${USER}/DATA/ERA5/level.grib .`

change &ungrib session of the namelist.wps to produce PL files

```
&ungrib
 out_format = 'WPS',
 prefix = 'PL',
/
```

run ungrib.exe:

`./ungrib.exe`

### c. UNGRIB for SURFACE LEVEL

link the inputs for *surface level* using link_grib.csh

`./link_grib.csh /scratch/${USER}/DATA/ERA5/single.grib .`

change &ungrib session of the namelist.wps to produce SFC files

```
\&ungrib
 out_format = 'WPS',
 prefix = 'SFC',
/
```

run ungrib.exe:

`./ungrib.exe`

### d. METGRID

run metgrid.exe to combine `PL` and `SFC` in `met_em` files

```
&metgrid
 fg_name = 'SFC', 'PL'
 io_form_metgrid = 2,
/
```

run metgrid.exe:

`./metgrid.exe`

----------------------------

Info:
Access to ERA5 surface data: cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=form
Access to ERA5 pressure level data: cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-pressure-levels?tab=form
Access to CDS API (python module to get ERA5 data): cds.climate.copernicus.eu/api-how-to
Access to ERA5 download codes to run the WRF model: github.com/anikfal/atmospheric_science/tree/main

----------------------

Additional information:

ERA5 download page: https://cds.climate.copernicus.eu/requests?tab=all

ERA5 download API: https://cds.climate.copernicus.eu/how-to-api

Video tutorial: https://www.youtube.com/watch?v=M91ec7EdCic
