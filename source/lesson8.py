
# class is a collection of functions and variables
# class is a way of encapsulating methods and data
# This is also called object oriented programming (OOP)

class Restaurant:
    def __init__(self, name, where):
        print('Creating a Restaurant object called ' + name +
              ' in ' + where)
        
    def combo2(self, item1, item2):
        print('Serving combo2 of: ' + item1 + ' and ' + item2)
        return [item1, item2]
    
    def combo2_with_options(self, item1, item2, allergic_to):
        print('Serving combo2 of: ' + item1 + ' and ' + item2)
        print('Note: allergic to: ' + allergic_to)
        return [item1, item2]

    def combo3(self, item1, item2, item3):
        print('Serving combo3 of: ' + item1 + ' and ' + item2 + ' and ' + item3)
        return [item1, item2, item3]
        
    def how_to_make_pizza(self, topping1, topping2):
        print('Make dough')
        print('Put ' + topping1)
        print('Put ' + topping2)
        
    def Pizza(self):
        "Will define later"
        pass            
    
    def ice_cream(self, topping1, topping2):
        print('Pour and freeze milk')
        print('Put ' + topping1)
        print('Put ' + topping2)        

print(Restaurant)
        
# res is the object of class Restaurant   
# An object is an instance of a class
# In other words objects are instantiated
res = Restaurant('Cheesecake Factory', 'Short Hills')

# Call a method on an oject of a class
print(res.combo2('Pizza', 'Cupcake'))
print(res.how_to_make_pizza('Peppers', 'Chicken'))

print(res.how_to_make_pizza('Peppers', 'Cars'))

print(res.combo2('Ice cream', 'Starwberry'))

print(res.combo2(Pizza, 'Cupcake'))

print(res.combo3('Ice cream', 'Starwberry', 'Cupcake'))

print(res.combo2_with_options('Cupcake', 'Strawberry', 'Nuts'))


