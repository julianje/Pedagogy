SampleCost = function(){
  HypothesisList = c("Correct",rep("Incorrect",choose(7,2)-1))
  TestingOrder = sample(HypothesisList)
  NumberOfHypothesisTested = which(TestingOrder=="Correct")
  TotalCost = NumberOfHypothesisTested*2
  return(TotalCost+7)
}
Simulations = replicate(100000,SampleCost())
mean(Simulations)
