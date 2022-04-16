from Environment.objects import Objects, Vector2, pygame


class Cart(Objects):
    def __init__(self, width: int, length: int, coordinates: Vector2, color: tuple, screen, directions):
        """Cart initialization"""
        super().__init__(width, length, coordinates, color, screen, directions)

        self.late_objects = None
        self.N = False  # North
        self.W = False  # West
        self.S = False  # South
        self.E = False  # East
        self.NE = False  # North East
        self.NW = False  # North West
        self.SE = False  # South East
        self.SW = False  # South West

    def set_late_objects(self, objects):
        self.late_objects = objects

    def render_cart(self):
        """Renders the cart"""
        self.rect.topleft = (self.coordinates.x, self.coordinates.y)
        self.reset_movement()   # reset actions

    def keyboard_move(self, keys, objects):
        """Movement from keyboard, parameter is the key read from the keyboard & objects list"""
        if keys[pygame.K_w] and keys[pygame.K_a]:  # check 'w' and 'a' key
            self.NW = True     # NW movement enabled
            self.move()  # movement call
        elif keys[pygame.K_w] and keys[pygame.K_d]:  # check 'w' and 'd' key
            self.NE = True     # NE movement enabled
            self.move()  # movement call
        elif keys[pygame.K_s] and keys[pygame.K_a]:  # check 's' and 'a' key
            self.SW = True     # SW movement enabled
            self.move()  # movement call
        elif keys[pygame.K_s] and keys[pygame.K_d]:  # check 's' and 'd' key
            self.SE = True     # SE movement enabled
            self.move()  # movement call
        elif keys[pygame.K_w]:     # check 'w' key
            self.N = True  # N movement enabled
            self.move()    # movement call
        elif keys[pygame.K_a]:   # check 'a' key
            self.W = True  # W movement enabled
            self.move()  # movement call
        elif keys[pygame.K_s]:   # check 's' key
            self.S = True  # S movement enabled
            self.move()  # movement call
        elif keys[pygame.K_d]:   # check 'd' key
            self.E = True  # E movement enabled
            self.move()  # movement call
        else:
            self.reset_movement()  # reset all movements

        self.collide_box(objects)

    def did_collide(self):
        """Checks if the cart will hit an object and return the result."""
        image = pygame.Surface([self.width, self.length])  # add the image
        image.fill((25, 25, 25))  # sets the color
        rect = image.get_rect(topleft=(self.coordinates.x, self.coordinates.y))
        for sprite in self.late_objects:  # go through the object list
            if rect.colliderect(sprite):  # checks the collision
                return True
        return False

    def did_follow(self):
        """Checks if the cart will follow the leader and return the result."""

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
