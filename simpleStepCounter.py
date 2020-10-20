def simpleStepCounter(vet):
    lastRow = 0; counter = 0
    for count in vet:
        if count < lastRow:
            counter += lastRow
        lastRow = count
    counter += count
    return counter

def simpleStepCounterCSV(loadedData):
    lastRow = 0; counter = 0
    for index, row in loadedData.iterrows():
        if row[1] < lastRow:
            counter += lastRow
        lastRow = row[1]
    counter += row[1]
    return counter
