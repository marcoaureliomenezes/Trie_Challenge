import dataTest1 as dt1

from StepCounterClass import StepCounter

stepCounter = StepCounter('data.csv')

stepCounter.test1(dt1.vet1, dt1.result1)
stepCounter.test1(dt1.vet2, dt1.result2)
stepCounter.test1(dt1.vet3, dt1.result3)
stepCounter.test1(dt1.vet4, dt1.result4)
stepCounter.test1(dt1.vet5, dt1.result5)

