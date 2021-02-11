import pygame
from Utility.vector2 import Vector2


class RacingTrack:

    def __init__(self, width: int, height: int, start_point: Vector2):
        """Initializes the Racing Track environment"""
        self.width = width  # width of the screen
        self.height = height    # height of the screen
        self.start_point = start_point  # starting point
        self.screen = pygame.display.set_mode((self.width, self.height))  # set the screen dimensions
        self.render()   # render the environment

    def render(self):
        pygame.display.set_caption('Racing Car')    # title of the simulator
        pygame.draw.rect(self.screen, (255, 255, 255), (400, 400, 20, 20))  # the car
        pygame.display.flip()   # shows on screen
