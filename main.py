from kivy.app import App
from kivy.uix.label import Label


class ReinforcementCar(App):
    def build(self):
        return Label(text="hello")


if __name__ == '__main__':
    ReinforcementCar().run()
