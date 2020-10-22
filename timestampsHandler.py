example1 = "2020-03-01 00:00:00.047143516"
example2 = "2020-02-28 23:59:59.047143525"
timePattern = [60, 60, 1]

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
print(monthToSecond(3, 2020))
print(monthToSecond(2, 2020))

def breakDate(date) :
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dateBroken = date.split("-")
    
    day = float(dateBroken[2]) - 1
    month = float(dateBroken[1]) - 1
    year = float(dateBroken[0])
    
    dayToSeconds = day * 60 * 60 * 24
    counter = 0
    monthDays = 0
    for i in months:
        monthDays += i
        if(counter == month):
            break
        counter += 1
        if leapYear(year):
            pass
    monthToSeconds = float(month) * (60 * 60 * 24 * months[month])
    yearToSeconds = float(dateBroken[0] - 1970) * (60 * 60 * 24)
    timeSeconds = dayToSeconds + monthToSeconds + yearToSeconds
    return timeSeconds

def breakTime(time) :
    timeBroken = time.split(":")
    seconds = float(timeBroken[2])
    minutesToSeconds = float(timeBroken[1]) * 60
    hoursToSeconds = float(timeBroken[0]) * 60
    timeSeconds = seconds + minutesToSeconds + hoursToSeconds
    return timeSeconds


def convertTimeToSeconds(time): 
    timestampsBroken = breakTimestamps(time)
    print(timestampsBroken)
    date = breakDate(timestampsBroken[0])
    print(date)
    time = breakTime(timestampsBroken[1])
    print(time)

    # timeInSeconds = float(time[2]) * 1 + float(time[1]) * 60 + float(time[0]) * 3600
    # return timeInSeconds

def subtractTime(time1, time2):
    return convertTimeToSeconds(time2) - convertTimeToSeconds(time1)



# print(convertTimeToSeconds(example1))
# print(convertTimeToSeconds(example2))
# ano: 1000000000 * 60 * 60 * 24