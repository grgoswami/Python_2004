
print(range(7000000000))

# One way of listing the values of range()
print(list(range(10)))

for val in range(10):
    print(val)
    
print(list(range(1000000)))

print(sum(range(7000000000)))

# % is for the remainder
5 % 2
# / is for float division
5 / 2 
# // is for integer division or the quotient
5 // 2

6 % 2

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
        