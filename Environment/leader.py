from Environment.objects import Objects, Vector2, pygame
from Utility.bug_algorithm import RandomWalk2D
import random


class Leader(Objects):
    def __init__(self, width: int, length: int, coordinates: Vector2, color: tuple, screen, directions):
        """Leader initialization"""
        super().__init__(width, length, coordinates, color, screen, directions)
        self.direction = ""     # we set a custom direction for random movement
        self.remaining_steps = 0    # the remaining steps for going in only one direction

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
        """Checks if the leader hits an object"""
        for sprite in objects:  # go through the object list
            if self.rect.colliderect(sprite):  # checks the collision
                print("hit")

    def test_reder(self, x, y):
        """Tests if a collide box of the same coordinates will collide"""
        image = pygame.Surface([self.width, self.length])  # add the image
        image.fill(self.color)  # sets the color
        image.set_alpha(128)
        # creates the rectangular shape of the leader
        rect = image.get_rect(topleft=(x, y))

    def is_collide(self, objects, x, y):
        """Checks if the leader will hit an object and return the result."""
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
        """Moves the leader randomly"""
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
            if self.is_collide(objects, self.coordinates.x, self.coordinates.y - 8):
                self.move_S()
                self.direction = "S"

        elif random_direction == "S":
            self.move_S()
            if self.is_collide(objects, self.coordinates.x, self.coordinates.y + 8):
                self.move_N()
                self.direction = "N"

        elif random_direction == "W":
            self.move_W()
            if self.is_collide(objects, self.coordinates.x - 8, self.coordinates.y):
                self.move_E()
                self.direction = "E"

        elif random_direction == "E":
            self.move_E()
            if self.is_collide(objects, self.coordinates.x + 8, self.coordinates.y):
                self.move_W()
                self.direction = "W"

        elif random_direction == "NW":
            self.move_NW()
            if self.is_collide(objects, self.coordinates.x - 8, self.coordinates.y - 8):
                self.move_SE()
                self.direction = "SE"

        elif random_direction == "NE":
            self.move_NE()
            if self.is_collide(objects, self.coordinates.x + 8, self.coordinates.y - 8):
                self.move_SW()
                self.direction = "SW"

        elif random_direction == "SW":
            self.move_SW()
            if self.is_collide(objects, self.coordinates.x - 8, self.coordinates.y + 8):
                self.move_NE()
                self.direction = "NE"

        elif random_direction == "SE":
            self.move_SE()
            if self.is_collide(objects, self.coordinates.x + 8, self.coordinates.y + 8):
                self.move_NW()
                self.direction = "NW"

        else:
            self.coordinates.y += 0.0
            self.coordinates.x += 0.0

        self.collide_box(objects)
