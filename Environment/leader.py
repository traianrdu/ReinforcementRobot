import pygame
from Utility.vector2 import Vector2


class Leader(pygame.sprite.Sprite):
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
        self.rect = self.image.get_rect(topleft=(coordinates.x, coordinates.y))  # creates the rectangular shape of the cart

        self.N = False  # North
        self.W = False  # West
        self.S = False  # South
        self.E = False  # East
        self.NE = False  # North East
        self.NW = False  # North West
        self.SE = False  # South East
        self.SW = False  # South West

    def render(self):
        """Renders the car on the first run"""
        self.rect.topleft = (self.coordinates.x, self.coordinates.y)
        self.reset_movement()   # reset actions

    def move(self):
        """Move function"""
        if self.N:
            self.coordinates.y -= 0.1
        elif self.W:
            self.coordinates.x -= 0.1
        elif self.S:
            self.coordinates.y += 0.1
        elif self.E:
            self.coordinates.x += 0.1
        elif self.NW:
            self.coordinates.y -= 0.1
            self.coordinates.x -= 0.1
        elif self.NE:
            self.coordinates.y -= 0.1
            self.coordinates.x += 0.1
        elif self.SW:
            self.coordinates.y += 0.1
            self.coordinates.x -= 0.1
        elif self.SE:
            self.coordinates.y += 0.1
            self.coordinates.x += 0.1

    def collide_box(self, objects):
        """Checks if the cart hits an object"""
        for sprite in objects:  # go through the object list
            if self.rect.colliderect(sprite):   # checks the collision
                print("hit")

    def reset_movement(self):
        """Reset movement actions"""
        self.N = False
        self.W = False
        self.S = False
        self.E = False
        self.NE = False
        self.NW = False
        self.SE = False
        self.SW = False
