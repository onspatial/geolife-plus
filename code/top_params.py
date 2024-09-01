import utils.params as params
from test.middle import test as test_middle
def pexit(*args):
    for arg in args:
        print(arg)
    

if __name__ == "__main__":
    pole_aws128_params = params.get_params_in_folder("pole_aws128")
    pole_aws64_params = params.get_params_in_folder("pole_aws64")
    pole_hopper_params = params.get_params_in_folder("pole_hopper")
    pole_nuc_params = params.get_params_in_folder("pole_nuc")

    pole_params = pole_aws128_params + pole_aws64_params + pole_hopper_params + pole_nuc_params

    top_params = params.get_top_params(pole_params,700)
    params.save_params_to_file(top_params, "params.700.json")