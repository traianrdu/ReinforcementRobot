class Vector2:

    def __init__(self, x, y):
        """Initializes vector of 2 elements (coordinates)"""
        self.x = x
        self.y = y

    @property
    def get_x(self):
        """Returns the x coordinate"""
        return self.x

    @property
    def get_y(self):
        """Returns the y coordinate"""
        return self.y

    def __add__(self, other):
        """Add function"""
        return Vector2(self.x + other.x, self.y + other.y)
