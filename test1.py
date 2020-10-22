
from src.StepCounterClass import StepCounter
import data.dataTest1 as dt1

stepCounter = StepCounter("data/data.csv")
# test1 method receives as parameter a data with list format
# and ideal result from a stepCounter method execution.
# Then it print a message for success and other for error.
def test1(data, idealResult):
    realResult = stepCounter.stepCounter(data)
    if realResult == idealResult:
        print("Test Ok!")
    else:
        print("Test Failed!")


test1(dt1.vet1, dt1.result1)
test1(dt1.vet2, dt1.result2)
test1(dt1.vet3, dt1.result3)
test1(dt1.vet4, dt1.result4)
test1(dt1.vet5, dt1.result5)

