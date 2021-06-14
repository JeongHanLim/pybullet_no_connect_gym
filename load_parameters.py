import json


def load_hyperparameters(env):
    path = "hyperparameter/"+str(env)+"-v0.json"
    with open(path, "r") as f:
        hyperparmas = json.load(f)
    return hyperparmas


# Test Code
if __name__ == "__main__":
    env = "HalfCheetahPyBulletEnv"
    hyper = load_hyperparameters(env)
    print(hyper)