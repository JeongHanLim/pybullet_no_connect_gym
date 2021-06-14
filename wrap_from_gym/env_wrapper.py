from pybullet_envs.gym_locomotion_envs import WalkerBaseBulletEnv
from wrapper.robot_wrapper import Hopper, Walker2D, HalfCheetah, Ant

class HopperBulletEnv(WalkerBaseBulletEnv):

  def __init__(self, render=False, **kwargs):
    self.robot = Hopper(**kwargs)
    WalkerBaseBulletEnv.__init__(self, self.robot, render)

  def update_power(self, hyperparams):
    self.robot.update_power(hyperparams)

class Walker2DBulletEnv(WalkerBaseBulletEnv):

  def __init__(self, render=False, **kwargs):
    self.robot = Walker2D(**kwargs)
    WalkerBaseBulletEnv.__init__(self, self.robot, render)

  def update_power(self, hyperparams):
    self.robot.update_power(hyperparams)


class HalfCheetahBulletEnv(WalkerBaseBulletEnv):

  def __init__(self, render=False, **kwargs):
    self.robot = HalfCheetah(**kwargs)
    WalkerBaseBulletEnv.__init__(self, self.robot, render)

  def _isDone(self):
    return False

  def update_power(self, hyperparams):
    self.robot.update_power(hyperparams)


class AntBulletEnv(WalkerBaseBulletEnv):

  def __init__(self, render=False, **kwargs):
    self.robot = Ant(**kwargs)
    WalkerBaseBulletEnv.__init__(self, self.robot, render)

  def update_power(self, hyperparams):
    self.robot.update_power(hyperparams)
