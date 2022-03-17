from Environment.objects import Objects, Vector2, pygame


class StaticObj(Objects):

    def __init__(self, width: int, length: int, coordinates: Vector2, color: tuple, screen):
        """Static object initialization"""
        super().__init__(width, length, coordinates, color, screen)

