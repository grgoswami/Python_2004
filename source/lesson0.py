
# lesson0.py: This is our first lesson, a bottom up approach
# Hi everyone 

"""
A multi line comment.
Hi Mr. President.
"""

# Lets print
print("Hello world!")
print('Hello world!')
print("Hi There")

# Define variables
name = 'Jane Doe' 
age = 2
weight = 23.4
print(name)
print(age)
print(weight)

distance = 100
print(distance)

place = 'Millburn'

# For adding strings
print(name + ' from ' + place + ' is a cute baby')

# For adding string and int
print('{0} {1}'.format(name, age))
# For adding string and float
print('{0} {1}'.format(name, weight))

name = "John Doe"
age = 3
weight = 34.5
print(name)
print(age)
print(weight)

# Work with list
students = ['Ari', 'Anya', 'Ben', 'Gia', 'Yuvi', 'Shraddha', 'Tista',
        'Auyona', 'Evaan']
print(students)

# Index a list
students[0]
students[1]
students[2]

students[-1]
students[-2]
students[-3]

# Slice a list
students[0:3]
students[:3]
students[-3:]

# Build a list
to_do_list = []
to_do_list.append('Play with friends')
to_do_list.append('Coding')
to_do_list.append('TV time')
to_do_list.append('Dinner time')
print(to_do_list)

# Add two lists
list0 = ['a', 'b', 'c']
list1 = [1, 2, 3]
print(list0)
print(list1)
print(list0 + list1)

# Search in a list
grocery_list = ['Rice', 'Bread', 'Tomato soup', 'Cheese', 'Egg', 'Milk',
        'Tomato', 'Nuts', 'Peanut butter']

# Search in the short form using 'list comprehension' and 'if condition'
tomato_related = [item for item in grocery_list if item.find('Tomato') >= 0]
print(tomato_related)

nut_related = [item for item in grocery_list if item.lower().find('nut') >= 0]
print(nut_related)

# Search in the long form using 'for loop' and 'if condition'
tomato_related = []
for item in grocery_list:
    if item.find('Tomato') >= 0:
        tomato_related.append(item)

print(tomato_related)

nut_related = []
for item in grocery_list:
    if item.lower().find('nut') >= 0:
        nut_related.append(item)

print(nut_related)

# The range function
print(list(range(10)))
print(list(range(1, 10)))

# Other uses of list comprehension
# The even numbers
print([2 * number for number in range(1, 6)])

# The odd numbers
print([2 * number - 1 for number in range(1, 6)])

