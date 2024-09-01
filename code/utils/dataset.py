import os
import pandas
import geopandas
import pyproj as geo_utils
import utils.geodata as geodata_utils
import time
# sample data:   
# UserId          CheckinTime  VenueId   VenueType             X             Y
# 0       0  2019-07-01T02:05:00      169   Workplace -1.526486e+06  1.529456e+07
# 1       1  2019-07-01T03:10:00      169   Workplace -1.526486e+06  1.529456e+07
# 2       6  2019-07-01T04:30:00      169   Workplace -1.526486e+06  1.529456e+07
# 3      24  2019-07-01T06:25:00      194  Restaurant -1.505625e+06  1.530512e+07
# 4     102  2019-07-01T06:25:00      190  Restaurant -1.502897e+06  1.529984e+07

def concatenate_files(files, uid='UserId', crs="EPSG:26916",standardize=False,output_dir="temp"):
   
    print(f"Concatenating {len(files)} files...")
    result = pandas.DataFrame()
    output_dir = "temp"
    os.makedirs(output_dir, exist_ok=True)
    id_counter = 0
    for file in files:
        try:
            file_df = pandas.read_csv(file, sep="\t")
            print(f"File {file} has {len(file_df)} rows")
            print(file_df.head())
            file_df[uid] = file_df[uid] + id_counter
            id_counter = file_df[uid].max() + 1
            if standardize:
                file_df = get_standard_df(file_df, crs=crs)  
            result = pandas.concat([result, file_df])
        except Exception as e:
            print(f"Error in file {file}: {e}")
            continue

    if standardize:
        output_path = f"{output_dir}/concatenated_standard.csv"
        result.to_csv(output_path, index=False)
    else:
        output_path = f"{output_dir}/concatenated_legacy.tsv"
        result.to_csv(output_path,sep="\t", index=False)

    return output_path
        
def get_standard_df(df, crs="EPSG:26916"):
    df = df.rename(columns={"X": "Longitude", "Y": "Latitude"})
    df["VenueId"] = df["VenueId"].astype(str)
    df["VenueType"] = df["VenueType"].astype(str)
    df["UserId"] = df["UserId"].astype(str)
    df["Longitude"] = df["Longitude"].astype(float)
    df["Latitude"] = df["Latitude"].astype(float)
    #conver to GPS
    df = convert_to_gps(df)
    return df

def convert_to_gps(df, crs="EPSG:26916"):
    print(f"Converting {len(df)} coordinates to GPS...")
    df["Longitude"], df["Latitude"] = geodata_utils.convert_coordinate(df["Longitude"], df["Latitude"], target_crs="EPSG:4326", source_crs=crs)
    return df



