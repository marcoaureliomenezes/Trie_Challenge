import pandas as pd

class StepCounter:
    		
	# Constructor
	def __init__(self, csvFile):
		self.df = pd.read_csv(csvFile, sep= ',', parse_dates=['timestamp'])
		self.walkingQuantity = 0
		self.walkingTime = 0	


	# Filter: This method filters by eliminating rows where
	# count[i] - count[i - 1] == 0. So, it eliminates consecutive
	# repeted values
	def filterData(self):
		data = self.df.loc[self.df["count"].diff() != 0]
		return data

 

	#	stepCounter method agregates the reset event in form of
	#	booleans
	def stepCounter(self):
		self.filterData()
		resetEvents = self.df[self.df['count'].diff() < 0]
		totalSteps = (self.df.iloc[resetEvents.index - 1]).sum()
		return totalSteps["count"]

	def absoluteSteps(self):
		


	def computeWalkingImperative(self, stepGoal=120, timeGoal=1):
		monitoredDataList = []; stepNumberList = [];
		walkingQuantity = 0; walkingTime = 0
		for index, row in self._file.iterrows():
			pas
	


	