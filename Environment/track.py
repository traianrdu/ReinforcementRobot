import pygame


class RacingTrack:

    def __init__(self, width, height, start_point):
        """Initializes the Racing Track environment"""
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.start_point = start_point
        pygame.display.set_caption('Racing Car')
