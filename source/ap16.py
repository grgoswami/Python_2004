
import pandas as pd

tab = pd.DataFrame({'first_name': ['John', 'Jane', 'John'],
                    'last_name': ['Doe', 'Doe', 'Smith'],
                    'age': [9, 10, 11]})
print(tab)

print(tab.replace(['John'], ['Tom']))
print(tab)

tab.replace(['John'], ['Tom'], inplace=True)
print(tab)
