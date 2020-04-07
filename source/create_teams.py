
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

num_students = len(students)
half_way_mark = num_students // 2
print('\nFirst team is: ' + ', '.join(students[:half_way_mark]))
print('\nSecond team is: ' + ', '.join(students[half_way_mark:]))

# First team is: Yuvi, Evaan, Auyona, Ari
# Second team is: Tista, Ben, Shraddha, Gia, Anya