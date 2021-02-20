import pygame
from Utility.vector2 import Vector2


class Car(pygame.sprite.Sprite):

    def __init__(self, width: int, height: int, coordinates: Vector2, color: tuple, screen):
        """Initializes the Car"""
        pygame.sprite.Sprite.__init__(self)
        self.width = width  # width of the car
        self.height = height    # length of the car
        self.coordinates = coordinates  # coordinates of the car
        self.screen = screen    # sets the screen
        self.color = color  # color of the car
        self.image = pygame.Surface([width, height])    # add the image
        self.image.fill(self.color)     # sets the color
        self.rect = self.image.get_rect()   # creates the rectangular shape of the car

    def render(self):
        """Renders the car"""
        pygame.draw.rect(self.screen, self.color, (self.coordinates.x, self.coordinates.y, self.width, self.height))
        pygame.display.flip()   # updates the screen

    def collide_box(self):
        """Creates a collide box"""
