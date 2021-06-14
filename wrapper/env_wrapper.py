from pybullet_envs.gym_locomotion_envs import WalkerBaseBulletEnv
from wrapper.robot_wrapper import Hopper, Walker2D, HalfCheetah, Ant
from load_parameters import load_hyperparameters
import numpy as np


class HopperBulletEnv(WalkerBaseBulletEnv):

    def __init__(self, foot=100, render=False):
        initial_hyper = load_hyperparameters('HopperBulletEnv')
        foot = initial_hyper["foot"]
        self.robot = Hopper(foot)
        WalkerBaseBulletEnv.__init__(self, self.robot, render)

    def update_power(self, hyperparams):
        self.robot.update_power(hyperparams)


class Walker2DBulletEnv(WalkerBaseBulletEnv):
    foot_list = ["foot_left", "foot_right"]
    joint_list = ["thigh_left_joint", "leg_left_joint", "foot_left_joint","thigh_joint", "leg_joint", "foot_joint"]

    def __init__(self, foot_left=100, foot_right=100, render=False):
        initial_hyper = load_hyperparameters('Walker2DBulletEnv')
        foot_left, foot_right = [initial_hyper[i] for i in Walker2DBulletEnv.foot_list]
        self.robot = Walker2D(foot_left, foot_right)
        WalkerBaseBulletEnv.__init__(self, self.robot, render)

    def update_power(self, foot_left, foot_right):
        self.robot.update_power(foot_left, foot_right)

    @property
    def power(self):
        return np.asarray([self.jdict[k].power_coef for k in Walker2DBulletEnv.joint_list], dtype=np.float32)


class HalfCheetahBulletEnv(WalkerBaseBulletEnv):
    foot_list = ["ffoot", "fshin", "fthigh", "bfoot", "bshin", "bthigh"]

    def __init__(self, ffoot=100, fshin=100, fthigh=100, bfoot=100, bshin=100, bthigh=100, render=False):
        initial_hyper = load_hyperparameters('HalfCheetahBulletEnv')
        ffoot, fshin, fthigh, bfoot, bshin, bthigh = [initial_hyper[i] for i in HalfCheetahBulletEnv.foot_list]
        self.robot = HalfCheetah(ffoot, fshin, fthigh, bfoot, bshin, bthigh)
        WalkerBaseBulletEnv.__init__(self, self.robot, render)

    # TODO : NEED TO LOOK.
    def _isDone(self):
        return False

    def update_power(self, params_to_update):
        self.robot.update_power(params_to_update)


class AntBulletEnv(WalkerBaseBulletEnv):
    foot_list = ['front_left_foot', 'front_right_foot', 'left_back_foot', 'right_back_foot']

    def __init__(self, front_left_foot=100, front_right_foot=100, left_back_foot=100, right_back_foot=100,
                 render=False):
        initial_hyper = load_hyperparameters('AntBulletEnv')
        front_left_foot, front_right_foot, left_back_foot, right_back_foot \
            = [initial_hyper[i] for i in AntBulletEnv.foot_list]
        self.robot = Ant(front_left_foot, front_right_foot, left_back_foot, right_back_foot)
        WalkerBaseBulletEnv.__init__(self, self.robot, render)

    def update_power(self, hyperparams):
        self.robot.update_power(hyperparams)


6
