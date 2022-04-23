from Environment.map import Map, Vector2, Direction
import pygame


class RiCart:

    def __init__(self):
        self.map = Map(900, 900, Vector2(20, 20))
        self.cart = self.map.cart
        self.score = 0
        self.running = True  # is the game running or not
        self.direction = Direction.N

    def reset(self):
        """Reset environment"""
        self.score = 0
        self.direction = Direction.N
        self.map.reset()

    def step(self, action):
        """New step"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # check if the event is the close (X) button
                self.running = False  # quit the game

        reward = 0  # reward
        game_over = False  # game over

        self.move(action)  # move the cart
        self.move_objects()  # move the objects
        self.map.render()  # render the map

        if self.cart.did_collide():  # if we detect collide
            reward = -10
            game_over = True
            return reward, game_over, self.score

        if self.cart.did_follow():  # if the cart follows the leader
            reward = 10  # we get extra reward
            self.score += 1  # increase score
            return reward, game_over, self.score

        reward = 5  # else it just did move one step without collision
        self.score += 1  # increase the score
        return reward, game_over, self.score

    def move(self, direction):
        """Movement action"""

        # TODO: we get an array (direction) so I have to convert it to our direction before

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

        else:
            self.cart.coordinates.y += 0.0
            self.cart.coordinates.x += 0.0

    def move_objects(self):
        self.map.leader.random_move(self.map.object_list_without_current(self.map.leader))  # move the leader randomly
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
