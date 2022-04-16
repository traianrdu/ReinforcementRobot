import pygame
from Utility.vector2 import Vector2
import random


class Objects(pygame.sprite.Sprite):
    def __init__(self, width: int, length: int, coordinates: Vector2, color: tuple, screen, directions):
        """Main objects class initialization"""
        pygame.sprite.Sprite.__init__(self)
        self.width = width  # width of the car
        self.length = length  # length of the car
        self.initial_coordinates = coordinates  # reset to initial coord
        self.coordinates = coordinates  # coordinates of the car
        self.screen = screen  # sets the screen
        self.color = color  # color of the car
        self.directions = directions
        self.image = pygame.Surface([width, length])  # add the image
        self.image.fill(self.color)  # sets the color
        # creates the rectangular shape of the leader
        self.rect = self.image.get_rect(topleft=(coordinates.x, coordinates.y))
        self.direction = ""  # we set a custom direction for random movement
        self.remaining_steps = 0  # the remaining steps for going in only one direction

    def reset(self):
        """Reset to initial coordinates"""
        self.coordinates = self.initial_coordinates

    def move_N(self):
        """North movement"""
        self.coordinates.y -= 0.1

    def move_S(self):
        """South movement"""
        self.coordinates.y += 0.1

    def move_W(self):
        """West movement"""
        self.coordinates.x -= 0.1

    def move_E(self):
        """East movement"""
        self.coordinates.x += 0.1

    def move_NW(self):
        """North west movement"""
        self.coordinates.y -= 0.1
        self.coordinates.x -= 0.1

    def move_NE(self):
        """North east movement"""
        self.coordinates.y -= 0.1
        self.coordinates.x += 0.1

    def move_SW(self):
        """South west movement"""
        self.coordinates.y += 0.1
        self.coordinates.x -= 0.1

    def move_SE(self):
        """South east movement"""
        self.coordinates.y += 0.1
        self.coordinates.x += 0.1

    def render(self):
        """Renders the object"""
        self.rect.topleft = (self.coordinates.x, self.coordinates.y)

    def is_not_in_screen(self, x, y):
        """Checks if the object is still on the screen"""
        s_width, s_length = self.screen.get_size()   # get screen size
        if y <= 0:
            return True
        elif x <= 0:
            return True
        elif y >= s_length:
            return True
        elif x >= s_width:
            return True
        return False

    def is_collide(self, objects, x, y):
        """Checks if the current object will hit an object and return the result."""
        image = pygame.Surface([self.width, self.length])  # add the image
        image.fill((25, 25, 25))  # sets the color
        #image.set_alpha(128)    # make it transparent
        # creates the rectangular shape of the leader
        rect = image.get_rect(topleft=(x, y))
        for sprite in objects:  # go through the object list
            if rect.colliderect(sprite):  # checks the collision
                return True
        return False

    def random_move(self, objects):
        """Moves the object randomly"""
        if self.remaining_steps > 0:
            random_direction = self.direction
            self.remaining_steps -= 1
        else:
            random_direction = random.choice(self.directions)  # get a random direction
            self.remaining_steps = random.randrange(100, 500)
            self.direction = random_direction

        if random_direction == "N":
            self.move_N()
            # change movement if it will collide
            if self.is_collide(objects, self.coordinates.x, self.coordinates.y - 5) or \
                    self.is_not_in_screen(self.coordinates.x, self.coordinates.y - 10):
                self.move_S()
                self.direction = "S"

        elif random_direction == "S":
            self.move_S()
            if self.is_collide(objects, self.coordinates.x, self.coordinates.y + 5) or \
                    self.is_not_in_screen(self.coordinates.x, self.coordinates.y + 10):
                self.move_N()
                self.direction = "N"

        elif random_direction == "W":
            self.move_W()
            if self.is_collide(objects, self.coordinates.x - 5, self.coordinates.y) or \
                    self.is_not_in_screen(self.coordinates.x - 10, self.coordinates.y):
                self.move_E()
                self.direction = "E"

        elif random_direction == "E":
            self.move_E()
            if self.is_collide(objects, self.coordinates.x + 5, self.coordinates.y) or \
                    self.is_not_in_screen(self.coordinates.x + 10, self.coordinates.y):
                self.move_W()
                self.direction = "W"

        elif random_direction == "NW":
            self.move_NW()
            if self.is_collide(objects, self.coordinates.x - 5, self.coordinates.y - 5) or \
                    self.is_not_in_screen(self.coordinates.x - 10, self.coordinates.y - 10):
                self.move_SE()
                self.direction = "SE"

        elif random_direction == "NE":
            self.move_NE()
            if self.is_collide(objects, self.coordinates.x + 5, self.coordinates.y - 5) or \
                    self.is_not_in_screen(self.coordinates.x + 10, self.coordinates.y - 10):
                self.move_SW()
                self.direction = "SW"

        elif random_direction == "SW":
            self.move_SW()
            if self.is_collide(objects, self.coordinates.x - 5, self.coordinates.y + 5) or \
                    self.is_not_in_screen(self.coordinates.x - 10, self.coordinates.y + 10):
                self.move_NE()
                self.direction = "NE"

        elif random_direction == "SE":
            self.move_SE()
            if self.is_collide(objects, self.coordinates.x + 5, self.coordinates.y + 5) or \
                    self.is_not_in_screen(self.coordinates.x + 10, self.coordinates.y + 10):
                self.move_NW()
                self.direction = "NW"

        else:
            self.coordinates.y += 0.0
            self.coordinates.x += 0.0

        #self.collide_box(objects)

