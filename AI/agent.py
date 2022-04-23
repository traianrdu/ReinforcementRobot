import torch
import random
import numpy as np
from Environment.training_env import RiCart as rc
from Utility.vector2 import Vector2
from collections import deque
from Environment.map import Direction
from AI.model import LinearQNet
from AI.trainer import QTrainer

MAX_MEMORY = 100_000  # max memory used
BATCH_SIZE = 1000  # batch size
LR = 0.001  # learning rate
MOVEMENT_STEP = 0.1


class Agent:

    def __init__(self):
        self.n_plays = 0
        self.epsilon = 80  # controls randomness of the env
        self.gamma = 0.9  # discount rate
        self.memory = deque(maxlen=MAX_MEMORY)  # it will remove elements if we exceed memory
        self.model = LinearQNet(24, 256, 8)   # model - 8 inputs (can change them if I find more), 8 outputs
        self.trainer = QTrainer(model=self.model, learning_rate=LR, gamma=self.gamma)

    def get_state(self, train_env):
        """Gets the state to calculate the next move."""
        # points of potential movement
        point_N = Vector2(train_env.map.cart.coordinates.x, train_env.map.cart.coordinates.y - MOVEMENT_STEP)
        point_S = Vector2(train_env.map.cart.coordinates.x, train_env.map.cart.coordinates.y + MOVEMENT_STEP)
        point_W = Vector2(train_env.map.cart.coordinates.x - MOVEMENT_STEP, train_env.map.cart.coordinates.y)
        point_E = Vector2(train_env.map.cart.coordinates.x + MOVEMENT_STEP, train_env.map.cart.coordinates.y)
        point_NE = Vector2(train_env.map.cart.coordinates.x + MOVEMENT_STEP, train_env.map.cart.coordinates.y - MOVEMENT_STEP)
        point_NW = Vector2(train_env.map.cart.coordinates.x - MOVEMENT_STEP, train_env.map.cart.coordinates.y - MOVEMENT_STEP)
        point_SE = Vector2(train_env.map.cart.coordinates.x + MOVEMENT_STEP, train_env.map.cart.coordinates.y + MOVEMENT_STEP)
        point_SW = Vector2(train_env.map.cart.coordinates.x - MOVEMENT_STEP, train_env.map.cart.coordinates.y + MOVEMENT_STEP)

        # current direction
        dir_N = train_env.direction == Direction.N
        dir_S = train_env.direction == Direction.S
        dir_W = train_env.direction == Direction.W
        dir_E = train_env.direction == Direction.E
        dir_NE = train_env.direction == Direction.NE
        dir_NW = train_env.direction == Direction.NW
        dir_SE = train_env.direction == Direction.SE
        dir_SW = train_env.direction == Direction.SW

        state = [
            # Danger N
            (dir_N and train_env.map.cart.collide_box(point_N)),

            # Danger S
            (dir_S and train_env.map.cart.collide_box(point_S)),

            # Danger W
            (dir_W and train_env.map.cart.collide_box(point_W)),

            # Danger E
            (dir_E and train_env.map.cart.collide_box(point_E)),

            # Danger NE
            (dir_NE and train_env.map.cart.collide_box(point_NE)),

            # Danger NW
            (dir_NW and train_env.map.cart.collide_box(point_NW)),

            # Danger SE
            (dir_SE and train_env.map.cart.collide_box(point_SE)),

            # Danger SW
            (dir_SW and train_env.map.cart.collide_box(point_SW)),

            # Move direction
            dir_N,
            dir_S,
            dir_W,
            dir_E,
            dir_NE,
            dir_NW,
            dir_SE,
            dir_SW,

            # Leader location
            train_env.map.leader.coordinates.y < train_env.map.cart.coordinates.y,  # leader N
            train_env.map.leader.coordinates.y > train_env.map.cart.coordinates.y,  # leader S
            train_env.map.leader.coordinates.x < train_env.map.cart.coordinates.x,  # leader W
            train_env.map.leader.coordinates.x > train_env.map.cart.coordinates.x,  # leader E


            (train_env.map.leader.coordinates.x > train_env.map.cart.coordinates.x and
             train_env.map.leader.coordinates.y < train_env.map.cart.coordinates.y),  # leader NE

            (train_env.map.leader.coordinates.x < train_env.map.cart.coordinates.x and
             train_env.map.leader.coordinates.y < train_env.map.cart.coordinates.y),  # leader NW

            (train_env.map.leader.coordinates.x > train_env.map.cart.coordinates.x and
             train_env.map.leader.coordinates.y > train_env.map.cart.coordinates.y),  # leader SE

            (train_env.map.leader.coordinates.x < train_env.map.cart.coordinates.x and
             train_env.map.leader.coordinates.y > train_env.map.cart.coordinates.y)  # leader SW
        ]

        return np.array(state, dtype=int)

    def remember(self, state, action, reward, next_state, done):
        """Saves the state"""
        self.memory.append((state, action, reward, next_state, done))  # popleft if max memory is reached

    def train_long(self):
        """Trains for the long memory"""
        if len(self.memory) > BATCH_SIZE:
            # get random samples from our saved memory
            mini_sample = random.sample(self.memory, BATCH_SIZE)  # list of tuples
        else:
            mini_sample = self.memory   # we get the whole memory

        # extract them from the memory and it puts every states together, every actions together, every...
        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)   # call the trainer

    def train_short(self, state, action, reward, next_state, done):
        """Trains for the short memory"""
        self.trainer.train_step(state, action, reward, next_state, done)

    def get_action(self, state):
        """Get the action based on the state. Random moves in the beginning and more trained actions in the future"""
        self.epsilon = 80 - self.n_plays    # hardcoded value for number of steps
        final_move = [0, 0, 0, 0, 0, 0, 0, 0]   # final move for the 8 direction movement
        # the lower the epsilon, the less frequent we will have random movement
        if random.randint(0, 200) < self.epsilon:
            move = random.randint(0, 7)  # from 0-7 movements
            final_move[move] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)  # prediction
            move = torch.argmax(prediction).item()
            final_move[move] = 1

        return final_move
