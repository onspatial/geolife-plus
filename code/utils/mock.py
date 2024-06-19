from time import sleep
from random import random
import utils.log as log
import time
import utils.file as file
def run(params, fork_join=False, check_time=100, parallel=1, shuffle=True, **kwargs):
    print(len(params), "params received...")
    log.note(f"Running {len(params)} params with fork_join={fork_join} and parallel={parallel}..., shuffle={shuffle}",filename="simulate.log.txt")
    for param in params:
        score = random()
        param["score"] = score 
        print(f"running {param['id']} with score: {score}")


    # sleep(5)  
    print("sample run completed...")
    return params   