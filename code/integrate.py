import sys
import utils.file as file
import time

def snake_case(string): 
    return ''.join(['_' + i.lower() if i.isupper()  
               else i for i in string]).lstrip('_')

if __name__ == "__main__":
    if len(sys.argv) > 3:
        log_dir = sys.argv[1]
        file_prefix = sys.argv[2]
        appended_file = sys.argv[3]
    else:
        log_dir = '/home/hosseinamiri/Research/geopol-dev/city/results/id_results_1/logs/logs'
        file_prefix = 'AgentStateTable'
        appended_file = f'{log_dir}/trajectories.tsv'
    print(f"Integrating log files from {log_dir} with prefix {file_prefix} into {appended_file}")
    if file_prefix=='Checkin':
        file.integrate_log_files(log_dir, file_prefix, appended_file,remove_original=True)
    elif file_prefix=='AgentStateTable':
        file.integrate_log_files(log_dir, file_prefix, appended_file, command='cut -f 1-4')
    # time.sleep(5)
    # print(f"Zipping the file {appended_file}...")
    # file.zip("/home/hosseinamiri/Research/geopol-dev/city/results/id_results_1/trajectories.tsv")

