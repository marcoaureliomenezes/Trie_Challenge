# Trie Challenge

#    Project structure
#       Data folder: Contains the CSV file and datasets for the assignment 1
#       (dataTest1.py) and 2 (dataTest2.py).

#       src folder: Contains the file with the class StepCounter, where
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
#       This problem is explained in dataTest1.py file at the line 19.
#       A simple way to solve the problem is showed as option to solve
#       the problem