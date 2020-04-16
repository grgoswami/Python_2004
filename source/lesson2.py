
print('Turn on tap')
print('Lather up with soap')
print('Rub soap and water for 20 seconds')
print('Rinse your hands')

# def means definition or define, it's a keyword
# You need def and (): to define a function
# () holds function arguments
# The spaces in the body of the function are necessary and they
# are called indentation
def wash_your_hands():
    print('Turn on tap')
    print('Later up with soap')
    print('Rub soap and water for 20 seconds')
    print('Rinse your hands')

# Use or call the function    
wash_your_hands()
wash_your_hands()
wash_your_hands()
wash_your_hands()

# Here topping1 and topping2 are arguments to the function
# make_pizza
def make_pizza(topping1, topping2, topping3, topping4):
    print('Make pizza dough')
    print('Put ' + topping1)
    print('Put ' + topping2)
    print('Put ' + topping3)
    print('Put ' + topping4)
    print('Bake it in the oven')
    
# The three arguments below are called positional arguments    
make_pizza('Banana pepper', 'Mushroom', 'Broccolli', 'Olive')
make_pizza('Olive', 'Broccolli', 'Banana pepper', 'Mushroom')
make_pizza('Mushroom', 'Broccolli', 'Olive', 'Banana pepper')
make_pizza('Mushroom', 'Broccolli', 'Olive', 'Banana pepper', 'Pepperoni')

    
    
    



