import pygame
from Utility.vector2 import Vector2


class Objects(pygame.sprite.Sprite):
    def __init__(self, width: int, length: int, coordinates: Vector2, color: tuple, screen):
        """Main objects class initialization"""
        pygame.sprite.Sprite.__init__(self)
        self.width = width  # width of the car
        self.length = length  # length of the car
        self.coordinates = coordinates  # coordinates of the car
        self.screen = screen  # sets the screen
        self.color = color  # color of the car
        self.image = pygame.Surface([width, length])  # add the image
        self.image.fill(self.color)  # sets the color
        # creates the rectangular shape of the leader
        self.rect = self.image.get_rect(topleft=(coordinates.x, coordinates.y))