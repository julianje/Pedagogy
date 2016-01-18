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
        return([np.mean(costs), self.reward])

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
