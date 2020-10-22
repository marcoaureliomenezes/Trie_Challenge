import data.dataTest2 as dt2
from src.StepCounterClass import StepCounter

stepCounter = StepCounter('data/data-test1.csv')
stepCounter.computeWalking()

stepCounter = StepCounter('data/data-test2.csv')
stepCounter.computeWalking()

stepCounter = StepCounter('data/data-test3.csv')
stepCounter.computeWalking()

def test2(data, idealResult):
    realResult = stepCounter.validatedWalking1(data)
    realResult2 = stepCounter.validatedWalking2(data)
    if(realResult == idealResult):
        print("Test with list Ok!")
    else:
        print("Test with list Failed")
    if(realResult2 == idealResult):
        print("Test with dictionary Ok!")
    else:
        print("Test with dictionary Failed")



