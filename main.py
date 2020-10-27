import pandas as pd
import numpy as np
from datetime import datetime

df = pd.read_csv('data.csv', sep= ',', parse_dates=['timestamp'])



print("Total de NaN na coluna timestamp:", df["timestamp"].isnull().sum())
print("Total de NaN na coluna count:", df["count"].isnull().sum())
# ************************** tarefa 1 ****************************************
print("Descrição do periodo de tempo")
print(df["timestamp"].describe())




df["delta count"] = df["count"].diff() 
df["reset event"] = df["delta count"].apply(lambda x : -x if x < 0 else 0)
df["reset_step_accumulator"] = df["reset event"].cumsum()
df["absolute_steps"] = df["reset_step_accumulator"] + df["count"]


print("Descrição dos passos")
print(df["absolute_steps"].describe())


print("Transformações para anular reset e encontrar numero de passos absolutos")
print(df.loc[:,['count', 'delta count', 'reset event', 'reset_step_accumulator',
'absolute_steps']])


total_steps = df["absolute_steps"].max()
print("\nTotal de passos com método 1: ", total_steps)

# ***************************** Tarefa 2 ***************************************


df["timeSeconds"] = (df["timestamp"] - df["timestamp"].loc[0]).dt.total_seconds()
print("passou por 1")

df["timeBefore10"] = df["timeSeconds"].apply(lambda x: x - 600 if x > 600 else 0)

def nearestValue(value):

    absolute_value = np.abs(df["timeSeconds"] - value)
    smallest_difference_index = absolute_value.argmin()
    closest_element = df["timeSeconds"][smallest_difference_index]
    return closest_element

df["observed_time"] = df["timeSeconds"].apply(lambda x: nearestValue(x-600))

def timeToStep(x):
    return df["absolute_steps"][df["timeSeconds"] == x].max()

df["observed_steps"] = df["observed_time"].apply(lambda x: timeToStep(x))

df["oneWalking"] = df["absolute_steps"] - df["observed_steps"] >= 1200

df["edge_mask"] = df["oneWalking"].diff()

df["stop_walking2"] = df["oneWalking"] & df["edge_mask"]

print(df.loc[:, ["timeSeconds", "observed_time", "absolute_steps", "observed_steps", "oneWalking", "edge_mask", "stop_walking2"]])

walkingNumber = (df["stop_walking2"].value_counts())
print("Numero de caminhadas:", walkingNumber)
