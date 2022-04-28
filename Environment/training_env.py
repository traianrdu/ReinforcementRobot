from Environment.map import Map, Vector2, Direction
import pygame


class RiCart:

    def __init__(self):
        self.map = Map(900, 900, Vector2(20, 20))
        self.cart = self.map.cart
        self.score = 0  # init score
        self.n_step = 0  # number of taken steps
        self.running = True  # is the game running or not
        self.direction = Direction.STAY  # default direction
        self.cart_old_coordinates = Vector2(self.cart.coordinates.x, self.cart.coordinates.y)   # cart old coordinates
        self.leader_old_coordinates = Vector2(self.map.leader.coordinates.x, self.map.leader.coordinates.y)  # leader old coordinates

    def reset(self):
        """Reset environment"""
        self.n_step = 0  # reset number of taken steps
        self.score = 0  # reset score
        self.direction = Direction.STAY  # default direction
        self.map.reset()    # reset map

    def step(self, action):
        """New step"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # check if the event is the close (X) button
                self.running = False  # quit the game

        self.n_step += 1    # increase number of taken steps
        reward = 0  # reward
        game_over = False  # game over

        self.move(action)  # move the cart
        self.move_objects()  # move the objects
        self.map.render()  # render the map

        if self.cart.did_collide():  # if we detect collide
            reward = -10
            game_over = True
            return reward, game_over, self.score

        if self.cart.did_follow(self.cart_old_coordinates, self.leader_old_coordinates,
                                Vector2(self.map.leader.coordinates.x, self.map.leader.coordinates.y)):  # if the cart follows the leader
            reward = 10  # we get extra reward
            self.score += 1  # increase score
            return reward, game_over, self.score

        # else it just did move one step without collision
        return reward, game_over, self.score, self.n_step

    def move(self, action):
        """Movement action"""
        self.cart_old_coordinates = Vector2(self.cart.coordinates.x, self.cart.coordinates.y)   # save old coordinates
        direction = 0   # init direction
        # init direction array
        direction_array = [Direction.N, Direction.S, Direction.W, Direction.E, Direction.NE, Direction.NW, Direction.SE, Direction.SW, Direction.STAY]
        for index in range(len(action)):
            if action[index] == 1:  # when we have a direction set
                direction = direction_array[index]  # get right the direction
                break

        self.direction = direction

        if direction == Direction.N:
            self.cart.move_N()

        elif direction == Direction.S:
            self.cart.move_S()

        elif direction == Direction.W:
            self.cart.move_W()

        elif direction == Direction.E:
            self.cart.move_E()

        elif direction == Direction.NW:
            self.cart.move_NW()

        elif direction == Direction.NE:
            self.cart.move_NE()

        elif direction == Direction.SW:
            self.cart.move_SW()

        elif direction == Direction.SE:
            self.cart.move_SE()

        elif direction == Direction.STAY:
            self.cart.stay()

        else:
            self.cart.coordinates.y += 0.0
            self.cart.coordinates.x += 0.0

    def move_objects(self):
        """Move the rest of the objects"""
        self.leader_old_coordinates = Vector2(self.map.leader.coordinates.x, self.map.leader.coordinates.y)  # save old coordinates
        self.map.leader.random_move(
            self.map.object_list_without_current(self.map.leader))  # move the leader randomly
        self.map.dynamic_object1.random_move(
            self.map.object_list_without_current(self.map.dynamic_object1))  # move the dynamic object
        self.map.dynamic_object1.random_move(
            self.map.object_list_without_current(self.map.dynamic_object1))  # move the dynamic object
        self.map.dynamic_object2.random_move(
            self.map.object_list_without_current(self.map.dynamic_object2))  # move the dynamic object
        self.map.dynamic_object3.random_move(
            self.map.object_list_without_current(self.map.dynamic_object3))  # move the dynamic object
        self.map.dynamic_object4.random_move(
            self.map.object_list_without_current(self.map.dynamic_object4))  # move the dynamic object
        self.map.dynamic_object5.random_move(
            self.map.object_list_without_current(self.map.dynamic_object5))  # move the dynamic object
