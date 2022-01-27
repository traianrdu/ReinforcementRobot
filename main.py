from kivy.app import App
from kivy.uix.label import Label
from GUI.interface import ReinforcementSimulator


class ReinforcementCar(App):
    def build(self):
        return Label(text="hello")


if __name__ == '__main__':
    #ReinforcementCar().run()
    ReinforcementSimulator().run()

