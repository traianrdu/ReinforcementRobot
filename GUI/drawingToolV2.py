from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color, Line, Ellipse
from Utility import algebra
from Utility.vector2 import Vector2


class DrawingToolV2(Screen, Widget):
    def __init__(self, **kwargs):
        super(DrawingToolV2, self).__init__(**kwargs)
        self.last_point_x = None
        self.last_point_y = None
        self.first_point_x = None
        self.first_point_y = None
        self.d = []
        self.check = None  # check if touch down was on the screen

    def on_touch_down(self, touch):
        if Widget.on_touch_down(self, touch):  # used to press buttons on screen
            return True

        with self.canvas.before:  # the canvas drawing part
            Color(1, 1, 0)
            self.last_point_x = touch.x  # initialize with the starting points
            self.last_point_y = touch.y
            self.first_point_x = touch.x
            self.first_point_y = touch.y
            touch.ud['line'] = Line(points=(touch.x, touch.y))  # shows line
            print("mouse down:", touch.pos)
            self.d.append(Vector2(self.first_point_x, self.first_point_y))  # append to list
            self.check = 1  # check completed

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]   # shows line
        self.last_point_x = touch.x     # saves last points
        self.last_point_y = touch.y
        self.d.append(Vector2(self.last_point_x, self.last_point_y))    # append to list

    def on_touch_up(self, touch):
        if self.check == 1:  # only if drawing mode
            self.check = None   # reset the check
            if self.last_point_x < self.first_point_x:
                # Left
                if self.last_point_y < self.first_point_y:
                    # Down
                    print("Left Down")
                    touch.ud['line'].points += [self.first_point_x, self.first_point_y]
                    #dist = algebra.findD(self.last_point_x, self.first_point_x, self.last_point_y, self.first_point_y)
                    #while self.last_point_x != self.first_point_x and self.last_point_y != self.first_point_y:
                else:
                    # Up
                    print("Left Up")
                    touch.ud['line'].points += [self.first_point_x, self.first_point_y]
            else:
                # Right
                if self.last_point_y < self.first_point_y:
                    # Down
                    print("Right Down")
                    touch.ud['line'].points += [self.first_point_x, self.first_point_y]
                else:
                    # Up
                    print("Right Up")
                    touch.ud['line'].points += [self.first_point_x, self.first_point_y]
            file = open("GUI/SaveFile/file.txt", "w+")
            for i in self.d:
                print(i.x, i.y)
                file.write(str(i.x)+" ")
                file.write(str(i.y)+'\n')
            file.close()

    def save(self):
        """Saves the data in the json"""
        print(self.d)
