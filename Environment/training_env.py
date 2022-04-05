import gym
from Environment.map import Map, Vector2


class RiCart(gym.Env):

    def __init__(self):
        self.map = Map(900, 900, Vector2(20, 20)).run()

    def reset(self):
        return