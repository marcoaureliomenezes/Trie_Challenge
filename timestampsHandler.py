def leapYear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def breakTimestamps(timestamps):
    return timestamps.split(" ")


def dayToSecond(day):
    return day * 60 * 60 * 24

def monthToSecond(month, year):
    seconds = 0
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leapYear(year):
        months[1] = 29
    for i in range(0, len(months)):
        seconds += dayToSecond(months[i])
        if i == month:
            break
    return seconds

def yearToSecond(year):
    seconds = 0.0
    for i in range(1, int(year)):
        if leapYear(i):
            seconds += dayToSecond(366)
        else:
            seconds += dayToSecond(365)
    return seconds



def breakDate(date) :
    dateBroken = date.split("-")
    day = float(dateBroken[2]) - 1
    month = float(dateBroken[1]) - 1
    year = float(dateBroken[0])

    seconds = dayToSecond(day) + monthToSecond(month,year) + yearToSecond(year) 
    return seconds

def breakTime(time) :
    timeBroken = time.split(":")
    seconds = float(timeBroken[2])
    minutesToSeconds = float(timeBroken[1]) * 60
    hoursToSeconds = float(timeBroken[0]) * 3600
    timeSeconds = seconds + minutesToSeconds + hoursToSeconds
    return timeSeconds


def convertTimeToSeconds(time): 
    timestampsBroken = breakTimestamps(time)
    return breakDate(timestampsBroken[0]) + breakTime(timestampsBroken[1])

def subtractTime(time1, time2):
    return convertTimeToSeconds(time2) - convertTimeToSeconds(time1)
