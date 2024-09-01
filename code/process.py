
import pandas
import utils.geo.info as geo_info
import utils.geo.convert as convert_utils
import os


if __name__ == '__main__':
    root_path = "/home/amiri/Research/geopol-dev/generated_data/OSF_GPS"
    datasets = ["01_182_5yrs", "02_1k_5yrs", "03_5k_5yrs", "04_10k_1yr", "05_50k_1yr", "06_100k_6mo", "07_59k_5yrs" ]


    for dataset in datasets:
        try:
            file_path = f'{root_path}/{dataset}/staypoints.tsv'
            out_path = f'{root_path}/{dataset}/staypoints_gps.tsv'
            if not os.path.exists(out_path):
                print(f"Reading {dataset} ...")
                dataset_df = pandas.read_csv(file_path, sep='\t')
                print(f"Converting {dataset} ...")
                dataset_df = convert_utils.convert_to_gps(dataset_df, lat_col=4, lon_col=5, crs_from=geo_info.get_csr(map_name='bjng'))
                print(f"Saving {dataset} ...")
                dataset_df.to_csv(out_path, index=False)
            print(f"Done with {dataset}")
        except Exception as e:
            print(f"Error with {dataset}: {e}")
            continue
