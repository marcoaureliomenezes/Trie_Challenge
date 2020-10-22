import pandas as pd
import numpy as np

class StepCounter:
    	
	
	# Constructor loading a csvFile passed as parameter
	# and printing a message that this data were loaded in a 
	# variable called _self 
	def __init__(self, csvFile):
		self._file = pd.read_csv(csvFile)
		self.walkingQuantity = 0
		self.walkingTime = 0	

	# _stepVel method receives as parameter 2 vectors of format
	# [time, step_number] and returns a step velocity with unit
	# step/second. This method is private because it's only used
	# inside the class and so, it can be encapsulated 
	def _stepVel(self, vet1, vet2):
		deltaStep = vet2[0] - vet1[0]
		deltaTime = vet2[1] - vet1[1]
		return deltaStep / deltaTime

	# _stepCounter method receives as parameter a vector of numbers
	# and return total of steps, considering that there may be resets
	# This method is private because it's only used inside the class
	# and so, it can be encapsulated
	def stepCounter(self, vet):
		sta = []
		stack = [0]
		for count in vet:
			if count >= stack[len(stack) -1]:
				stack.pop()
			stack.append(count)
		return np.sum(stack)
	
	# stepCounterCSV method uses the _file attribute, loaded
	# when the constructor was called and return total of steps
	# of that dataset 
	def stepCounterCSV(self):
		stack = [-1]
		for index, row in self._file.iterrows():
			if row[1] >= stack[len(stack) -1]:
				stack.pop()	
			stack.append(row[1])
		return np.sum(stack)

	# validatedWaking method for a speed receives as parameters
	# data set and also the stepGoal and timeGoal. These 2 last
	# parameters determine the average velocity in a time interval
	# that's accepted as a valid walking. The default specification
	# is 120 steps in 1 minute
	# The method return a vector with the walking number in the first
	# position and walking time in the second one

	# validatedWalking method using a dictionary..
	# as we run through the data 
	# a element with key = actual instant and value = absolute step number
	# (instantGoal: stepNumber)
	# a cada instante nos vemos se chegou no 
	#   and we can the method stores for each
	# instant, the goal instant (60 second after the actual instant)
	# and the actual number of steps (absolut steps).
		# Running through this dict, if the actual instant greater than
		#  

	def computeWalking(self, stepGoal=120, timeGoal=1):
		monitoredDataList = []; stepNumberList = [];
		walkingQuantity = 0; walkingTime = 0
		for index, row in self._file.iterrows():
			instant = row[0]
			stepNumberList.append(row[1])
			stepNumber = self.stepCounter(stepNumberList)
			monitoredDataList.append([instant + (60 * timeGoal), stepNumber])
			for monitoredData in monitoredDataList:
				if instant >= monitoredData[0]:
					if (int(stepNumber) - monitoredData[1]) >= stepGoal :
						walkingQuantity += 1
						walkingTime += 1
						monitoredDataList = []
						break
		print(walkingQuantity, walkingTime)
		return [walkingQuantity, walkingTime]

	def validatedWalking1(self, data, stepGoal=120, timeGoal=1):
		monitoredDataList = []; stepNumberList = [];
		walkingQuantity = 0; walkingTime = 0
		for it in data:
			instant = it[0]
			stepNumberList.append(it[1])
			stepNumber = self.stepCounter(stepNumberList)
			monitoredDataList.append([instant + (60 * timeGoal), stepNumber])
			for monitoredData in monitoredDataList:
				if instant >= monitoredData[0]:
					if (int(stepNumber) - monitoredData[1]) >= stepGoal :
						walkingQuantity += 1
						walkingTime += 1
						monitoredDataList = []
						break
		print(walkingQuantity, walkingTime)
		return [walkingQuantity, walkingTime]
	def validatedWalking2(self, data, stepGoal=120, timeGoal=1):
		walkingQuantity = 0 ; walkingTime = 0
		monitoredDataList = {}
		stepNumberList = []; ajudaHacker=[0,0];
		for it in data:
			instant = it[0]
			stepNumberList.append(it[1])
			stepNumber = self.stepCounter(stepNumberList)
			instantGoal = instant + (60 * timeGoal)
			monitoredDataList[instantGoal] = stepNumber
			for it2 in monitoredDataList:
				if int(stepNumber) - monitoredDataList[it2] >= stepGoal :
					walkingTime += 1
					walkingQuantity += 1
					monitoredDataList = {}
					break
		print(walkingQuantity, walkingTime)
		return [walkingQuantity, walkingTime]
