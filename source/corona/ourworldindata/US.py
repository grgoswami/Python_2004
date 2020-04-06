
import pandas as pd
import seaborn 

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 5000)

seaborn.set_style('darkgrid')

"""
https://ourworldindata.org/coronavirus-source-data
"""

full_data = pd.read_csv(r'/home/gopi/Python_202004/data/corona/ourworldindata/full_data.csv')
print(full_data.head())
print(full_data.describe())
print(full_data.location.value_counts())
print(full_data.shape)

US = full_data.loc[full_data.location == 'United States',:]
print(US.shape)
US.loc[:,'date'] = pd.to_datetime(US.date, format='%Y-%m-%d')
US.set_index('date', inplace=True)
US[['new_cases', 'new_deaths']].plot()
US[['total_cases', 'total_deaths']].plot()
US[['new_deaths', 'total_deaths']].plot()

US.tail()

