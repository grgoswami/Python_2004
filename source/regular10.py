
a, b = 0, 1
print(a)
print(b)

a, b, c = 0, 1

a, b, c = 0, 1, 100

a = 100
b = a
print(b)

# functions in Python are first class variables
# they can be assigned to other variables much like 
# str, float or int variables

def silly(blah):
    print(blah)
    return blah

print(silly)    
s0 = silly
print(s0)

s0(100)

s1 = silly(10)
print(s1)

print(s1 + s0)

s0(s1)
silly(s1)
silly(s0)

l0 = []
l0.append(1)
print(l0)
l0.append(1000)
print(l0)
l0.append(10)
print(l0)

l1 = [] 
l1.extend(1)
l1.extend([2, 3, 4])
print(l1)
l1.extend([-10, 10])
print(l1)

def foo(bar):
    print(bar)
    
f = foo('hello')
print(f)
print(f is None)
print(f == None)

print(l1)
l1.sort()
print(l1)
