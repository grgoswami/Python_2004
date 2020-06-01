
# The is called 'tuple unpacking'
a, b = 0, 1
print(a)
print(b)

a = 0
b = 1

c, d, e = 4, 5, 6
print(c)
print(d)
print(e)

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b
    
a, b = 0, 1
while a < 20:
    print(a)
    c = a + b
    a = b
    b = c
    
i = 256 * 256
print('The value of i is ' + str(i))    

print('The value of i is', i)    

print('The value of i is', i, sep='|=!')    

j = 100
print('The value of i is', i, 'and the value of j is', j)    

print('The value of i is', i, 'and the value of j is', j, end='\n\n\n\n\n')    

x = int(input("Please enter an integer: "))
print(x)

# The if, elif and else conditions should always be 'mutually exclusive'
# that is if one is satisfied the other shouldn't
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
    