
import pandas as pd

tab = pd.DataFrame({'first_name': ['John', 'Jane', 'John'],
                    'last_name': ['Doe', 'Doe', 'Smith'],
                    'age': [9, 10, 11]})
print(tab)

# tab has two three columns: first_name, last_name, age
# tab has two rows: 0 and 1

# tab.last_name is a series
print(tab.last_name) 
print(type(tab.last_name)) 

# Choose the whole column
print(tab.age)
print(tab['age'])

# Choose the whole row
print(tab.loc[0,:])
print(tab.loc[1,:])

# Choose one cell
print(tab.loc[0,'last_name'])
print(tab.loc[1,'last_name'])

print(tab.loc[1,'age'])

print(tab.loc[tab.first_name == 'Jane','age'])

print(tab.loc[tab.first_name == 'John','age'])

print(tab.loc[(tab.first_name == 'John') &
              (tab.last_name == 'Doe'),'age'])

print(tab.loc[(tab.first_name == 'John') &
              (tab.last_name == 'Smith'),'age'])

# The following shows that we are not going to get any row because
# of the typo: Doe vs. Doeh
print(tab.loc[(tab.first_name == 'John') &
              (tab.last_name == 'Doeh'),'age'])

print(tab.age)
print(tab.age[1])
print(tab.age.iloc[1])
print(tab.age.loc[1])

print(tab.loc[tab.first_name == 'Jane','age'])
print(tab.loc[tab.first_name == 'Jane','age'].iloc[0])
