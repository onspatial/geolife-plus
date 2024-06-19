from utils.config import get_layer_params
import utils.params as params
from utils.params import initialization, save_params_to_file, get_pool_params, update_pool
from utils.simulate import run
import utils.file as file
from utils.constants.config import get_layer_width
from test.basics import test as test
import test.middle as test_middle

def clean_up():
    file.delete_folder("pole")
    file.delete_folder("city")
    file.delete_folder("tmp")
    return

if __name__ == "__main__":
    print("Calibration is running...")
    try:
        clean_up()
    except Exception as e:
        print(f"Error in clean_up: {e}")
        pass
    timestamp = 618000 + get_layer_width()
    print(f"Calibration started at {timestamp}...")
    print("Initialization completed...")
    layer_level = 0
    if layer_level == 0:
        run_id=f't{timestamp}_l{str(layer_level).zfill(3)}'
        initialization(run_id)
        print(f"Initialization completed with run_id: {run_id}...")
    test()
    layer_params = []
    while layer_level < 100:
        layer_level += 1
        run_id=f't{timestamp}_l{str(layer_level).zfill(3)}'
        print(f"Running calibration with run_id: {run_id}...")
        pool_params = get_pool_params()     
        layer_params = get_layer_params(pool_params, run_id)
        layer_params = run(layer_params, fork_join=False, check_time=5, parallel=90)
        update_pool(pool_params, layer_params, layer_level)
        test_middle.test()
      
    print(f"Calibration completed successfully with {layer_level} iterations...")