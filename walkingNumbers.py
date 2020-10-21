import simpleStepCounter as ssc

def stepVel(vet1, vet2):
        deltaStep = vet2[1] - vet1[1]
        deltaTime = vet2[0] - vet1[0]
        return deltaStep / deltaTime

def validatedWalking(data) :
        stack = []
        trainStack = [0]
        walkingQuantity = 0; 
        walkingTime = 0
        for it in data:
                instant = it[0]
                trainStack.append(it[1])
                stepNumber = ssc.simpleStepCounter(trainStack)
                stack.append([instant + 60, stepNumber])
                for dadoGuardado in stack:
                        if instant >= dadoGuardado[0]:
                                if (stepNumber - dadoGuardado[1]) >=120 :
                                        walkingQuantity += 1
                                        walkingTime += 1
                                        stack = []
        return [walkingQuantity, walkingTime]