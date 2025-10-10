import cdsapi
from datetime import datetime, timedelta

c = cdsapi.Client()

# Loop through days 1-2 of August 2019
start_date = datetime(2019, 8, 1)
end_date = datetime(2019, 8, 2)

current_date = start_date
while current_date <= end_date:
    # Format date strings
    year = current_date.strftime('%Y')
    month = current_date.strftime('%m')
    day = current_date.strftime('%d')
    date_str = current_date.strftime('%Y-%m-%d')
    
    # Output filename
    output_file = f'ERA5_surface_{date_str}.grib'
    
    print(f'Downloading surface data for {date_str}...')
    
    try:
        c.retrieve(
            'reanalysis-era5-single-levels',
            {
                'product_type': 'reanalysis',
                'variable': [
                    '10m_u_component_of_wind', '10m_v_component_of_wind', '2m_dewpoint_temperature',
                    '2m_temperature', 'geopotential', 'land_sea_mask',
                    'leaf_area_index_high_vegetation', 'mean_sea_level_pressure', 'sea_ice_cover',
                    'sea_surface_temperature', 'snow_depth', 'soil_temperature_level_1',
                    'soil_temperature_level_2', 'soil_temperature_level_3', 'soil_temperature_level_4',
                    'soil_type', 'surface_latent_heat_flux', 'surface_pressure',
                    'top_net_solar_radiation_clear_sky', 'total_precipitation', 'volumetric_soil_water_layer_1',
                    'volumetric_soil_water_layer_2', 'volumetric_soil_water_layer_3', 'volumetric_soil_water_layer_4',
                    'skin_temperature',
                ],
                'year': year,
                'month': month,
                'day': day,
                'time': [
                    '00:00', '03:00', '06:00', '09:00', 
                    '12:00', '15:00', '18:00', '21:00',
                ],
                'format': 'grib',  # Keeping GRIB format
            },
            output_file)
        
        print(f'Successfully downloaded {output_file}')
        
    except Exception as e:
        print(f'Error downloading data for {date_str}: {e}')
    
    # Move to next day
    current_date += timedelta(days=1)

print('Download complete for surface variables')
