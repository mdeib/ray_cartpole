# Ray RLlib Cartpole

python dependencies are in requirements.txt

```
pip install -r requirements.txt
```

before the script is run an instance of ray must be started

```
ray start --head
```

finally the script can be run

```
python train.py
```

and the results can be seen in tensorboard 

```
tensorboard --logdir <checkpoints_directory_path>
```
