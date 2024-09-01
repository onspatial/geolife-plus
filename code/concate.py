
import utils.results as results_utils
import utils.dataset as dataset_utils
import utils.file as file_utils
import scorer 
from utils.simulate import run
from utils.params import save_params_to_file
def generate_results():
    print("Generating the results...")
    top_params = results_utils.get_top_params(threshold=0.7) 
    configured_params = results_utils.get_configured_params(top_params,configure_type="calibration")
    simulated_params = run(configured_params, shuffle=False,fork_join=False, check_time=1000, parallel=8)
    save_params_to_file(simulated_params, f"results/params.concatenation.json")
    print("Results Generated successfully!")

def concatenate_results():
    folders = file_utils.get_folders_path("city/calibration")
    folders = get_name_soeted_folders(folders)[:300]
    files = file_utils.get_files_path(folders, "Checkin.tsv")
    result_legacy = dataset_utils.concatenate_files(files, uid="UserId")
    result_standardized = dataset_utils.concatenate_files(files, uid="UserId", standardize=True)
    print(f'The results is at: {result_standardized}')
    print(f"score is {scorer.get_score(result_legacy)}")



def get_name_soeted_folders(folders):
    return sorted(folders, key=lambda x: int(x.split("/")[-1].split("_")[-1]))
        


if __name__ == "__main__":
    # generate_results()
    concatenate_results()
