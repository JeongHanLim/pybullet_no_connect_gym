from wrapper.env_wrapper import HalfCheetahBulletEnv, Walker2DBulletEnv, HopperBulletEnv, AntBulletEnv
import numpy as np
import time
import random
#env_list = [AntBulletEnv,HalfCheetahBulletEnv, Walker2DBulletEnv, HopperBulletEnv]
env = Walker2DBulletEnv()
env.render()

episode = 0
rewards = []
for i in range(1000):
    state = env.reset()
    env.update_power(foot_left=130.0, foot_right=1.0)
    sth = env.power
    print(sth)
    reward_episode = 0
    episode += 1
    while True:
        #action, _ = model.predict(state)
        action = env.action_space.sample()
        ns, rw, done, info = env.step(action)
        reward_episode+=rw
        if done == True:
            rewards.append(reward_episode)
            break
        time.sleep(0.02)

print(np.mean(rewards))
print(np.std(rewards))

