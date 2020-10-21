import pandas as pd
import numpy as np

def stepCounter(vet):
    stack = [0] 
    for count in vet:
        if count >= stack[len(stack) -1]:
            stack.pop()
        stack.append(count)
    return np.sum(stack)

def stepCounterCSV(file):
    stack = [0] 
    for index, row in file.iterrows():
        if row[1] >= stack[len(stack) -1]:
            stack.pop()
        stack.append(row[1])
    return np.sum(stack)