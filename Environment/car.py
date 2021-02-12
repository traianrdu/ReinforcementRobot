import pygame
from Utility.vector2 import Vector2


class Car:

    def __init__(self, width: int, length: int, coordinates: Vector2):
        """Initializes the Car"""
        self.width = width  # width of the car
        self.height = length    # length of the car
        self.coordinates = coordinates  # coordinates of the car

    def collide_box(self):
        """Creates a collide box"""
