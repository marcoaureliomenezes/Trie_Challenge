from src.StepCounter import StepCounter

def test(testNumber, csvUrl, idealValue):
    stepCounter = StepCounter(csvUrl)
    computedSteps = stepCounter.stepCounterCSV()
    if computedSteps == idealValue:
        print("Test", testNumber, "Ok! Result:", computedSteps)
    else:
        print("Test", testNumber, "Failed! Expected Result:", idealValue, ", Computed Result:", computedSteps)


result1 = 300
test(1, "data/data1/data-test1.csv", result1)

result2 = 150
test(2, "data/data1/data-test2.csv", result2)

result3 = 200 + 200 + 500 + 2600
test(3, "data/data1/data-test3.csv", result3)

result4 = 10 * 10
test(4, "data/data1/data-test4.csv", result4)

result5 = 100 + 70 + 50 + 30 + 20 + 10
test(5, "data/data1/data-test5.csv", result5)

result6 = 300 + 400 + 1000 + 200 + 100
test(1, "data/data1/data-test6.csv", result6)

