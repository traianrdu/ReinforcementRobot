#from kivy.app import App
#from kivy.uix.label import Label
#from GUI.interface import ReinforcementSimulator
from Environment.map import Map, Vector2


'''
class ReinforcementCar(App):
    def build(self):
        return Label(text="hello")
'''


if __name__ == '__main__':
    #ReinforcementCar().run()
    #ReinforcementSimulator().run()
    #RacingTrack(900, 900, Vector2(20, 20)).run()
    Map(900, 900, Vector2(20, 20)).run()


