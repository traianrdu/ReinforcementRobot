from Environment.training_env import RiCart
from AI.agent import Agent
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


def auto_run(map_env, env):
    """Handle auto run"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # check if the event is the close (X) button
            map_env.running = False  # quit the game
            env.running = False  # quit the game

    map_env.leader.random_move(map_env.object_list_without_current(map_env.leader))  # move the leader randomly
    map_env.dynamic_object1.random_move(
        map_env.object_list_without_current(map_env.dynamic_object1))  # move the dynamic object
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


def train():
    """Train function"""
    plot_score = []  # score
    plot_avg_score = []  # avg score
    total_score = 0  # total score
    record = 0  # record
    agent = Agent()  # init agent
    training_env = RiCart()  # training env
    training_env.running = True
    while training_env.running:
        state_old = agent.get_state(training_env)  # get old state
        final_move = agent.get_action(state_old)  # get the movement
        reward, done, score = env.step(final_move)  # perform movement
        state_new = agent.get_state(training_env)  # get the new state
        agent.train_short(state_old, final_move, reward, state_new, done)  # short train
        agent.remember(state_old, final_move, reward, state_new, done)  # save the state

        if done:
            training_env.reset()  # reset the env
            agent.n_plays += 1  # increase number of plays
            agent.train_long()  # train long

            if score > record:
                record = score  # save new record
                agent.model.save()

            print('Run', agent.n_plays, 'Score', score, 'Record:', record)  # print stats
            # TODO: plot the results
            total_score += score    # total score
            avg_score = total_score / agent.n_plays     # mean score


def run(map_env, env):
    """Starts the environment loop"""
    env.running = True
    while env.running:
        # self.handle_events()  # handles the events of the game
        # auto_run(map_env, env)  # auto run
        reward, game_over, score = env.step("")
        if game_over:
            env.reset()

    pygame.quit()


if __name__ == '__main__':
    # Map(900, 900, Vector2(20, 20)).run()
    env = RiCart()
    run(env.map, env)
