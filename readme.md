# Trie Challenge

#    Project structure
#       Data folder: Contains the CSV file and datasets for the assignment 1
#       (dataTest1.py) and 2 (dataTest2.py).

#       src folder: Contains StepCounterClass and TimeStampsHandler

#       Contains the file with the class StepCounter, where
#       all methods about the step counter are implemented.

#       test1.py file: file that imports dataTest1 dataset and
#       StepCounter class and executes tests of stepCounter method.
#       StepCounter method is used to compute the absolute number of
#       steps even whether resets are made.

#       test2.py: file that imports dataTest2 dataset and
#       StepCounter class and executes tests of validatedWalking method.
#       validatedWalking method is used to compute the number of
#       walkings made and time spent with these walkings. 

#       testCSV1.py: file that imports data.csv dataset and
#       StepCounter class and executes stepCounter method on it to
#       find the absolute number of steps in data.csv.

#       testCSV2.py: file that imports data.csv dataset and
#       StepCounter class and executes stepCounter method on it to
#       find the absolute number of steps in data.csv.

#       There's a interesting problem with the way we receive data that
#       can generate data inconsistency.

#       Problem of reset on stepCounter device side
#       If in a vector of steps we analyze a sequential pair (v1, v2) 
#       we have the following situations:
#       Situation 1: If v1 > v2 it means that a reset had occurred
#       Situation 2: If v1 <= v2 there's a problem, becaouse we 
#           don't know if a reset has occured

#       Analyzing better situation 2 with an example:
#       If we have the vector [0, 1, 1] there's there are 2 different  
#       possibilities: 
#           Possibility 1: Any reset has been occurred. It means that the user
#               just has walked 1 step and stopped.
#           Possibility 2: a reset has occurred between t2 and t3 and after this
#               reset the user walked more 1 step.
#               Error!!! In this case the user walked 2 step, not 1 step 

#       Soluctions: 
#           Soluction 1: The step counter device must save the reset instant and
#               when send [resetInstant, 0] and after that [actualInstant, 
#               stepNumber]
#       Soluction 2: The absolute number of steps (disregarding resets) must be
#           calculated on the device side.

