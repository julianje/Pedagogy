# -*- coding: utf-8 -*-
import random
import itertools
import numpy as np


class Toy(object):

    def __init__(self, buttons, activation, cost=1, reward=5):
        self.buttons = range(buttons) if isinstance(buttons, int) else buttons
        self.activation = [activation] if isinstance(
            activation, int) else activation
        if not set(self.activation).issubset(set(self.buttons)):
            print "Error: Activation sequence uses buttons that don't exist."
            return None
        self.cost = -cost
        if reward <= 0:
            print "Error: Reward must be positive"
            return None
        self.reward = reward
        self.expcost = None
        # Hacky code. I already know the expected cost so no need to keep
        # recomputing it!
        if self.buttons == 6 and length(self.action) == 2:
            self.expcost = -22.063199999999998
        if self.buttons == 1 and length(self.action) == 1:
            self.expcost = -1

    def Play(self, action):
        # The cost is linear as a function of presses.
        #############################
        # Should the cost be be a linear function of buttons pressed?
        #############################
        cost = -len(action)
        # Reward is 0 unless the correct buttons are pressed.
        reward = self.reward if set(
            self.activation).issubset(set(action)) else 0
        #reward = self.reward if set(action) == set(self.activation) else 0
        return [cost, reward]

    def Discover(self, samples=1000):
        # Get expected cost by assuming that learner starts with the simplest
        # hypotheses
        if self.expcost is not None:
            return ([self.expcost, self.reward])
        else:
            costs = [0] * samples
            for i in range(samples):
                complete = False
                sequencelength = 0
                while(True):
                    sequencelength += 1
                    Actions = self.ActionSpace(sequencelength)
                    random.shuffle(Actions)
                    for attempt in Actions:
                        [c, r] = self.Play(attempt)
                        costs[i] += c
                        if r != 0:
                            complete = True
                            break
                    if complete:
                        break
            self.expcost = np.mean(costs)
        return([self.expcost, self.reward])

    def Teach(self, rewardtype="Constant"):
        #############################
        # Should the the teacher get a reward? Should it depend on whether the toy is cool?
        # For now, the teacher gets a constant reward of 1 for teaching.
        #############################
        if (rewardtype == "Constant"):
            # Get a constant reward
            return([self.cost * len(self.activation), 1])
        else:
            # Get a reward for watching the toy
            return([self.cost * len(self.activation), self.reward])

    def ActionSpace(self, size=-1):
        # Get the list of all collections of button presses
        if size == -1:
            return reduce(lambda result, x: result + [subset + [x] for subset in result],
                          self.buttons, [[]])
        else:
            return [list(i) for i in map(set, itertools.combinations(set(self.buttons), size))]
