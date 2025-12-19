#!/bin/bash
set -euo pipefail

# TIME FORMAT YYY-MM-DD_HH:mm:ss
START_DATE="2023-03-22 00:00:00"
END_DATE="2023-05-01 00:00:00"
INTERVAL_SECONDS=10800
# Paths
WPS_DIR=$(pwd)
GEOG_PATH="/scratch/schuch/DATA/WPS_GEOG"
ERA5_SFC_DIR="/scratch/schuch/Africa/ERA5/sur_2023-04"
ERA5_PL_DIR="/scratch/schuch/Africa/ERA5/lev_2023-04"
# Vtables for pressure-level data as input
VTABLE_PL="Vtable.ERA-interim.pl"
# Vatebles for model-leval data as input (dontr need to change)
# VTABLE_PL="Vtable.ERA-interim.ml"

VTABLE_SFC=$VTABLE_PL

min_date() {
  [[ "$1" < "$2" ]] && echo "$1" || echo "$2"
}

wps_date() {
  date -u -d "$1" +"%Y-%m-%d_%H:%M:%S"
}

cd "$WPS_DIR"

START_TS=$(date -u -d "$START_DATE" +%s)
END_TS=$(date -u -d "$END_DATE" +%s)
CUR_TS=$START_TS

if [ ! -f geo_em.d01.nc ]; then
  echo "Running geogrid.exe"
  ./geogrid.exe
fi

while [ "$CUR_TS" -lt "$END_TS" ]; do

  CUR_DATE_INT=$(date -u -d "@$CUR_TS" +"%Y-%m-%d %H:%M:%S")

  # End of current month (00 UTC of next month)
  NEXT_MONTH_INT=$(date -u -d "$(date -u -d "$CUR_DATE_INT" +"%Y-%m-01") +1 month" +"%Y-%m-01 00:00:00")

  # Chunk end = min(next month, END_DATE)
  CHUNK_END_INT=$(min_date "$NEXT_MONTH_INT" "$END_DATE")

  # Convert ONLY for WPS
  START_WPS=$(wps_date "$CUR_DATE_INT")
  END_WPS=$(wps_date "$CHUNK_END_INT")

  YM=$(date -u -d "$CUR_DATE_INT" +"%Y%m")

  echo "========================================"
  echo "Processing: $START_WPS → $END_WPS"
  echo "========================================"

  # rm -f FILE:* PFILE:* met_em* namelist.wps

  cat > namelist.wps << EOF
&share
 wrf_core = 'ARW',
 max_dom = 3,
 start_date = '$START_WPS','$START_WPS','$START_WPS',
 end_date   = '$END_WPS','$END_WPS','$END_WPS',
 interval_seconds = $INTERVAL_SECONDS,
/

&geogrid
 parent_id         =   1,   1,   2,
 parent_grid_ratio =   1,   6,   6,
 i_parent_start    =   1, 129, 103,
 j_parent_start    =   1,  84, 153,
 e_we              = 229, 217, 103,
 e_sn              = 162, 199,  79,
 geog_data_res     = '30s','30s','30s',
 dx                = 36000,
 dy                = 36000,
 map_proj          = 'lambert',
 ref_lat           =  20.715,
 ref_lon           =  19.336,
 truelat1          =   0.0,
 truelat2          =  30.0,
 stand_lon         =  22.0,
 geog_data_path    = '$GEOG_PATH'
/

&ungrib
 out_format = 'WPS',
 prefix = 'SFC',
/

&metgrid
 fg_name = 'SFC','PL'
 io_form_metgrid = 2,
/
EOF

  ln -sf ungrib/Variable_Tables/$VTABLE_SFC Vtable
  ./link_grib.csh "$ERA5_SFC_DIR"/*.grib
  ./ungrib.exe

  # rm -f FILE:*

  sed "s/prefix = 'SFC'/prefix = 'PL'/" namelist.wps > namelist.wps.pl
  mv namelist.wps.pl namelist.wps

  ln -sf ungrib/Variable_Tables/$VTABLE_PL Vtable
  ./link_grib.csh "$ERA5_PL_DIR/"/*.grib
  ./ungrib.exe

  ./metgrid.exe

  CUR_TS=$(date -u -d "$CHUNK_END_INT" +%s)

done


echo "WPS ERA5 processing completed successfully."
