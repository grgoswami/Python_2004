
# Type conversions

# int to str
print(str(4))

# str and int cannot be added
'Millburn' + 3
'Millburn' + str(3)

# str to int
print(int('3'))
print(int('Millburn'))
print(int('3.0'))

# str to float
print(float('3'))
print(float('Millburn'))
print(float('3.0'))

print(int(3.5))

# int + int = int
3 + 4

# float + int = float
3.0 + 4

# float converted to an int + int = int
int(3.5) + 4

# anything can be converted to a string
str(3)
str(3.5)
str('Millburn')

# Forth type: boolean
True
False

# The following spelling are not going to work
true 
TRUE 
TrUe

FALSE
false 
FaLse 

done = False
flag = True

print(done)
print(flag)

# This is called checking for a boolean value
if done:
    print('The job is done')
else:
    print('The job is still running')
    
if flag:
    print('We have reached flag')
else:
    print('We have not reached the flag yet')
    
# The following also create boolean values by testing for 
# equality or less than or greater than
print((8 + 6) == 18)

print((8 + 6) == 14)

print((8 + 6) < 18)

print((8 + 6) > 18)

print((8 + 6) <= 18)

print((8 + 6) >= 18)

print(bool('3'))
print(bool('Millburn'))
print(bool('3.0'))
print(bool('False'))
print(bool(''))

# The following are examples of 'list comprehension'
# list all the odd numbers < 10
print([2 * number + 1 for number in range(5)])

# list all the even numbers < 10
print([2 * number for number in range(5)])

 
