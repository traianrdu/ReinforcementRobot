import gym
from Environment.map import Map, Vector2


class RiCart(gym.Env):

    def __init__(self):
        self.map = Map(900, 900, Vector2(20, 20))
        self.cart = self.map.cart
        #self.action_space = gym.spaces.Box()

    def reset(self):
        return