import pygame
from Utility.vector2 import Vector2


class Car(pygame.sprite.Sprite):

    def __init__(self, width: int, height: int, coordinates: Vector2, color: tuple, screen):
        """Initializes the Car"""
        pygame.sprite.Sprite.__init__(self)
        self.width = width  # width of the car
        self.height = height    # length of the car
        self.coordinates = coordinates  # coordinates of the car
        self.screen = screen
        self.color = color

        self.image = pygame.Surface([width, height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

    def render(self):
        """Renders the car"""
        pygame.draw.rect(self.screen, self.color, (self.coordinates.x, self.coordinates.y, self.width, self.height))
        #pygame.display.flip()

    def collide_box(self):
        """Creates a collide box"""
