example1 = "2020-01-01 01:00:01.047143516"
example2 = "2020-01-01 02:00:01.047143525"
timePattern = [60, 60, 1]

def breakDateTime(timestamps):
    instant = timestamps.split(" ")
    date = instant[0]
    time = instant[1]
    return [date, time]

def breakTime(time) :
    dads = time.split(":")
    return dads

def convertTimeToSeconds(time): 
    dateTime = breakDateTime(time)
    time = breakTime(dateTime[1])
    timeInSeconds = float(time[2]) * 1 + float(time[1]) * 60 + float(time[0]) * 3600
    return timeInSeconds

def subtractTime(time1, time2):
    return convertTimeToSeconds(time2) - convertTimeToSeconds(time1)



print(convertTimeToSeconds(example1))
print(convertTimeToSeconds(example2))
print(convertTimeToSeconds(example2) - convertTimeToSeconds(example1))
# ano: 1000000000 * 60 * 60 * 24