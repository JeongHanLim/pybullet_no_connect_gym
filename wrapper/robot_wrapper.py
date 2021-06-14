from pybullet_envs.robot_locomotors import WalkerBase
import numpy as np
import pybullet_data
import os

class Ant(WalkerBase):
    foot_list = ['front_left_foot', 'front_right_foot', 'left_back_foot', 'right_back_foot']
    # joint_list = ["hip_1"  "ankle_1" "hip_2" "ankle_2": "hip_3" "ankle_3"  "hip_4"  "ankle_4"]

    def __init__(self, **kwargs):
        self.hyperparameter = kwargs['hyper']
        WalkerBase.__init__(self, "ant.xml", "torso", action_dim=8, obs_dim=28, power=2.5)

    def alive_bonus(self, z, pitch):
        return +1 if z > 0.26 else -1  # 0.25 is central sphere rad, die if it scrapes the ground

    def robot_specific_reset(self, bullet_client):
        WalkerBase.robot_specific_reset(self, bullet_client)
        for i, data in enumerate(self.hyperparameter):
            self.jdict[data].power_coef = self.hyperparameter[data]

    def print_power(self):
        for i, data in enumerate(self.hyperparameter):
            print(self.jdict[data].power_coef, end='\t')
        print()  # newline

    def update_power(self, power):
        self.hyperparameter.update(power)
        for i, data in enumerate(self.hyperparameter):
            self.jdict[data].power_coef = self.hyperparameter[data]


class HalfCheetah(WalkerBase):
    foot_list = ["ffoot", "fshin", "fthigh", "bfoot", "bshin", "bthigh"]  # track these contacts with ground

    def __init__(self, **kwargs):
        self.hyperparameter = kwargs['hyper']
        WalkerBase.__init__(self, "half_cheetah.xml", "torso", action_dim=6, obs_dim=26, power=0.90)

    def alive_bonus(self, z, pitch):  # Working as step code.
        # Use contact other than feet to terminate episode: due to a lot of strange walks using knees
        return +1 if np.abs(pitch) < 1.0 and not self.feet_contact[1] and not self.feet_contact[
            2] and not self.feet_contact[4] and not self.feet_contact[5] else -1

    def robot_specific_reset(self, bullet_client):
        WalkerBase.robot_specific_reset(self, bullet_client)
        for i, data in enumerate(self.hyperparameter):
            self.jdict[data].power_coef = self.hyperparameter[data]

        #torque = a * power_coef * power(constant)
    def print_power(self):
        for i, data in enumerate(self.hyperparameter):
            print(self.jdict[data].power_coef, end='\t')
        print()

    def update_power(self, power):
        self.hyperparameter.update(power)
        for i, data in enumerate(self.hyperparameter):
            self.jdict[data].power_coef = self.hyperparameter[data]


class Hopper(WalkerBase):
    foot_list = ["foot"]
    # joint_list = ["thigh_joint", "leg_joint", "foot_joint"]
    def __init__(self, **kwargs):
        self.hyperparameter = kwargs['hyper']
        WalkerBase.__init__(self, "hopper.xml", "torso", action_dim=3, obs_dim=15, power=0.75)

    def alive_bonus(self, z, pitch):
        return +1 if z > 0.8 and abs(pitch) < 1.0 else -1

    def robot_specific_reset(self, bullet_client):
        WalkerBase.robot_specific_reset(self, bullet_client)
        for i, data in enumerate(self.hyperparameter):
            self.jdict[data].power_coef = self.hyperparameter[data]

    def print_power(self):
        for i, data in enumerate(self.hyperparameter):
            print(self.jdict[data].power_coef, end='\t')
        print()  # newline

    def update_power(self, power):
        self.hyperparameter.update(power)
        for i, data in enumerate(self.hyperparameter):
            self.jdict[data].power_coef = self.hyperparameter[data]


class Walker2D(WalkerBase):
    foot_list = ["foot", "foot_left"]
    # joint_list = ["thigh_joint","leg_joint", "foot_joint", "thigh_left_joint", "leg_left_joint","foot_left_joint"]

    def __init__(self, **kwargs):
        self.hyperparameter = kwargs['hyper']
        print(self.hyperparameter)
        WalkerBase.__init__(self, "walker2d.xml", "torso", action_dim=6, obs_dim=22, power=0.40)

    def alive_bonus(self, z, pitch):
        return +1 if z > 0.8 and abs(pitch) < 1.0 else -1

    def robot_specific_reset(self, bullet_client):
        WalkerBase.robot_specific_reset(self, bullet_client)
        for i, data in enumerate(self.hyperparameter):
            self.jdict[data].power_coef = self.hyperparameter[data]

    def print_power(self):
        for i, data in enumerate(self.hyperparameter):
            print(self.jdict[data].power_coef, end='\t')
        print()  # newline

    def update_power(self, power):
        self.hyperparameter.update(power)
        for i, data in enumerate(self.hyperparameter):
            self.jdict[data].power_coef = self.hyperparameter[data]



