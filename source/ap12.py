
list0 = ['a', 1, 100, 'bb']
list1 = ['test', 'cc', 10, 100000]
for val in list0:
    print(val)
    
for count, val in enumerate(list0):
    print(count, val)
    
print(list0 + list1)
for count, val in enumerate(list0 + list1):
    print(count, val)

    
    
    