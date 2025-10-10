import cdsapi
from datetime import datetime, timedelta

c = cdsapi.Client()

# Loop through days 3-4 of August 2019
start_date = datetime(2019, 8, 3)
end_date = datetime(2019, 8, 4)

current_date = start_date
while current_date <= end_date:
    # Format date strings
    year = current_date.strftime('%Y')
    month = current_date.strftime('%m')
    day = current_date.strftime('%d')
    date_str = current_date.strftime('%Y-%m-%d')
    
    # Download surface variables
    surface_file = f'ERA5_surface_{date_str}.grib'
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
                'format': 'grib',
            },
            surface_file)
        
        print(f'Successfully downloaded {surface_file}')
        
    except Exception as e:
        print(f'Error downloading surface data for {date_str}: {e}')
    
    # Download pressure level variables
    pressure_file = f'ERA5_pressure_{date_str}.grib'
    print(f'Downloading pressure level data for {date_str}...')
    
    try:
        c.retrieve(
            'reanalysis-era5-pressure-levels',
            {
                'product_type': 'reanalysis',
                'variable': [
                    'geopotential', 'relative_humidity', 'specific_humidity',
                    'temperature', 'u_component_of_wind', 'v_component_of_wind',
                ],
                'pressure_level': [
                    '1', '2', '3',
                    '5', '7', '10',
                    '20', '30', '50',
                    '70', '100', '125',
                    '150', '175', '200',
                    '225', '250', '300',
                    '350', '400', '450',
                    '500', '550', '600',
                    '650', '700', '750',
                    '775', '800', '825',
                    '850', '875', '900',
                    '925', '950', '975',
                    '1000',
                ],
                'year': year,
                'month': month,
                'day': day,
                'time': [
                    '00:00', '03:00', '06:00', '09:00', 
                    '12:00', '15:00', '18:00', '21:00',
                ],
                'format': 'grib',
            },
            pressure_file)
        
        print(f'Successfully downloaded {pressure_file}')
        
    except Exception as e:
        print(f'Error downloading pressure data for {date_str}: {e}')
    
    print(f'Completed downloads for {date_str}\n')
    
    # Move to next day
    current_date += timedelta(days=1)

print('Download complete for all surface and pressure level variables')
