import stepCounter as sc
import dataTest1 as dt1

def test(data, idealResult):
    realResult = sc.stepCounter(data)
    if realResult == idealResult:
        print("teste Ok!")
    else:
        print("teste Failed!")

test(dt1.vet1, dt1.result1)
test(dt1.vet2, dt1.result2)
test(dt1.vet3, dt1.result3)
test(dt1.vet4, dt1.result4)
test(dt1.vet5, dt1.result5)

