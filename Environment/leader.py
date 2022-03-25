from Environment.objects import Objects, Vector2, pygame
from Utility.bug_algorithm import RandomWalk2D
import random


class Leader(Objects):
    def __init__(self, width: int, length: int, coordinates: Vector2, color: tuple, screen, directions):
        """Leader initialization"""
        super().__init__(width, length, coordinates, color, screen, directions)

    def render(self):
        """Renders the leader"""
        self.rect.topleft = (self.coordinates.x, self.coordinates.y)

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

    def keyboard_move(self, keys, objects):
        """Movement from keyboard, parameter is the key read from the keyboard & objects list"""
        if keys[pygame.K_w] and keys[pygame.K_a]:  # check 'w' and 'a' key
            self.move_NW()  # NW movement call
        elif keys[pygame.K_w] and keys[pygame.K_d]:  # check 'w' and 'd' key
            self.move_NE()  # NW movement call  # NE movement enabled
        elif keys[pygame.K_s] and keys[pygame.K_a]:  # check 's' and 'a' key
            self.move_SW()  # SW movement enabled
        elif keys[pygame.K_s] and keys[pygame.K_d]:  # check 's' and 'd' key
            self.move_SE()  # SE movement enabled
        elif keys[pygame.K_w]:  # check 'w' key
            self.move_N()  # N movement enabled
        elif keys[pygame.K_a]:  # check 'a' key
            self.move_W()  # W movement enabled
        elif keys[pygame.K_s]:  # check 's' key
            self.move_S()  # S movement enabled
        elif keys[pygame.K_d]:  # check 'd' key
            self.move_E()  # E movement enabled

        self.collide_box(objects)

    def collide_box(self, objects):
        """Checks if the cart hits an object"""
        for sprite in objects:  # go through the object list
            if self.rect.colliderect(sprite):  # checks the collision
                print("hit")

    def random_move(self):
        """Moves the leader randomly"""
        random_direction = random.choice(self.directions)  # get a random direction

        if random_direction == "N":
            self.move_N()
        elif random_direction == "S":
            self.move_S()
        elif random_direction == "W":
            self.move_W()
        elif random_direction == "E":
            self.move_E()
        elif random_direction == "NW":
            self.move_NW()
        elif random_direction == "NE":
            self.move_NE()
        elif random_direction == "SW":
            self.move_SW()
        elif random_direction == "SE":
            self.move_SE()
        else:
            self.coordinates.y += 0.0
            self.coordinates.x += 0.0
