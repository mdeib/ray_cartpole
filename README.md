# Ray RLlib Cartpole

Simple script to test out basic RL algorithms on Cartpole

## Usage

Python dependencies are in requirements.txt

```
pip install -r requirements.txt
```

Before the script is run an instance of ray must be started

```
ray start --head
```

Finally the script can be run

```
python train.py
```

And the results can be seen in tensorboard 

```
tensorboard --logdir <checkpoints_directory_path>
```

## Experiments

Below is an exploration of the impact a network's size has on learning (across different algorithms

![PG](Plots/PG_mean_reward.PNG)

**Orange - Two hidden Layers 32 neurons each **<br />
**Pink - One hidden Layer of 32 neurons **<br />
**Light Blue - Two hidden Layers 4 neurons each **<br />
**Red - One hidden Layer of 4 neurons **<br />
**Blue - Linear **<br />

![PPO](Plots/PPO_mean_reward.PNG)

Light Blue - Two hidden Layers 32 neurons each
Red - One hidden Layer of 32 neurons
Blue - Two hidden Layers 4 neurons each
Orange - One hidden Layer of 4 neurons
Pink - Linear

![PPO Entropy](Plots/PPO_entropy.PNG)

Light Blue - Two hidden Layers 32 neurons each
Red - One hidden Layer of 32 neurons
Blue - Two hidden Layers 4 neurons each
Orange - One hidden Layer of 4 neurons
Pink - Linear

![DQN](Plots/DQN_mean_reward.PNG)

Red - Two hidden Layers 32 neurons each
Orange - One hidden Layer of 32 neurons
Green - Two hidden Layers 4 neurons each
Pink - One hidden Layer of 4 neurons
Light Blue - Linear
Blue - Linear (try #2)

![DQN Sizes](Plots/DQN_mean_reward_sizes.PNG)

Light Blue - Four hidden Layers 32 neurons each
Red - Three hidden Layers 32 neurons each
Blue - Two hidden Layers 32 neurons each
Orange - One hidden Layer of 32 neurons
