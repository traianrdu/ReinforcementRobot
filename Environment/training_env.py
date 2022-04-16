from Environment.map import Map, Vector2
import pygame


class RiCart:

    def __init__(self):
        self.map = Map(900, 900, Vector2(20, 20))
        self.cart = self.map.cart
        self.score = 0
        self.running = True  # is the game running or not
        #self.action_space = gym.spaces.Box()

    def reset(self):
        """Reset environment"""
        self.score = 0
        self.map.reset()

    def step(self):
        """New step"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # check if the event is the close (X) button
                self.running = False  # quit the game

        reward = 0  # reward
        game_over = False   # game over
        return reward, game_over, self.score

    def move(self):
        """Movement action"""

