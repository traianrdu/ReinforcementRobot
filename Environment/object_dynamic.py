import pygame
from Utility.vector2 import Vector2


class DynamicObj(pygame.sprite.Sprite):

    def __init__(self, width: int, length: int, coordinates: Vector2, color: tuple, screen):
        """Dynamic object initialization"""
        pygame.sprite.Sprite.__init__(self)
        self.width = width  # width of the object
        self.length = length  # length of the object
        self.coordinates = coordinates  # coordinates of the object
        self.screen = screen  # sets the screen
        self.color = color  # color of the object
        self.image = pygame.Surface([width, length])  # add the image
        self.image.fill(self.color)  # sets the color
        self.rect = self.image.get_rect()  # creates the rectangular shape of the object

    def render(self, screen):
        """Renders the car"""
        screen.blit(self.image, (self.coordinates.x, self.coordinates.y))

    def collide_box(self):
        """Creates a collide box"""
