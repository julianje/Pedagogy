# -*- coding: utf-8 -*-
import sys


class Agent(object):

    def __init__(self, toys=[], LearnC=1, LearnR=1, DiscoverC=1, DiscoverR=1, ExploreProb=1, toynames=[0, 1]):
        """
        toys[]: List of toy objects.
        Learn (bool): Does the agent care about the learner's experience with the taught toy?
        ExploreProb (float): Probability that the agent will choose to explore the other toy.
        Discover (bool): does the agent care about the costs and rewards associated with discovery?
        teacherreward (string): "Constant" or "Variable". Determines if teacher gets a constant reward for teaching or not.
        """
        if len(toys) != 2:
            print "Error: Code only supports reasoning about two toys."
            return None
        self.toys = toys
        self.rewards = [i.reward for i in self.toys]
        self.costs = [i.cost for i in self.toys]
        self.ExploreProb = ExploreProb
        self.UseLearnC = LearnC
        self.UseDiscoverC = DiscoverC
        self.UseLearnR = LearnR
        self.UseDiscoverR = DiscoverR
        self.toynames = toynames

    def TeachToy(self, toyid):
        """
        Get utility for teaching toy with id toyid
        """
        if toyid < 0 or toyid > len(self.toys):
            print "Error: No such toy"
            return None
        # If agent cares about learner's costs and rewards with taugh toy.
        [c_L, r_L] = self.toys[toyid].Play(self.toys[toyid].activation)
        if not self.UseLearnR:
            r_L = 0
        if not self.UseLearnC:
            c_L = 0
        # If agent cares about what the learner will do with the untaught
        # toy.
        [c_D, r_D] = [
            self.ExploreProb*i for i in self.toys[int(not toyid)].Discover()]
        if not self.UseDiscoverR:
            r_D = 0
        if not self.UseDiscoverC:
            c_D = 0
        # return costs and rewards
        return [c_L + c_D, r_L + r_D]

    def Teach(self, utilities=False):
        """
        Choose which toy to teach.
        utilities (bool): Should we return utilities as well?
        """
        # option 1
        [c0, r0] = self.TeachToy(0)
        # option 2
        [c1, r1] = self.TeachToy(1)
        # Costs are already negative so you have to add them!
        if (r0+c0 > r1+c1):
            choice = self.toynames[0]
        elif (r0+c0 < r1+c1):
            choice = self.toynames[1]
        else:
            choice = "Either"
        if utilities:
            return [r0+c0, r1+c1, choice]
        else:
            return choice

    def PrintSummary(self, header=True):
        if header:
            sys.stdout.write()
