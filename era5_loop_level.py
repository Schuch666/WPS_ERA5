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
    output_file = f'ERA5_pressure_{date_str}.grib'
    
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
            output_file)
        
        print(f'Successfully downloaded {output_file}')
        
    except Exception as e:
        print(f'Error downloading data for {date_str}: {e}')
    
    # Move to next day
    current_date += timedelta(days=1)

print('Download complete for pressure level variables')
