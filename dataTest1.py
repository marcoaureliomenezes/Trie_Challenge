# Test 1: when the number of steps increases sequentially
vet1 = [0, 0, 0, 2, 4, 6, 8, 10]
result1 = 10

# Test 2: When there's a reset
vet2 = [0, 0, 1, 2, 0, 0, 1, 2]
result2 = 2 + 2

# Test 3: When there are two resets. The seconds reset is identified
# by the number of step on the previous instant measured is greater than
# the actual number of steps
vet3 = [5, 0, 1, 3, 5, 4]
result3 = 5 + 5 + 4

# Test 4: 
vet4 = [1, 2, 0, 0, 1, 0, 1, 2]
result4 = 2 + 1 + 2

# Problem of reset on stepCounter device side
# If in a vector of steps we analyze a sequential pair (v1, v2) 
# we have the following situations:
#   Situation 1: If v1 > v2 it means that a reset had occurred
#   Situation 2: If v1 <= v2 there's a problem, becaouse we 
#   don't know if a reset has occured
# Analyzing better situation 2 with an example:
# If we have the vector [0, 1, 1] there's there are 2 different  
# possibilities: 
#   Possibility 1: Any reset has been occurred. It means that the user
#   just has walked 1 step and stopped.
#   Possibility 2: a reset has occurred between t2 and t3 and after this
#   reset the user walked more 1 step.
#   Error!!! In this case the user walked 2 step, not 1 step 

# Soluctions: 
#   Soluction 1: The step counter device must save the reset instant and
#   when send [resetInstant, 0] and after that [actualInstant, stepNumber]
#   Soluction 2: The absolute number of steps (disregarding resets) must be
#   calculated on the device side.
vet5 = [0, 1, 1, 1]
result5 = 1
