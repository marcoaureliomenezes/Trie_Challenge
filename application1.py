import pandas as pd
import stepCounter as sc

file = pd.read_csv('data.csv')

print(sc.stepCounterCSV(file))
