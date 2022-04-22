import torch
import random
import numpy as np
from Environment.training_env import RiCart as rc
from collections import deque

MAX_MEMORY = 100_000  # max memory used
BATCH_SIZE = 1000  # batch size
LR = 0.001  # learning rate


class Agent:

    def __init__(self):
        self.n_plays = 0
        self.epsilon = 0  # controls randomness of the env
        self.gamma = 0  # discount rate
        self.memory = deque(maxlen=MAX_MEMORY)  # it will remove elements if we exceed memory

    def get_state(self, train_env):
        """Gets the state to calculate the next move."""
        pass

    def remember(self, state, action, reward, next_state, done):
        """Saves the state"""
        pass

    def train_long(self):
        """Trains for the long memory"""
        pass

    def train_short(self, state, action, reward, next_state, done):
        """Trains for the short memory"""
        pass

    def get_action(self, state):
        """Get the action based on the state"""
        pass
