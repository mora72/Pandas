# Render our plots inline
# %matplotlib inline

import pandas as pd
import matplotlib.pyplot as plt

# pd.set_option('display.mpl_style', 'default')  # Make the graphs a bit prettier
plt.rcParams['figure.figsize'] = (15, 5)

df = pd.read_csv('./csv/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')

# Look at the first 3 rows
print(df[:5])
print(df.columns)
print(df['Berri 1'])
print(df['C?te-Sainte-Catherine'])
print(df.describe()['Berri 1'])
print(df.describe()['C?te-Sainte-Catherine'])

# Selecting a column
# print(df['Berri 1'])
print(df['Berri 1'].plot())
df['Berri 1'].plot()  # plota gráfico desta coluna. só funcionou no python console
df.plot(figsize=(15, 10))  # plota gráfico com todas as coluna. só funcionou no python console

