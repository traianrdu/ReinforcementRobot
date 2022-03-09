import pygame
from Utility.vector2 import Vector2


class Cart(pygame.sprite.Sprite):
    def __init__(self, width: int, length: int, coordinates: Vector2, color: tuple, screen):
        """Cart initialization"""
        pygame.sprite.Sprite.__init__(self)
        self.width = width  # width of the car
        self.length = length  # length of the car
        self.coordinates = coordinates  # coordinates of the car
        self.screen = screen  # sets the screen
        self.color = color  # color of the car
        self.image = pygame.Surface([width, length])  # add the image
        self.image.fill(self.color)  # sets the color
        self.rect = self.image.get_rect()  # creates the rectangular shape of the car

        self.w = False
        self.a = False
        self.s = False
        self.d = False

    def render(self, screen):
        """Renders the car on the first run"""
        screen.blit(self.image, (self.coordinates.x, self.coordinates.y))

    def move(self):
        """Move function"""
        if self.w:
            self.coordinates.y -= 0.1
        elif self.a:
            self.coordinates.x -= 0.1
        elif self.s:
            self.coordinates.y += 0.1
        elif self.d:
            self.coordinates.x += 0.1

    def collide_box(self):
        """Creates a collide box"""

    def reset_movement(self):
        """Reset movement actions"""
        self.w = False
        self.a = False
        self.s = False
        self.d = False
