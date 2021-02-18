import pygame
from Utility.vector2 import Vector2
from Environment.car import Car


class RacingTrack:
    # define the colors
    BLACK = (25, 25, 25)
    WHITE = (255, 255, 255)
    RED = (255, 80, 80)
    BLUE = (80, 80, 255)

    def __init__(self, width: int, height: int, start_point: Vector2):
        """Initializes the Racing Track environment"""
        pygame.init()   # starts the environment

        self.width = width  # width of the screen
        self.height = height    # height of the screen
        self.start_point = start_point  # starting point
        self.screen = pygame.display.set_mode((self.width, self.height))  # set the screen dimensions
        self.car = Car(20, 20, Vector2(400, 400), self.RED, self.screen)
        self.render()   # render the environment

        self.running = False    # is the game running or not

    def render(self):
        """Renders the environment"""
        pygame.display.set_caption('Racing Car')    # title of the simulator
        #pygame.draw.rect(self.screen, self.RED, (400, 400, 20, 20))  # the car
        self.car.render()   # render the car
        pygame.display.flip()   # shows on screen

    def handle_events(self):
        """Handle the press key events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # check if the event is the X button
                self.running = False    # if it is quit the game

    def run(self):
        """Starts the environment loop"""

        self.running = True

        while self.running:
            self.handle_events()  # handles the events of the game

        pygame.quit()
