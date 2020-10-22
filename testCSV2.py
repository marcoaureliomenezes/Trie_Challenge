from src.StepCounter import StepCounter

def test(testNumber, csvUrl, idealValue):
    obj = StepCounter(csvUrl)
    obj.computeWalkingCSV()
    print([obj.walkingTime, obj.walkingQuantity])
    # if computedSteps == idealValue:
    #     print("Test", testNumber, "Ok! Result:", computedSteps)
    # else:
    #     print("Test", testNumber, "Failed! Expected Result:", idealValue, ", Computed Result:", computedSteps)

result1 = [0, 0]
test(1, 'data/data2/data-test1.csv', result1)

# result2 = [0, 0]
# test(2, 'data/data2/data-test1', result2)

# result3 = [0, 0]
# test(3, 'data/data2/data-test1', result3)

# result4 = [0, 0]
# test(4, 'data/data2/data-test1', result4)

# result5 = [0, 0]
# test(5, 'data/data2/data-test1', result5)

# result6 = [0, 0]
# test(6, 'data/data2/data-test1', result6)

# result7 = [0, 0]
# test(7, 'data/data2/data-test1', result7)

# result8 = [0, 0]
# test(8, 'data/data2/data-test1', result8)

# result9 = [0, 0]
# test(9, 'data/data2/data-test1', result9)

# result10 = [0, 0]
# test(10, 'data/data2/data-test1', result10)
