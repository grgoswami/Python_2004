
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(100))

print(f(10, [-1]))
print(f(100))

print(f(10, [-1, 1, 1000]))
print(f(100))

print(f(10, L=[1, 2, 3]))
print(f(10, L=[1, 2, 3]) + f(6, L=[5]))
print(f(10, L=[1, 2, 3]) + f(6) + f(400))

# This confusing phenomenon is used in something called 'closure',
# it's sometimes called sharing states over consecutive calls of 
# a function

def g(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(g(1))
print(g(2))

print(g(10, [-1]))
print(g(10, [None]))
print(g(10, None))

