
import random

# For loop
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


# Here for and in are keywords, they are in purple
# The syntax: for something in something:
for st in students:
    print('This prestigious bachelors degree is awarded to: ' + st)
    
for ss in students:
    print(ss + ' gets this degree')
    
for tt in students:
    print('Note: ' + tt + ' gets this degree')
    
    
    
    
    