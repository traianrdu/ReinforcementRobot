from Environment.objects import Objects, Vector2, pygame


class DynamicObj(Objects):

    def __init__(self, width: int, length: int, coordinates: Vector2, color: tuple, screen):
        """Dynamic object initialization"""
        super().__init__(width, length, coordinates, color, screen)
