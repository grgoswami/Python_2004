

# lesson1.py: This is our second lesson, a bottom up approach

# Let's write functions; a simple one first
def do_one_thing(thing):
    print('Done: ' + thing)

do_one_thing('Playing')

def do_many_things(thing0, thing1, thing2):
    print('Done: ' + thing0)
    print('Done: ' + thing1)
    print('Done: ' + thing2)

do_many_things('Playing', 'Having dinner', 'Homework')

def assign_students(students):
    """
    This assigns students to different exam rooms based on their first name:
    """
    print('The students:')
    print(students)
    roomA = []
    roomB = []
    for student in students:
        if student[0] >= 'A' and student[0] < 'M':
            roomA.append(student)
        elif student[0] >= 'M' and student[0] <= 'Z':
            roomB.append(student)
    print('The roomA:')
    print(roomA)
    print('The roomB:')
    print(roomB)

students = ['Ari', 'Anya', 'Ben', 'Gia', 'Yuvi', 'Shraddha', 'Tista',
        'Auyona', 'Evaan']
assign_students(students)

