import ray
from ray import tune
import time
import gym

ray.init(address='auto', _redis_password='5241590000000000')

config = {}

# List of available algorithms can be found here: https://docs.ray.io/en/master/rllib-algorithms.html
# algorithm specific parameters can be found by clicking on the corresponding hyperlink
# parameters used for all algorithms are here: https://docs.ray.io/en/master/rllib-training.html#common-parameters
algorithm = "DQN"

# Any gym environment can be plugged in here
env_name = "CartPole-v1"

# architecture defined here, list of neurons in each hidden layer, empty list is linear model
arch = [4, 4]

# These configs define the hyperparameters for the algorithm
# A seperate config dictionary is kept for each algorithm so that seperate
# parameters can be defined for each and seperately switched between
config["PPO"] = {
	"env": env_name,
	"model": {
		"fcnet_hiddens": arch
	},
	"num_workers": 4,
	"num_gpus": 0,
   	"lr": 0.0005,
	"framework": "torch"
}

config["PG"] = {
	"env": env_name,
	"model": {
		"fcnet_hiddens": arch
	},
	"num_workers": 4,
	"num_gpus": 0,
   	"lr": 0.0005,
	"framework": "torch"
}

config["DQN"] = {
	"env": env_name,
	"model": {
		"fcnet_hiddens": arch
	},
	"num_workers": 4,
	"num_gpus": 0,
   	"lr": 0.0005,
	"framework": "torch"
}

# This command runs the actual training using the parameters defined above
results = tune.run(
    algorithm,
    name = algorithm + "_" + str(arch) + "_" + env_name + str(time.time()),
    config = config[algorithm],
    verbose = 3,
    local_dir = "checkpoints")

ray.shutdown()
