from Toy import *
from Agent import *
import sys


# Master function that creates a family of models given two toys and gets
# all the model choices.
def GetModelChoices(ToyA, ToyB, ConditionName, ExploreProb=1, ToyAName="Toy0", ToyBName="Toy1", header=True):
    """
    Get the utilities of all kinds of agents.
    header (bool): Add header to file?
    """
    # Create all kinds of agents and get their choices.
    # Params: Learner cost & reward, teacher cost & reward, discover cost & reward
    # Four main models: Use/Ignore learner's utility. Use/Ignore learner's
    # exploration
    A_DiscoverOnly = Agent([ToyA, ToyB], 0, 0, 1, 1, ExploreProb,
                 [ToyAName, ToyBName]).Teach()
    A_InstructionOnly = Agent([ToyA, ToyB], 1, 1, 0, 0, ExploreProb,
                 [ToyAName, ToyBName]).Teach()
    A_FullModel = Agent([ToyA, ToyB], 1, 1, 1, 1, ExploreProb,
                 [ToyAName, ToyBName]).Teach()
    A_CostsOnly = Agent([ToyA, ToyB], 1, 0, 1, 0, ExploreProb,
                 [ToyAName, ToyBName]).Teach()
    A_RewardOnly = Agent([ToyA, ToyB], 0, 1, 0, 1, ExploreProb,
                 [ToyAName, ToyBName]).Teach()
    if header:
        sys.stdout.write("Condition,"+str(ToyAName)+"Reward,"+str(ToyBName) +
                         "Reward,LearnC,LearnR,DiscoverC,DiscoverR,ExploreProb,Decision\n")
    sys.stdout.write(str(ConditionName)+","+str(ToyA.reward) + "," +
                     str(ToyB.reward) + ",0,0,1,1," + str(ExploreProb) + "," + str(A_DiscoverOnly) + "\n")
    sys.stdout.write(str(ConditionName)+","+str(ToyA.reward) + "," +
                     str(ToyB.reward) + ",1,1,0,0," + str(ExploreProb) + "," + str(A_InstructionOnly) + "\n")
    sys.stdout.write(str(ConditionName)+","+str(ToyA.reward) + "," +
                     str(ToyB.reward) + ",1,1,1,1," + str(ExploreProb) + "," + str(A_FullModel) + "\n")
    sys.stdout.write(str(ConditionName)+","+str(ToyA.reward) + "," +
                     str(ToyB.reward) + ",1,0,1,0," + str(ExploreProb) + "," + str(A_CostsOnly) + "\n")
    sys.stdout.write(str(ConditionName)+","+str(ToyA.reward) + "," +
                     str(ToyB.reward) + ",0,1,0,1," + str(ExploreProb) + "," + str(A_RewardOnly) + "\n")

# Up to what value can the red toy's reward be?
CoolRewardSpace = range(1, 57)
LameRewardSpace = range(1, 57)

for CoolReward in CoolRewardSpace:
    ## These are two different parameters for
    ## probability that child will explore second toy
    ExploreProbabilities = [0.25, 0.5, 0.75, 1]
    # Run family of models on all four conditions
    # Run each model twice, one with low exploration pobability and one with
    # high probability.
    for LameReward in LameRewardSpace:
        for ExploreProb in ExploreProbabilities:
            RedToy = Toy(buttons=1, activation=0, cost=1, reward=LameReward)
            YellowToy = Toy(buttons=7, activation=[0, 1], cost=1, reward=CoolReward)
            # Some extra code here so it only prints the header on the first iteration
            # of the loop
            ## Every line is repeated twice, running the same code for different exploration probabilities.
            if LameReward == 1 and CoolReward == 1 and ExploreProb==ExploreProbabilities[0]:
                GetModelChoices(RedToy, YellowToy, "1: R&C", ExploreProb,
                                     "RedToy", "YellowToy", True)
            else:
                GetModelChoices(RedToy, YellowToy, "1: R&C", ExploreProb,
                                     "RedToy", "YellowToy", False)
            RedToy = Toy(buttons=1, activation=0, cost=1, reward=CoolReward)
            YellowToy = Toy(buttons=1, activation=0, cost=1, reward=LameReward)
            GetModelChoices(RedToy, YellowToy, "2: Diff. R", ExploreProb,
                                 "RedToy", "YellowToy", False)
            RedToy = Toy(buttons=1, activation=0, cost=1, reward=LameReward)
            YellowToy = Toy(buttons=7, activation=[0, 1], cost=1, reward=LameReward)
            GetModelChoices(RedToy, YellowToy, "3: Diff. C", ExploreProb, "RedToy", "YellowToy", False)
            RedToy = Toy(buttons=1, activation=0, cost=1, reward=CoolReward)
            YellowToy = Toy(buttons=7, activation=[0, 1], cost=1, reward=LameReward)
            GetModelChoices(RedToy, YellowToy, "4: RvC",
                                 ExploreProb, "RedToy", "YellowToy", False)
