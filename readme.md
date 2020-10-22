# Trie Challenge

#    Project structure
#       Data folder: Contains data.csv and folders data1 and data2,
#       data.csv: contains data.csv (file sent by Trie company)
#       data1 folder: contains csv files to test the first assignment
#       data2 folder: contains csv files to test the second assignment

#       src folder: Contains StepCounterClass and TimeStampsHandler

#           StepCounter class contains the methods to calculate total of
#           steps of a CSV file (assigment 1) and to compute total of walking
#           and time spent walking from a CSV file and load these values inside
#           private attributes of the class.

#           TimeStampsHandler class contains static methods to handle with data
#           and the timestamps format received from CSV files. The main purpose
#           for this class is convert timestamps with format 
#           2020-03-01 22:44:00.047143516 to a float number that represents the
#           same timesstamps in seconds

#       testCSV1.py: Where is written a method to test the first assignment.
#       One object from StepCounter class is instantiated with the csv file
#       for test being passed as parameter, the result of StepCounterCSV is
#       compared with a ideal result.

#       testCSV2.py: Where is written a method to test the second assignment.
#       One object from StepCounter class is instantiated with the csv file
#       for test being passed as parameter, the result of ComputeWalkingCSV is
#       compared with a ideal result.


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

