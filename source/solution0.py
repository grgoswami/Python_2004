# The following is based on create_teams.py that you saw first day of
# our class. Now modify the code below to create three teams instead
# of two.

import random

students = ['Ari', 'Anya', 'Ben', 'Gia', 'Yuvi', 'Shraddha', 'Tista',
        'Auyona', 'Evaan', 'Adrij', 'Cossal', 'Cari', 'Byron']
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
print(num_students)
one_third = num_students // 3
print(one_third)
two_third = 2 * one_third
print(two_third)

print('\nFirst team is:')
print(students[0:one_third])

print('\nSecond team is:')
print(students[one_third:two_third])

print('\nThird team is:')
print(students[two_third:num_students])
