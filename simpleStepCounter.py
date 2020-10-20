def simpleStepCounter(vet):
    lastRow = 0; counter = 0
    for count in vet:
        if count < lastRow:
            counter += lastRow
        lastRow = count
    counter += count
    return counter

