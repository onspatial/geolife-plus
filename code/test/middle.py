import os
import utils.file as files
import test.check as check
import test.utils as utils
import utils.params as params

def is_compatible_itself(params):
    for param in params:
        assert check.is_compatible_itself(param["properties"]) == True
        
def pool_param_consistency(pool_param_file="params.pool.json",throw_error=True):
    try:
        assert check.pool_param_consistency(pool_param_file) == True
    except:
        if throw_error:
            raise Exception("pool_param_consistency failed")
        print("pool_param_consistency failed")

def test(message="",pool_param_file="params.pool.json",throw_error=True):
    params_dir = "pole"
    project_path = files.get_project_path()
    print(f"Testing {message}...")
    for file in os.listdir(f'{project_path}/{params_dir}'):
        if not file.endswith("l000.json"):
            print(f"Testing {file}...")
            params = files.load_json(f"{project_path}/{params_dir}/{file}")
            is_compatible_itself(params)

    pool_param_consistency(pool_param_file,throw_error)

def test_pool_params_consistency(params_to_be_tested, message="",throw_error=True,count=-2):
    print(f"Testing params consistency for {message} with {len(params_to_be_tested)} params...")
    fake_pool="params.fake_pool.json"
    pool_params = params.get_pool_params()
    params.save_params_to_file(params_to_be_tested,f"pole_test/l{count}/params.tbt.{message}.json")
    params.update_pool(pool_params, params_to_be_tested, count, fake_pool)
    test(f"actual message: {message}", fake_pool, throw_error)