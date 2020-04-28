
# class is a collection of functions and variables

class Restaurant:
    def __init__(self, name, where):
        print('Creating a Restaurant object called ' + name +
              ' in ' + where)
        
    def combo2(self, item1, item2):
        print('Serving combo2 of: ' + item1 + ' and ' + item2)
        return [item1, item2]

# res is the object of class Restaurant   
# An object is an instance of a class
# In other words objects are instantiated
res = Restaurant('Cheesecake Factory', 'Short Hills')

# Call a method on an oject of a class
print(res.combo2('Pizza', 'Cupcake'))

print(res.combo2('Ice cream', 'Starwberry'))

