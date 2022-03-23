from Environment.objects import Objects, Vector2, pygame


class Leader(Objects):
    def __init__(self, width: int, length: int, coordinates: Vector2, color: tuple, screen):
        """Leader initialization"""
        super().__init__(width, length, coordinates, color, screen)

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
            self.move_N()   # N movement enabled
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
            if self.rect.colliderect(sprite):   # checks the collision
                print("hit")