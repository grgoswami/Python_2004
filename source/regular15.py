
lfunc0 = lambda a, b: a + b
lfunc0(10, 100)

lfunc1 = lambda a, b: a * b
lfunc1(10, 100)

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)
f(10)

def make_lambda0(n):
    l0 = lambda x: x + n
    l1 = lambda x: x - n
    print(l0, l1)

make_lambda0(10)    
    
f = make_incrementor(5)
f(50)   

def make_incrementor1(n):
    def temp(x):
        return x + n
    return temp

f1 = make_incrementor1(42)
f1(0)
f1(10)

# pairs is a list of tuples
pairs = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
print(pairs)
pairs[0]
pairs[3]

# Lexicographical sorting
pairs.sort(key=lambda pair: pair[1])
pairs

# Numerical sorting
pairs.sort(key=lambda pair: pair[0])
pairs

