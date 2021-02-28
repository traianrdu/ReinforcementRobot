from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color, Line, Ellipse


class DrawingToolV2(Screen, Widget):
    def __init__(self, **kwargs):
        super(DrawingToolV2, self).__init__(**kwargs)
        self.last_point_x = None
        self.last_point_y = None
        self.first_point_x = None
        self.first_point_y = None

    def on_touch_down(self, touch):
        if Widget.on_touch_down(self, touch):  # used to press buttons on screen
            return True

        with self.canvas.before:  # the canvas drawing part
            Color(1, 1, 0)
            self.last_point_x = touch.x  # initialize with the starting points
            self.last_point_y = touch.y
            self.first_point_x = touch.x
            self.first_point_y = touch.y
            touch.ud['line'] = Line(points=(touch.x, touch.y))
            print("mouse donw:", touch.pos)
            print(self.last_point_x)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]
        self.last_point_x = touch.x
        self.last_point_y = touch.y

    def on_touch_up(self, touch):
        if self.last_point_x < self.first_point_x:
            # Left
            if self.last_point_y < self.first_point_y:
                # Down
                print("Left Down")
            else:
                # Up
                print("Left Up")
        else:
            # Right
            if self.last_point_y < self.first_point_y:
                # Down
                print("Right Down")
            else:
                # Up
                print("Right Up")

    def save(self):
        print(self.last_point_x)
