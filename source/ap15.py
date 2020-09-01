
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

pd.set_option('display.max_columns', None)

sb.set_style('darkgrid')

full_data = pd.read_csv(r'/home/gopi/Python_202004/data/corona/ourworldindata/full_data_20200824.csv')
print(full_data.head())
print(full_data.tail())

# The row numbers in pandas is also known as the 'index'
# Here we are setting the index to be the dates instead of the 
# row numbers
full_data.set_index(pd.to_datetime(full_data.date, format='%Y-%m-%d'),
                    inplace=True)
print(full_data.tail())

# Here we are adding a new column death_rate by defining
# each row: the following process of defining all the rows
# in a single statement is called vectorization
full_data.loc[:,'death_rate'] = (full_data.total_deaths / 
                                 full_data.total_cases)
print(full_data.tail())

plt.figure()
full_data.death_rate.plot(title='Death rate of corona')

US = full_data.loc[full_data.location == 'United States',:]
print(US.tail())

plt.figure()
US.death_rate.plot(title='Death rate of corona for the US')

