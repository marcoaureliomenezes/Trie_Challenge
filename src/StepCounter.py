import pandas as pd

class StepCounter:
    		
	# Constructor loading a csvFile passed as parameter
	# and printing a message that this data were loaded in a 
	# variable called _self 
	def __init__(self, csvFile):
		self.df = pd.read_csv(csvFile, sep= ',', parse_dates=['timestamp'])
		self.walkingQuantity = 0
		self.walkingTime = 0	

	# _stepCounter method receives as parameter a vector of numbers
	# and return total of steps, considering that there may be resets
	# This method is private because it's only used inside the class
	# and so, it can be encapsulated
	def stepCounterImperative(self, vet):
		stack = [0]
		for count in vet:
			if count >= stack[len(stack) -1]:
				stack.pop()
			stack.append(count)
		return np.sum(stack)


	
	# stepCounterCSV method uses the _file attribute, loaded
	# when the constructor was called and return total of steps
	# of that dataset 
	def stepCounterImperative(self):
		stack = [-1]
		for index, row in self._file.iterrows():
			if row[1] >= stack[len(stack) -1]:
				stack.pop()
			stack.append(row[1])
		return np.sum(stack)

	
	def stepCounterDeclarative(self):
		self.df["resetEvents"] = self.df['count'].diff() < 0
		resetEvents = self.df[self.df['count'].diff() < 0]
		totalSteps = (self.df.iloc[resetEvents.index - 1]).sum()
		return totalSteps["count"]



	def computeWalkingImperative(self, stepGoal=120, timeGoal=1):
		monitoredDataList = []; stepNumberList = [];
		walkingQuantity = 0; walkingTime = 0
		for index, row in self._file.iterrows():
			print(row[0])
	


	