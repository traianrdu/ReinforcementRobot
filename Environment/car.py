import pygame


class Car:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def collide_box(self):
        """Creates a collide box"""
