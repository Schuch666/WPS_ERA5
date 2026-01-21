import cdsapi
from datetime import datetime, timedelta

c = cdsapi.Client()

# Loop through all days in August 2019
start_date = datetime(2019, 8, 1)
end_date = datetime(2019, 8, 31)

current_date = start_date
while current_date <= end_date:
    # Format date strings
    year = current_date.strftime('%Y')
    month = current_date.strftime('%m')
    day = current_date.strftime('%d')
    date_str = current_date.strftime('%Y-%m-%d')
    
    # Output filename
    output_file = f'ERA5_RAIN_{date_str}.nc'
    
    print(f'Downloading data for {date_str}...')
    
    try:
        c.retrieve(
            'reanalysis-era5-single-levels',
            {
                'product_type': 'reanalysis',
                'variable': 'total_precipitation',
                'year': year,
                'month': month,
                'day': day,
                'time': [
                    '00:00', '01:00', '02:00', '03:00', '04:00', '05:00',
                    '06:00', '07:00', '08:00', '09:00', '10:00', '11:00',
                    '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
                    '18:00', '19:00', '20:00', '21:00', '22:00', '23:00',
                ],
                'format': 'netcdf',
            },
            output_file)
        
        print(f'Successfully downloaded {output_file}')
        
    except Exception as e:
        print(f'Error downloading data for {date_str}: {e}')
    
    # Move to next day
    current_date += timedelta(days=1)

print('Download complete for all days in August 2019')
