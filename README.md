# WPS_ERA5
Documentation to use ERA5 data in WPS

## 1. Download inputs using Python:
### a. Download and install [miniconda](https://docs.anaconda.com/miniconda)
```
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```
After the conda installation
```
source ~/miniconda3/bin/activate
```
To initiallize conda
```
conda init --all
```
### b. Create a python environment called py311 and install the python cdsapi package:
```
conda create -n py311 python=3.11
conda activate py311
pip install 'cdsapi>=0.7.2'
```
### c. Copy the credentials

Register/login in [cdc site](https://cds.climate.copernicus.eu/how-to-api) and copy and paste the `url:xxx and key:yyy` in a configuration file.

`nano $HOME/.cdsapirc`

### d. Download *pressure level* ERA5

Change the `era5_level.py` python script
```
conda activate py311
python 
```

### e. Download *surface level* ERA5

Change the `era5_surface.py` python script
```
conda activate py311
python 
```

## 2. Process using WPS:

### a. GEOGRID

Create a namelist with the simulation information and run geogrid.exe (no modifications are needed)

`cd geogrid; ln -sf GEOGRID.TBL.ARW_CHEM GEOGRID.TBL; cd ..`

`./ungrib.exe`

### b. UNGRIB for *pressure level* 

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

### c. UNGRIB for *surface level*

link the inputs for *surface level* using link_grib.csh

`./link_grib.csh /scratch/${USER}/DATA/ERA5/single.grib .`

change &ungrib session of the namelist.wps to produce SFC files

```
&ungrib
 out_format = 'WPS',
 prefix = 'SFC',
/
```

run ungrib.exe:

`./ungrib.exe`

### d. METGRID for *pressure level* and *surface level*

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

Additional information:

Miniconda download and documentaion: https://docs.anaconda.com/miniconda

WRF documentaion page: https://www2.mmm.ucar.edu/wrf/users/docs/user_guide_v4/contents.html

ERA5 download API page: https://cds.climate.copernicus.eu/how-to-api

ERA5 download page: https://cds.climate.copernicus.eu/requests?tab=all

Video tutorial: https://www.youtube.com/watch?v=M91ec7EdCic
