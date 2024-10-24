import cdsapi

c = cdsapi.Client()

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
        'year': '2023',
        'month': '01',
        'day': [
            '21', '22',
        ],
        'time': [
            '00:00', '06:00',
            '12:00', '18:00',
        ],
        'format': 'grib',
    },
    'single.grib')
