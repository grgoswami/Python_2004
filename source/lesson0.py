
# lesson0.py: This is our first lesson, a bottom up approach
# Hi everyone 

"""
A multi line comment.
Hi Mr. President.

This is also called a 'doc string'
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

# Working with constants
2 + 3
2 * 3
3 / 2
3 - 2

21.4 + 90.7
90 - 21
21.4 + 90

"Millburn" + "21.4"

weight * age + 3 / 100 - 2000

weight / age + weight * age * age * age

# Work with list
# Here students is the list
# The names within the list are the elements of the list
students = ['Ari', 'Anya', 'Ben', 'Gia', 'Yuvi', 'Shraddha', 'Tista',
        'Auyona', 'Evaan']
print(students)
len(students)

# Index a list
# Python indexes starting from 0 or Python starts counting from 0
# Whereas we start counting from 1
# When you start indexing from the begining of the list
# you start from 0
students[0]
students[1]
students[2]
students[8]
students[100]

# When you start indexing from the end of the list
# you start from -1
students[-1]
students[-2]
students[-3]

students[-8]
students[-9]
students[-10]
students[-100]


# Slice a list
# 0 is starting index and 3 is the ending index, but we don't
# touch 3, end just before 3
# begin:end
students[0:3]
# Here 0 is the starting index and 3 is the ending index
students[:3]
# Here -3 is the starting index and end of the list is the 
# ending index
students[-3:]

# Python indexing is call left inclusive, right exclusive
students[-3:-1]
students[3:5]
students[-4:-2]
students[-6:-3]
students[0:100]
students[:]

# if, elif, else statement
# are also known as 'conditional statements'
age = 8
print(age)

if age < 2:
    print('baby')
else:
    print('not a baby')

# elif is short for else if     
age = 97
if age < 2:
    print('baby')
elif age < 4:
    print('toddler')
elif age < 13:
    print('kid')
elif age < 21:
    print('teenager')
else:
    print('adult')
          
# length of a string
len('Pizza')
len('Cheese')

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

