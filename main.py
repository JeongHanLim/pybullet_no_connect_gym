from pybullet_wrapper.env_wrapper import HalfCheetahBulletEnv, Walker2DBulletEnv, HopperBulletEnv, AntBulletEnv
import numpy as np
import time
import random
#env_list = [AntBulletEnv,HalfCheetahBulletEnv, Walker2DBulletEnv, HopperBulletEnv]
env = Walker2DBulletEnv()
env.update_power(foot_left=130.0, foot_right=1.0)
env = HalfCheetahBulletEnv()
env.update_power(ffoot=100, fshin=100, fthigh=100, bfoot=100, bshin=100, bthigh=100)
env = AntBulletEnv()
env.update_power(flfoot=100, frfoot=100, lbfoot=100, rbfoot=100)
env = HopperBulletEnv()
env.update_power(foot=100)


state = env.reset()
# TODO: Before reset, update_power does not work.
env.update_power(foot_left=130.0, foot_right=1.0)
joint_power = env.power
print(joint_power)

episode = 0
rewards = []
for i in range(1000):
    state = env.reset()
    episode_reward = 0
    episode += 1
    while True:
        #action, _ = model.predict(state)
        action = env.action_space.sample()
        ns, rw, done, info = env.step(action)
        episode_reward+=rw
        if done == True:
            rewards.append(episode_reward)
            print(episode_reward)
            break
        time.sleep(0.02)

print(np.mean(rewards))
print(np.std(rewards))

