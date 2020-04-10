
# The following is based on create_teams.py that you saw first day of
# our class. Now modify the code below to create three teams instead
# of two.

import random

students = ['Ari', 'Anya', 'Ben', 'Gia', 'Yuvi', 'Shraddha', 'Tista',
        'Auyona', 'Evaan']
print('The students:')
print(students)

students.sort()
print('\nThe students sorted by first name:')
print(students)

random.shuffle(students)
print('\nThe students after shuffling:')
print(students)

# Change the code below this line
num_students = len(students)
half_way_mark = num_students // 2

print('\nFirst team is:')
print(students[:half_way_mark])

print('\nSecond team is:')
print(students[half_way_mark:])

print('\nThird team is:')
