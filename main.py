import pandas as pd
from datetime import datetime

data = pd.read_csv('data-test4.csv', sep= ',', parse_dates=['timestamp'])

# This line filters data taking out repeated numbers if the a 2 times
# consecutives.
df = data.loc[data["count"].diff(2) != 0]


# This block generates the absolute step counter (step number is
# never reset) through the following steps
# a column with difference between the element and its previous one.
# It returns the negative numbers that stores how many steps we had
# before the reset
def absoluteSteps():
    delta_count = df["count"].diff() 
    reset_event = delta_count.apply(lambda x : x if x < 0 else 0)
    reset_step_accumulator = reset_event.cumsum() * (-1)
    absolute_steps = reset_step_accumulator + df["count"]
    return absolute_steps

def totalSteps():
    return absoluteSteps().max()

def timestampToSeconds():
    timeSeconds = (df["timestamp"] - df["timestamp"].loc[0]).dt.total_seconds()
    return timeSeconds
stepNumber = totalSteps()

df["timestamp"] = timestampToSeconds()
df["Absolute steps"] = absoluteSteps()
df["velocity"] = df["count"].diff() / (df["timestamp"].diff())

# next block

print(df)