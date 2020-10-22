from src.TimestampsHandler import TimeManager
example1 = "2020-03-01 22:44:00.047143516"
example2 = "2020-03-01 22:44:01.047143516"

example3 = "2020-02-28 22:45:01.047143516"
example4 = "2020-02-28 22:46:01.047143516"

example5 = "2020-03-01 22:44:00.047143516"
example6 = "2020-03-01 23:44:00.047143516"

example7 = "2020-03-01 22:44:00.047143516"
example8 = "2020-03-02 22:44:00.047143516"


example9 = "2020-01-01 07:25:41.047143516"
example10 = "2020-02-01 07:25:41.047143516"

example11 = "2020-04-01 07:25:41.047143516"
example12 = "2020-05-01 07:25:41.047143516"


print(TimeManager.subtractTime(example1, example2))
print(TimeManager.subtractTime(example3, example4))
print(TimeManager.subtractTime(example5, example6))
print(TimeManager.subtractTime(example7, example8))
print(TimeManager.subtractTime(example9, example10))
print(TimeManager.subtractTime(example11, example12))