import dataTest2 as dt2
import walkingNumbers as wn

def test(data, idealResult):
    realResult = wn.validatedWalking(data)
    if(realResult == idealResult):
        print("Test Ok!")
    else:
        print("Test Failed")

test(dt2.data1, dt2.result1)
test(dt2.data2, dt2.result2)
test(dt2.data3, dt2.result3)
test(dt2.data4, dt2.result4)
test(dt2.data5, dt2.result5)
test(dt2.data6, dt2.result6)
test(dt2.data7, dt2.result7)
test(dt2.data8, dt2.result8)
test(dt2.data9, dt2.result9)
