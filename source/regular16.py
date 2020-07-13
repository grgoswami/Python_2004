
def foo():
     """
Do nothing, but document it.

No, really, it doesn't do anything.
     """
     pass
 
print(foo)
print(foo.__doc__)

def bar(arg0, arg1):
    """
    

    Parameters
    ----------
    arg0 : int 
        the number of bunnies.
    arg1 : str
        name of the mother.

    Returns
    -------
    None.

    """
    print(arg0, arg1)
    
print(bar.__doc__)
print(bar.__name__)

f1 = bar
print(f1.__name__)

x = 100
print(x)
print(x.__name__)

y = [100]
print(y)
print(y.__name__)

def baz(fly):
    print(fly)
    
print(baz.__doc__)    

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits)

print(fruits.reverse())
print(fruits)

print(fruits.pop())
print(fruits)

# alphabetical or lexicograhical or language dictionary order
print(fruits.sort())
print(fruits)

print(fruits.pop(2))
print(fruits)

print(fruits[2])
print(fruits)
