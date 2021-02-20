import pygame
from Utility.vector2 import Vector2


class Road(pygame.sprite.Sprite):

    p1x_right = 500
    p1y_right = 200
    p1x_left = 200
    p1y_left = 200

    # ----Exemplul 1
    p1x = 340
    p1y = 390
    p2x = 340
    p2y = 430
    p3x = 460
    p3y = 430
    p4x = 460
    p4y = 340
    p5x = 420
    p5y = 340
    p6x = 420
    p6y = 390

    def __init__(self, screen, color):
        """Initializes the Road"""
        pygame.sprite.Sprite.__init__(self)
        self.color = color  # the color of the road
        self.screen = screen    # sets the screen
        self.background = pygame.Surface(self.screen.get_size()).convert()  # creates a surface for the road

    def render(self):
        """Renders the road"""
        # ### asta trebuie sa pun in functia de generare a drumului
        """
        for i in range(self.p1x_left, self.p1x_right):  # creates a straight line
            self.background.set_at((i, 410), self.color)    # sets the color at the coordinates
        """

        self.generate_road()

        """
        self.background.set_at((200, 200), c)
        self.background.set_at((300, 200), c)
        self.background.set_at((400, 400), c)
        """
        self.screen.blit(self.background, (0, 0))   # draw the road in the background

    def generate_road(self):
        """Algorithm that generates the road"""

        """
        # -----Generare exemplul1
        for i in range(self.p1y, self.p2y):
            self.background.set_at((self.p1x, i), self.color)
        for i in range(self.p2x, self.p3x):
            self.background.set_at((i, self.p2y), self.color)
        for i in range(self.p4y, self.p3y):
            self.background.set_at((self.p3x, i), self.color)
        for i in range(self.p5x, self.p4x):
            self.background.set_at((i, self.p5y), self.color)
        for i in range(self.p5y, self.p6y):
            self.background.set_at((self.p5x, i), self.color)
        for i in range(self.p1x, self.p6x):
            self.background.set_at((i, self.p1y), self.color)
        """

        # --- Asta genereaza corect, dar mai trebuie lucrat la algoritm
        # (??? pot sa fac un tool care sa genereze acesti pixeli cu fiecare click)
        for i in range(self.p1x, self.p3x):
            for j in range(self.p4y, self.p2y):
                if i >= self.p1x and j >= self.p1y:
                    self.background.set_at((i, j), self.color)
                if i >= self.p6x and j >= self.p4y:
                    self.background.set_at((i, j), self.color)
