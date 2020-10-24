import pandas as pd
from datetime import datetime

data = pd.read_csv('data.csv', sep= ',', parse_dates=['timestamp'])

# This line filters data taking out repeated numbers if the a 2 times
# consecutives.
df = data.loc[data["count"].diff(2) != 0]


# This block generates the absolute step counter (step number is
# never reset) through the following steps

# a column with difference between the element and its previous one.
# It returns the negative numbers that stores how many steps we had
# before the reset
df["diff"] = df["count"].diff()
# To get only the step number at the reset moment we filter the
# diff column to contain just zero on all steps besides the reset moments 
df["reset_event"] = df["diff"].apply(lambda x : x if x < 0 else 0)
# With this step we creates a column with the reset time step numbers
df["reset_steps_accumulator"] = df["reset_event"].cumsum() * (-1)

# The table absoluteSteps is made through the the sum of the
# count column and reset_steps_accumulator
df["absoluteSteps"] = df["reset_steps_accumulator"] + df["count"]