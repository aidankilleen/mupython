# pandas_csv_import.py
# By: Aidan
# Date: 17/6/2022

import pandas as pd


df = pd.read_csv("https://professional.ie/PandasQ1Sales.csv")








print(df.head())


print(df.describe())

print(df.columns)

print(type(df.columns))

print(df.columns.values)
print(type(df.columns.values))




subset = df.iloc[:, [2,4]]

print(subset.groupby(by=['Sales Person']).sum())


pv = df.pivot(index='Country', columns='Sales Person', values='Total')

print(pv)


print("====================================")


c = df.columns[5]

print (c)
print(type(c))
print(df.columns.values)


for row in len(df.iloc):
    print(df.iloc[row])




