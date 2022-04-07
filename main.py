from Environment.training_env import RiCart
import pygame


'''
class ReinforcementCar(App):
    def build(self):
        return Label(text="hello")
'''


def handle_events(map_env):
    """Handle the press key events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # check if the event is the close (X) button
            map_env.running = False  # quit the game

    keys = pygame.key.get_pressed()  # return pressed key

    map_env.leader.keyboard_move(keys, map_env.object_list_without_current(map_env.leader))
    map_env.render()  # render the simulation


def auto_run(map_env):
    """Handle auto run"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # check if the event is the close (X) button
            map_env.running = False  # quit the game

    map_env.leader.random_move(map_env.object_list_without_current(map_env.leader))  # move the leader randomly
    map_env.dynamic_object1.random_move(map_env.object_list_without_current(map_env.dynamic_object1))  # move the dynamic object
    map_env.dynamic_object1.random_move(
        map_env.object_list_without_current(map_env.dynamic_object1))  # move the dynamic object
    map_env.dynamic_object2.random_move(
        map_env.object_list_without_current(map_env.dynamic_object2))  # move the dynamic object
    map_env.dynamic_object3.random_move(
        map_env.object_list_without_current(map_env.dynamic_object3))  # move the dynamic object
    map_env.dynamic_object4.random_move(
        map_env.object_list_without_current(map_env.dynamic_object4))  # move the dynamic object
    map_env.dynamic_object5.random_move(
        map_env.object_list_without_current(map_env.dynamic_object5))  # move the dynamic object
    map_env.render()  # render the simulation


def run(map_env):
    """Starts the environment loop"""
    running = True
    while running:
        # self.handle_events()  # handles the events of the game
        auto_run(map_env)  # auto run

    pygame.quit()


if __name__ == '__main__':
    #Map(900, 900, Vector2(20, 20)).run()
    environment = RiCart()
    run(environment.map)


