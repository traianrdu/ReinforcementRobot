from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.widget import Widget
#from kivy.graphics import Rectangle, Color, Line, Ellipse
from functools import partial
from Utility import algebra
from Environment.map import Map, Vector2
from GUI.drawingToolV1 import DrawingToolV1
from GUI.drawingToolV2 import DrawingToolV2


class MainWindow(Screen):
    pass


class DrawingTool(Screen):
    pass


class ReinforcementApp(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("GUI/main.kv")


class ReinforcementSimulator(App):

    dtV1 = DrawingToolV1()
    dtV2 = DrawingToolV2()

    def call_runSimulator(self, event):
        print("button pressed")
        print(event)
        Map(900, 900, Vector2(20, 20)).run()
    """
    

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
        #return kv

        # i can't use pygame with kivy events
        layout = FloatLayout()  # creates a float layout

        button_run = Button(text="Run", background_color=(0, 0, 128, 0.4), pos=(300, 350),
                            size_hint=(.25, .18))  # run simulation button
        button_run.bind(on_press=self.call_runSimulator)
        layout.add_widget(button_run)  # add the buttons to the layout
        return layout
