import pandas as pd
import numpy as np


df = pd.read_csv('data-test2.csv', sep= ',', parse_dates=['timestamp'])



# ************************** tarefa 1 ****************************************

df["delta count"] = df["count"].diff() 
df["reset event"] = df["delta count"].apply(lambda x : -x if x < 0 else 0)
df["reset_step_accumulator"] = df["reset event"].cumsum()
df["absolute_steps"] = df["reset_step_accumulator"] + df["count"]


# print("Passos para anular o valor do reset e encontrar o numero de passos absolutos")
# print(df.loc[:,['count', 'delta count', 'reset event', 'reset_step_accumulator',
# 'absolute_steps']])

total_steps = df["absolute_steps"].max()
total_steps2 = df["absolute_steps"].loc[df["absolute_steps"].size - 1]

print("\nTotal de passos com método 1", total_steps)
print("Total de passos com método 2", total_steps2)


# ***************************** Tarefa 2 ***************************************


df["timeSeconds"] = (df["timestamp"] - df["timestamp"].loc[0]).dt.total_seconds()
df["velocity"] = df["absolute_steps"].diff() / (df["timeSeconds"].diff())

def nearestValue(value):
    absolute_value = np.abs(df["timeSeconds"] - value)
    smallest_difference_index = absolute_value.argmin()
    closest_element = df["timeSeconds"][smallest_difference_index]
    return closest_element

df["timeBefore10"] = df["timeSeconds"].apply(lambda x: x - 600 if x > 600 else 0)
df["wished_value"] = df["timeSeconds"].apply(lambda x: nearestValue(x-600))


df["wishedSteps"] = df["absolute_steps"]

print(df.loc[:, ["timeSeconds", "timeBefore10", "wished_value", "absolute_steps",
"wishedSteps"]])

