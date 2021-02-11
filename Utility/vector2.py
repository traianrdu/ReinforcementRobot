class Vector2:

    def __init__(self, x, y):
        """Initializes vector 2"""
        self.x = x
        self.y = y

    def getX(self):
        """Returns the x coordinate"""
        return self.x

    def getY(self):
        """Returns the y coordinate"""
        return self.y

    def __add__(self, other):
        """Add function"""
        return Vector2(self.x + other.x, self.y + other.y)
