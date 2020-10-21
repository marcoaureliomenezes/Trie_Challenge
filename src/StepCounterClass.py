import pandas as pd
import numpy as np

class StepCounter:
	# Constructor loading a csvFile passed as parameter
	# and printing a message that this data were loaded in a 
	# variable called _self 
	def __init__(self, csvFile):
		self._file = pd.read_csv(csvFile)
		print("Instance created and CSV data loaded to a Pandas structure")	

	# _stepVel method receives as parameter 2 vectors of format
	# [time, step_number] and returns a step velocity with unit
	# step/second. This method is private because it's only used
	# inside the class and so, it can be encapsulated 
	def _stepVel(self, vet1, vet2):
		deltaStep = vet2[1] - vet1[1]
		deltaTime = vet2[0] - vet1[0]
		return deltaStep / deltaTime

	# _stepCounter method receives as parameter a vector of numbers
	# and return total of steps, considering that there may be resets
	# This method is private because it's only used inside the class
	# and so, it can be encapsulated
	def _stepCounter(self, vet):
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
		stack = [0]
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
	def validatedWalking(self, data, stepGoal=120, timeGoal=1):
		stack = []; trainStack = []; walkingQuantity = 0; walkingTime = 0
		for it in data:
			instant = it[0]
			trainStack.append(it[1])
			stepNumber = self._stepCounter(trainStack)
			stack.append([instant + (60 * timeGoal), stepNumber])
			for dadoGuardado in stack:
				if instant >= dadoGuardado[0]:
					if (stepNumber - dadoGuardado[1]) >=stepGoal :
						walkingQuantity += 1
						walkingTime += 1
						stack = []
		return [walkingQuantity, walkingTime]
	
	# test1 method receives as parameter a data with list format
	# and ideal result from a stepCounter method execution.
	# Then it print a message for success and other for error.
	def test1(self, data, idealResult):
		realResult = self._stepCounter(data)
		if realResult == idealResult:
			print("Test Ok!")
		else:
			print("Test Failed!")
	
	def test2(self, data, idealResult):
		realResult = self.validatedWalking(data)
		if(realResult == idealResult):
			print("Test Ok!")
		else:
			print("Test Failed")