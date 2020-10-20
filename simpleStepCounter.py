import numpy as np

vet = [1, 2, 3, 10, 0, 1, 7, 10, 20, 10, 0, 40, 20, 3, 0, 10, 1000];

def simpleStepCounter(vet):
    lastRow = 0; counter = 0
    for count in vet:
        if count < lastRow:
            counter += lastRow
        lastRow = count
    counter += count
    return counter

