from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color, Line, Ellipse
from functools import partial
from Utility import algebra


class MainWindow(Screen):
    pass


class DrawingTool(Screen, Widget):
    def __init__(self, **kwargs):
        super(DrawingTool, self).__init__(**kwargs)
        self.old_touch_x = 0
        self.old_touch_y = 0

    def on_touch_down(self, touch):
        if Widget.on_touch_down(self, touch):  # used to press back button
            return True

        with self.canvas.before:  # the canvas drawing part
            Color(1, 1, 0)
            self.old_touch_x = touch.x  # initialize with the starting points
            self.old_touch_y = touch.y
            touch.ud['line'] = Line(points=(touch.x, touch.y))
            touch.ud['line2'] = Line(points=(touch.x, touch.y - 20))  # starts a new line with +20 offset
            # ---- the new line only works for drawing horizontal ----
            print("mouse donw:", touch.pos)

    def on_touch_move(self, touch):

        if touch.y == self.old_touch_y and touch.x > self.old_touch_x:
            # Right
            touch.ud['line'].points += [touch.x, touch.y]
            while touch.x > self.old_touch_x:
                touch.ud['line2'].points += [touch.x + 0.1, touch.y-20]
                self.old_touch_x += 0.1

        elif touch.x == self.old_touch_x and touch.y > self.old_touch_y:
            # Up
            touch.ud['line'].points += [touch.x, touch.y]
            while touch.y > self.old_touch_y:
                touch.ud['line2'].points += [touch.x+20, touch.y+0.1]
                self.old_touch_y += 0.1

        elif touch.y == self.old_touch_y and touch.x < self.old_touch_x:
            # Left
            touch.ud['line'].points += [touch.x, touch.y]
            while touch.x < self.old_touch_x:
                touch.ud['line2'].points += [touch.x - 0.1, touch.y + 20]
                self.old_touch_x -= 0.1

        elif touch.x == self.old_touch_x and touch.y < self.old_touch_y:
            # Down
            touch.ud['line'].points += [touch.x, touch.y]
            while touch.y < self.old_touch_y:
                touch.ud['line2'].points += [touch.x-20, touch.y-0.1]
                self.old_touch_y -= 0.1

        self.old_touch_x = touch.x
        self.old_touch_y = touch.y


class ReinforcementApp(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("main.kv")


class ReinforcementSimulator(App):

    def save(self):
        print("save")

    """
    def call_runSimulator(self, event):
        print("button pressed")
        print(event)

    def call_runDrawingTool(self, event):
        print("button pressed")
        print(event)
    """

    def build(self):
        """
        layout = FloatLayout()  # creates a float layout

        button_run = Button(text="Run", background_color=(0, 0, 128, 0.4), pos=(300, 350), size_hint=(.25, .18))    # run simulation button
        button_tool = Button(text="Drawing tool", background_color=(0, 0, 128, 0.4), pos=(300, 150), size_hint=(.25, .18))  # run drawing tool button
        button_run.bind(on_press=self.call_runSimulator)
        button_tool.bind(on_press=self.call_runDrawingTool)
        layout.add_widget(button_run)   # add the buttons to the layout
        layout.add_widget(button_tool)
        return layout
        """
        return kv
