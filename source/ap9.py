
fruit  = 'I like to eat %s'

# The following is called Python 2 style string formatting
print(fruit %('oranges'))
print(fruit)

# This following is Python 3 style string formatting
fruit = 'I like to eat {0} and {1}'
print(fruit.format('oranges', 'strawberry'))
print(fruit)

