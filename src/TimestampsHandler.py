class TimeManager:
    
    @staticmethod
    def leapYear(year):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True
        else:
            return False
    @staticmethod
    def breakTimestamps(timestamps):
        return timestamps.split(" ")

    @staticmethod
    def dayToSecond(day):
        return day * 60 * 60 * 24

    @staticmethod
    def monthToSecond(month, year):
        seconds = 0
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if TimeManager.leapYear(year):
            months[1] = 29
        for i in range(0, len(months)):
            seconds += TimeManager.dayToSecond(months[i])
            if i == month:
                break
        return seconds

    @staticmethod
    def yearToSecond(year):
        seconds = 0.0
        for i in range(1, int(year)):
            if TimeManager.leapYear(i):
                seconds += TimeManager.dayToSecond(366)
            else:
                seconds += TimeManager.dayToSecond(365)
        return seconds

    @staticmethod
    def breakDate(date) :
        dateBroken = date.split("-")
        day = float(dateBroken[2]) - 1
        month = float(dateBroken[1]) - 1
        year = float(dateBroken[0])

        seconds = TimeManager.dayToSecond(day) + TimeManager.monthToSecond(month,year) + TimeManager.yearToSecond(year) 
        return seconds

    @staticmethod
    def breakTime(time) :
        timeBroken = time.split(":")
        seconds = float(timeBroken[2])
        minutesToSeconds = float(timeBroken[1]) * 60
        hoursToSeconds = float(timeBroken[0]) * 3600
        timeSeconds = seconds + minutesToSeconds + hoursToSeconds
        return timeSeconds

    @staticmethod
    def convertTimeToSeconds(time): 
        timestampsBroken = TimeManager.breakTimestamps(time)
        return TimeManager.breakDate(timestampsBroken[0]) + TimeManager.breakTime(timestampsBroken[1])

    
    def subtractTime(time1, time2):
        return TimeManager.convertTimeToSeconds(time2) - TimeManager.convertTimeToSeconds(time1)
