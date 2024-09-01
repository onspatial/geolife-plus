import pandas
import geopandas
import utils.geo.point as point_utils
import utils.geo.info as info_utils
from pyproj import Transformer


def convert_to_gps(input_df, lat_col=1, lon_col=2, crs_from=info_utils.get_csr(map_name='bjng'), crs_to="epsg:4326"):
    input_df_columns = input_df.columns
    if lat_col == lon_col:
        input_df['Latitude'] = point_utils.get_latitudes(input_df[input_df_columns[lat_col]])
        input_df['Longitude'] = point_utils.get_longitudes(input_df[input_df_columns[lon_col]])
        input_df = input_df.drop(input_df_columns[lat_col], axis=1)
    else: 
        input_df = input_df.rename(columns={input_df_columns[lat_col]:'Latitude', input_df_columns[lon_col]:'Longitude'})

    input_df['Latitude'], input_df['Longitude'] = convert_coordinate_system(input_df['Latitude'], input_df['Longitude'], from_crs=crs_from, to_crs=crs_to, inplace=True)
    return input_df

def convert_coordinate_system(latitude, longitude, from_crs=info_utils.get_csr(map_name='bjng'), to_crs="epsg:4326", inplace=False):
    transformer = Transformer.from_crs(from_crs, to_crs)
    print(f"Transforming from {from_crs} to {to_crs}")
    return transformer.transform(latitude, longitude, inplace=inplace)

def convert_to_datetime(input_df, time_col=1):
    input_df_columns = input_df.columns
    input_df['Time'] = pandas.to_datetime(input_df[input_df_columns[time_col]])
    return input_df