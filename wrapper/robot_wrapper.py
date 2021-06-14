from pybullet_envs.robot_locomotors import WalkerBase
import numpy as np
import pybullet_data
import os

class Ant(WalkerBase):
    foot_list = ['front_left_foot', 'front_right_foot', 'left_back_foot', 'right_back_foot']
    joint_list = ["hip_1", "ankle_1", "hip_2", "ankle_2", "hip_3", "ankle_3", "hip_4", "ankle_4"]

    def __init__(self,front_left_foot, front_right_foot, left_back_foot, right_back_foot):
        self.front_left_foot = front_left_foot
        self.front_right_foot = front_right_foot
        self.left_back_foot = left_back_foot
        self.right_back_foot = right_back_foot
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

    def _update(self):
        for set in Ant.foot_list:
            self.jdict[foot_right_joint].power_coef = self.right_foot


class HalfCheetah(WalkerBase):
    foot_list = ["ffoot", "fshin", "fthigh", "bfoot", "bshin", "bthigh"]  # track these contacts with ground

    def __init__(self, ffoot, fshin, fthigh, bfoot, bshin, bthigh):
        self.hyperparameter = kwargs['hyper']
        WalkerBase.__init__(self, "half_cheetah.xml", "torso", action_dim=6, obs_dim=26, power=0.90)

    def alive_bonus(self, z, pitch):  # Working as step code.
        self.print_power()
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

    def update_power(self, params_to_update):
        self.hyperparameter.update(params_to_update)
        for i, data in enumerate(self.hyperparameter):
            self.jdict[data].power_coef = self.hyperparameter[data]


class Hopper(WalkerBase):
    foot_list = ["foot"]
    joint_list = ["thigh_joint", "leg_joint", "foot_joint"]
    def __init__(self, foot):
        self.foot = foot
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
    joint_foot_right = ["thigh_joint","leg_joint", "foot_joint"]
    joint_foot_left = ["thigh_left_joint", "leg_left_joint","foot_left_joint"]
    joint_list = joint_foot_right + joint_foot_left

    def __init__(self, foot_left: float, foot_right: float):
        """
        torque of Joint = clipped action * power_coef * power
        :param foot_left: power_coef of left foot
        :param foot_right: power_coef of right foot
        action is clipped in range [-1, 1]
        power is constant (0.40)
        """
        self.foot_left = foot_left
        self.foot_right = foot_right
        WalkerBase.__init__(self, "walker2d.xml", "torso", action_dim=6, obs_dim=22, power=0.40)


    def alive_bonus(self, z, pitch):
        return +1 if z > 0.8 and abs(pitch) < 1.0 else -1

    def robot_specific_reset(self, bullet_client):
        WalkerBase.robot_specific_reset(self, bullet_client)
        self._update()

    def update_power(self,foot_left, foot_right):
        self.foot_left = foot_left
        self.foot_right = foot_right
        self._update()

    def _update(self):
        for foot_left_joint in Walker2D.joint_foot_left:
            self.jdict[foot_left_joint].power_coef = self.foot_left
        for foot_right_joint in Walker2D.joint_foot_right:
            self.jdict[foot_right_joint].power_coef = self.foot_right

