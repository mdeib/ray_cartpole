# Ray RLlib Cartpole

Simple script to test out basic RL algorithms on Cartpole

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
