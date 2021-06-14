from pybullet_envs.robot_locomotors import WalkerBase
import numpy as np

import os

class Ant(WalkerBase):
    foot_list = ['front_left_foot', 'front_right_foot', 'left_back_foot', 'right_back_foot']
    fljoint, frjoint, lbjoint, rbjoint = \
        ["hip_1", "ankle_1"], ["hip_2", "ankle_2"], ["hip_3", "ankle_3"], ["hip_4", "ankle_4"]
    joint_list = fljoint + frjoint + lbjoint + rbjoint

    def __init__(self, flfoot, frfoot, lbfoot, rbfoot):
        self.flfoot = flfoot
        self.frfoot = frfoot
        self.lbfoot = lbfoot
        self.rbfoot = rbfoot
        WalkerBase.__init__(self, "ant.xml", "torso", action_dim=8, obs_dim=28, power=2.5)

    def alive_bonus(self, z, pitch):
        return +1 if z > 0.26 else -1  # 0.25 is central sphere rad, die if it scrapes the ground

    def robot_specific_reset(self, bullet_client):
        WalkerBase.robot_specific_reset(self, bullet_client)
        self._update()

    def update_power(self, flfoot=100, frfoot=100, lbfoot=100, rbfoot=100):
        self.front_left_foot = flfoot
        self.front_right_foot = frfoot
        self.left_back_foot = lbfoot
        self.right_back_foot = rbfoot
        self._update()

    def _update(self):
        for hip_ankle in Ant.fljoint:
            self.jdict[hip_ankle].power_coef = self.front_left_foot
        for hip_ankle in Ant.frjoint:
            self.jdict[hip_ankle].power_coef = self.front_right_foot
        for hip_ankle in Ant.bljoint:
            self.jdict[hip_ankle].power_coef = self.left_back_foot
        for hip_ankle in Ant.brjoint:
            self.jdict[hip_ankle].power_coef = self.right_back_foot


class HalfCheetah(WalkerBase):
    foot_list = ["ffoot", "fshin", "fthigh", "bfoot", "bshin", "bthigh"]  # track these contacts with ground

    def __init__(self, ffoot, fshin, fthigh, bfoot, bshin, bthigh):
        self.ffoot, self.fshin, self.fthigh, self.bfoot, self.bshin, self.bthigh = \
            ffoot, fshin, fthigh, bfoot, bshin, bthigh
        WalkerBase.__init__(self, "half_cheetah.xml", "torso", action_dim=6, obs_dim=26, power=0.90)

    def alive_bonus(self, z, pitch):  # Working as step code.
        # Use contact other than feet to terminate episode: due to a lot of strange walks using knees
        return +1 if np.abs(pitch) < 1.0 and not self.feet_contact[1] and not self.feet_contact[
            2] and not self.feet_contact[4] and not self.feet_contact[5] else -1

    def robot_specific_reset(self, bullet_client):
        WalkerBase.robot_specific_reset(self, bullet_client)
        self._update()

    def update_power(self, ffoot=120, fshin=90, fthigh=60, bfoot=140, bshin=60, bthigh=30):
        self.ffoot, self.fshin, self.fthigh, self.bfoot, self.bshin, self.bthigh = \
            ffoot, fshin, fthigh, bfoot, bshin, bthigh
        self._update()

    def _update(self):
        self.jdict["bthigh"].power_coef = self.bthigh
        self.jdict["bshin"].power_coef  = self.bshin
        self.jdict["bfoot"].power_coef  = self.bfoot
        self.jdict["fthigh"].power_coef = self.fthigh
        self.jdict["fshin"].power_coef  = self.fshin
        self.jdict["ffoot"].power_coef  = self.ffoot


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
        self._update()

    def update_power(self, power):
        self.power = power
        self._update()

    def _update(self):
        for foot_joint in Hopper.joint_list:
            self.jdict[foot_joint].power_coef = self.foot


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

