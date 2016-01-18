from Toy import *
from Agent import *
import sys


# Master function that creates a family of models given two toys and gets
# all the model choices.
def GetChoicesMainModels(ToyA, ToyB, ConditionName, ExploreProb=1, ToyAName="Toy0", ToyBName="Toy1", teacherreward="Constant", header=True):
    """
    Get the utilities of all kinds of agents.
    teacherreward should be "Constant" or "Variable"
    header (bool): Add header to file?
    """
    # Create all kinds of agents and get their choices.
    # Parameters: Learner cost, learner reward, teacher cost, teacher reward, discover cost, discover reward
    # Four main models: Use/Ignore learner's utility. Use/Ignore learner's
    # exploration
    A_00 = Agent([ToyA, ToyB], 0, 0, 0, 0, 0, 0, ExploreProb,
                 [ToyAName, ToyBName], teacherreward).Teach()
    A_01 = Agent([ToyA, ToyB], 0, 0, 0, 0, 1, 1, ExploreProb,
                 [ToyAName, ToyBName], teacherreward).Teach()
    A_10 = Agent([ToyA, ToyB], 1, 1, 0, 0, 0, 0, ExploreProb,
                 [ToyAName, ToyBName], teacherreward).Teach()
    A_11 = Agent([ToyA, ToyB], 1, 1, 0, 0, 1, 1, ExploreProb,
                 [ToyAName, ToyBName], teacherreward).Teach()
    if header:
        sys.stdout.write("Condition,"+str(ToyAName)+"Reward,"+str(ToyBName) +
                         "Reward,LearnC,LearnR,TeachC,TeachR,DiscoverC,DiscoverR,ExploreProb,TeacherReward,Decision\n")
    sys.stdout.write(str(ConditionName)+","+str(ToyA.reward) + "," +
                     str(ToyB.reward) + ",0,0,0,0,0,0," + str(ExploreProb) + "," + str(teacherreward) + "," + str(A_00) + "\n")
    sys.stdout.write(str(ConditionName)+","+str(ToyA.reward) + "," +
                     str(ToyB.reward) + ",0,0,0,0,1,1," + str(ExploreProb) + "," + str(teacherreward) + "," + str(A_01) + "\n")
    sys.stdout.write(str(ConditionName)+","+str(ToyA.reward) + "," +
                     str(ToyB.reward) + ",1,1,0,0,0,0," + str(ExploreProb) + "," + str(teacherreward) + "," + str(A_10) + "\n")
    sys.stdout.write(str(ConditionName)+","+str(ToyA.reward) + "," +
                     str(ToyB.reward) + ",1,1,0,0,1,1," + str(ExploreProb) + "," + str(teacherreward) + "," + str(A_11) + "\n")


# Up to what value can the red toy's reward be?
RedToyRLimit = 50

# Run the main set of models: Use/Ignore learner's learned toy and discovered toy.
# Need these as model parameters, but don't matter
teacherreward = "Constant"
YellowToyR = 5
ExploreProb = 0.5
# Run family of models on all four conditions
# Run each model twice, one with low exploration pobability and one with
# high probability.
for RedToyR in range(1, RedToyRLimit+1):
    RedToy = Toy(buttons=1, activation=0, cost=1, reward=RedToyR)
    YellowToy = Toy(buttons=6, activation=[
                    0, 1], cost=1, reward=YellowToyR)
    # Some extra code here so it only prints the header on the first iteration
    # of the loop
    if RedToyR == 1:
        GetChoicesMainModels(RedToy, YellowToy, "Unequal_Costs", 0.5,
                             "RedToy", "YellowToy", teacherreward, True)
    else:
        GetChoicesMainModels(RedToy, YellowToy, "Unequal_Costs", 0.5,
                             "RedToy", "YellowToy", teacherreward, False)
    GetChoicesMainModels(RedToy, YellowToy, "Unequal_Costs", 1,
                         "RedToy", "YellowToy", teacherreward, False)
    RedToy = Toy(buttons=1, activation=0, cost=1, reward=RedToyR)
    YellowToy = Toy(buttons=1, activation=0, cost=1, reward=YellowToyR)
    GetChoicesMainModels(RedToy, YellowToy, "Equal_Costs", 0.5,
                         "RedToy", "YellowToy", teacherreward, False)
    GetChoicesMainModels(RedToy, YellowToy, "Equal_Costs", 1,
                         "RedToy", "YellowToy", teacherreward, False)
    RedToy = Toy(buttons=1, activation=0, cost=1, reward=YellowToyR)
    YellowToy = Toy(buttons=6, activation=[
                    0, 1], cost=1, reward=YellowToyR)
    GetChoicesMainModels(RedToy, YellowToy, "Matched_Rewards",
                         0.5, "RedToy", "YellowToy", teacherreward, False)
    GetChoicesMainModels(RedToy, YellowToy, "Matched_Rewards",
                         1, "RedToy", "YellowToy", teacherreward, False)
    RedToy = Toy(buttons=1, activation=0, cost=1, reward=YellowToyR)
    YellowToy = Toy(buttons=6, activation=[0, 1], cost=1, reward=RedToyR)
    GetChoicesMainModels(RedToy, YellowToy, "Inverted_Rewards",
                         0.5, "RedToy", "YellowToy", teacherreward, False)
    GetChoicesMainModels(RedToy, YellowToy, "Inverted_Rewards",
                         1, "RedToy", "YellowToy", teacherreward, False)


# Run models exploring cost and reward usage rather than the whole thing.
def GetChoicesCRModels(ToyA, ToyB, ConditionName, ExploreProb=1, ToyAName="Toy0", ToyBName="Toy1", teacherreward="Constant", header=True):
    """
    Get the utilities of all kinds of agents.
    teacherreward should be "Constant" or "Variable"
    header (bool): Add header to file?
    """
    # Create all kinds of agents and get their choices.
    # Parameters: Learner cost, learner reward, teacher cost, teacher reward, discover cost, discover reward
    # Four main models: Use/Ignore learner's costs. Use/Ignore learner's
    # rewards
    A_01 = Agent([ToyA, ToyB], 1, 0, 0, 0, 1, 0, ExploreProb,
                 [ToyAName, ToyBName], teacherreward).Teach()
    A_10 = Agent([ToyA, ToyB], 0, 1, 0, 0, 0, 1, ExploreProb,
                 [ToyAName, ToyBName], teacherreward).Teach()
    if header:
        sys.stdout.write("Condition,"+str(ToyAName)+"Reward,"+str(ToyBName) +
                         "Reward,LearnC,LearnR,TeachC,TeachR,DiscoverC,DiscoverR,ExploreProb,TeacherReward,Decision\n")
    sys.stdout.write(str(ConditionName)+","+str(ToyA.reward) + "," +
                     str(ToyB.reward) + ",1,0,0,0,1,0," + str(ExploreProb) + "," + str(teacherreward) + "," + str(A_01) + "\n")
    sys.stdout.write(str(ConditionName)+","+str(ToyA.reward) + "," +
                     str(ToyB.reward) + ",0,1,0,0,0,1," + str(ExploreProb) + "," + str(teacherreward) + "," + str(A_10) + "\n")

# Up to what value can the red toy's reward be?
RedToyRLimit = 50

# Run the main set of models: Use/Ignore costs and rewards.
# Need these as model parameters, but don't matter
teacherreward = "Constant"
YellowToyR = 5
ExploreProb = 0.5
# Run family of models on all four conditions
# Run each model twice, one with low exploration pobability and one with
# high probability.
for RedToyR in range(1, RedToyRLimit+1):
    RedToy = Toy(buttons=1, activation=0, cost=1, reward=RedToyR)
    YellowToy = Toy(buttons=6, activation=[
                    0, 1], cost=1, reward=YellowToyR)
    GetChoicesCRModels(RedToy, YellowToy, "Unequal_Costs", 0.5,
                       "RedToy", "YellowToy", teacherreward, False)
    GetChoicesCRModels(RedToy, YellowToy, "Unequal_Costs", 1,
                       "RedToy", "YellowToy", teacherreward, False)
    RedToy = Toy(buttons=1, activation=0, cost=1, reward=RedToyR)
    YellowToy = Toy(buttons=1, activation=0, cost=1, reward=YellowToyR)
    GetChoicesCRModels(RedToy, YellowToy, "Equal_Costs", 0.5,
                       "RedToy", "YellowToy", teacherreward, False)
    GetChoicesCRModels(RedToy, YellowToy, "Equal_Costs", 1,
                       "RedToy", "YellowToy", teacherreward, False)
    RedToy = Toy(buttons=1, activation=0, cost=1, reward=YellowToyR)
    YellowToy = Toy(buttons=6, activation=[
                    0, 1], cost=1, reward=YellowToyR)
    GetChoicesCRModels(RedToy, YellowToy, "Matched_Rewards",
                       0.5, "RedToy", "YellowToy", teacherreward, False)
    GetChoicesCRModels(RedToy, YellowToy, "Matched_Rewards",
                       1, "RedToy", "YellowToy", teacherreward, False)
    RedToy = Toy(buttons=1, activation=0, cost=1, reward=YellowToyR)
    YellowToy = Toy(buttons=6, activation=[0, 1], cost=1, reward=RedToyR)
    GetChoicesCRModels(RedToy, YellowToy, "Inverted_Rewards",
                       0.5, "RedToy", "YellowToy", teacherreward, False)
    GetChoicesCRModels(RedToy, YellowToy, "Inverted_Rewards",
                       1, "RedToy", "YellowToy", teacherreward, False)


# Run models exploring whether sensitivity to the teacher matters.
def GetChoicesTeacherModels(ToyA, ToyB, ConditionName, ExploreProb=1, ToyAName="Toy0", ToyBName="Toy1", teacherreward="Constant", header=True):
    """
    Get the utilities of all kinds of agents.
    teacherreward should be "Constant" or "Variable"
    header (bool): Add header to file?
    """
    # Create all kinds of agents and get their choices.
    # Parameters: Learner cost, learner reward, teacher cost, teacher reward, discover cost, discover reward
    # Four main models: Use/Ignore learner's costs. Use/Ignore learner's
    # rewards
    A_a = Agent([ToyA, ToyB], 1, 0, 1, 0, 1, 0, ExploreProb,
                [ToyAName, ToyBName], teacherreward).Teach()
    A_b = Agent([ToyA, ToyB], 1, 1, 1, 0, 1, 1, ExploreProb,
                [ToyAName, ToyBName], teacherreward).Teach()
    A_c = Agent([ToyA, ToyB], 0, 1, 0, 1, 0, 1, ExploreProb,
                [ToyAName, ToyBName], teacherreward).Teach()
    A_d = Agent([ToyA, ToyB], 1, 1, 0, 1, 1, 1, ExploreProb,
                [ToyAName, ToyBName], teacherreward).Teach()
    if header:
        sys.stdout.write("Condition,"+str(ToyAName)+"Reward,"+str(ToyBName) +
                         "Reward,LearnC,LearnR,TeachC,TeachR,DiscoverC,DiscoverR,ExploreProb,TeacherReward,Decision\n")
    sys.stdout.write(str(ConditionName)+","+str(ToyA.reward) + "," +
                     str(ToyB.reward) + ",1,0,1,0,1,0," + str(ExploreProb) + "," + str(teacherreward) + "," + str(A_a) + "\n")
    sys.stdout.write(str(ConditionName)+","+str(ToyA.reward) + "," +
                     str(ToyB.reward) + ",1,1,1,0,1,1," + str(ExploreProb) + "," + str(teacherreward) + "," + str(A_b) + "\n")
    sys.stdout.write(str(ConditionName)+","+str(ToyA.reward) + "," +
                     str(ToyB.reward) + ",1,1,0,1,1,1," + str(ExploreProb) + "," + str(teacherreward) + "," + str(A_c) + "\n")
    sys.stdout.write(str(ConditionName)+","+str(ToyA.reward) + "," +
                     str(ToyB.reward) + ",1,1,1,1,1,1," + str(ExploreProb) + "," + str(teacherreward) + "," + str(A_d) + "\n")


# Up to what value can the red toy's reward be?
RedToyRLimit = 50

# Run the main alternative models.
# Need to run model twice. One with constant teacher rewards and one with variable teacher rewards
teacherreward = "Constant"
YellowToyR = 5
ExploreProb = 0.5
# Run family of models on all four conditions
# Run each model twice, one with low exploration pobability and one with
# high probability.
for RedToyR in range(1, RedToyRLimit+1):
    RedToy = Toy(buttons=1, activation=0, cost=1, reward=RedToyR)
    YellowToy = Toy(buttons=6, activation=[
                    0, 1], cost=1, reward=YellowToyR)
    GetChoicesTeacherModels(RedToy, YellowToy, "Unequal_Costs", 0.5,
                       "RedToy", "YellowToy", teacherreward, False)
    GetChoicesTeacherModels(RedToy, YellowToy, "Unequal_Costs", 1,
                       "RedToy", "YellowToy", teacherreward, False)
    RedToy = Toy(buttons=1, activation=0, cost=1, reward=RedToyR)
    YellowToy = Toy(buttons=1, activation=0, cost=1, reward=YellowToyR)
    GetChoicesTeacherModels(RedToy, YellowToy, "Equal_Costs", 0.5,
                       "RedToy", "YellowToy", teacherreward, False)
    GetChoicesTeacherModels(RedToy, YellowToy, "Equal_Costs", 1,
                       "RedToy", "YellowToy", teacherreward, False)
    RedToy = Toy(buttons=1, activation=0, cost=1, reward=YellowToyR)
    YellowToy = Toy(buttons=6, activation=[
                    0, 1], cost=1, reward=YellowToyR)
    GetChoicesTeacherModels(RedToy, YellowToy, "Matched_Rewards",
                       0.5, "RedToy", "YellowToy", teacherreward, False)
    GetChoicesTeacherModels(RedToy, YellowToy, "Matched_Rewards",
                       1, "RedToy", "YellowToy", teacherreward, False)
    RedToy = Toy(buttons=1, activation=0, cost=1, reward=YellowToyR)
    YellowToy = Toy(buttons=6, activation=[0, 1], cost=1, reward=RedToyR)
    GetChoicesTeacherModels(RedToy, YellowToy, "Inverted_Rewards",
                       0.5, "RedToy", "YellowToy", teacherreward, False)
    GetChoicesTeacherModels(RedToy, YellowToy, "Inverted_Rewards",
                       1, "RedToy", "YellowToy", teacherreward, False)

# Need to run model twice. One with constant teacher rewards and one with variable teacher rewards
teacherreward = "Variable"
YellowToyR = 5
ExploreProb = 0.5
# Run family of models on all four conditions
# Run each model twice, one with low exploration pobability and one with
# high probability.
for RedToyR in range(1, RedToyRLimit+1):
    RedToy = Toy(buttons=1, activation=0, cost=1, reward=RedToyR)
    YellowToy = Toy(buttons=6, activation=[
                    0, 1], cost=1, reward=YellowToyR)
    GetChoicesTeacherModels(RedToy, YellowToy, "Unequal_Costs", 0.5,
                       "RedToy", "YellowToy", teacherreward, False)
    GetChoicesTeacherModels(RedToy, YellowToy, "Unequal_Costs", 1,
                       "RedToy", "YellowToy", teacherreward, False)
    RedToy = Toy(buttons=1, activation=0, cost=1, reward=RedToyR)
    YellowToy = Toy(buttons=1, activation=0, cost=1, reward=YellowToyR)
    GetChoicesTeacherModels(RedToy, YellowToy, "Equal_Costs", 0.5,
                       "RedToy", "YellowToy", teacherreward, False)
    GetChoicesTeacherModels(RedToy, YellowToy, "Equal_Costs", 1,
                       "RedToy", "YellowToy", teacherreward, False)
    RedToy = Toy(buttons=1, activation=0, cost=1, reward=YellowToyR)
    YellowToy = Toy(buttons=6, activation=[
                    0, 1], cost=1, reward=YellowToyR)
    GetChoicesTeacherModels(RedToy, YellowToy, "Matched_Rewards",
                       0.5, "RedToy", "YellowToy", teacherreward, False)
    GetChoicesTeacherModels(RedToy, YellowToy, "Matched_Rewards",
                       1, "RedToy", "YellowToy", teacherreward, False)
    RedToy = Toy(buttons=1, activation=0, cost=1, reward=YellowToyR)
    YellowToy = Toy(buttons=6, activation=[0, 1], cost=1, reward=RedToyR)
    GetChoicesTeacherModels(RedToy, YellowToy, "Inverted_Rewards",
                       0.5, "RedToy", "YellowToy", teacherreward, False)
    GetChoicesTeacherModels(RedToy, YellowToy, "Inverted_Rewards",
                       1, "RedToy", "YellowToy", teacherreward, False)
