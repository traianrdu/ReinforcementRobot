import numpy as np
import random


class RandomWalk2D:

    def __init__(self, steps, directions):
        """Init random walk"""
        self.steps = steps  # number of steps
        self.directions = directions    # direction list

    def random_walk2D(self):
        """Random walk"""
        x = np.zeros(self.steps)    # x array of zeros for every steps ex: x = [0, 0, 0,..., n]
        y = np.zeros(self.steps)

        for step in range(1, self.steps):   # for every step
            random_direction = random.choice(self.directions)   # get a random direction

            if random_direction == "N":
                x[step] = x[step - 1]
                y[step] = y[step - 1] + 1
            elif random_direction == "S":
                x[step] = x[step - 1]
                y[step] = y[step - 1] - 1
            elif random_direction == "W":
                x[step] = x[step - 1] - 1
                y[step] = y[step - 1]
            elif random_direction == "E":
                x[step] = x[step - 1] + 1
                y[step] = y[step - 1]
            elif random_direction == "NW":
                x[step] = x[step - 1] - 1
                y[step] = y[step - 1] + 1
            elif random_direction == "NE":
                x[step] = x[step - 1] + 1
                y[step] = y[step - 1] + 1
            elif random_direction == "SW":
                x[step] = x[step - 1]
                y[step] = y[step - 1]
            elif random_direction == "SE":
                x[step] = x[step - 1]
                y[step] = y[step - 1]
            else:
                x[step] = x[step - 1]
                y[step] = y[step - 1]

        return x, y     # return all positions of an object
