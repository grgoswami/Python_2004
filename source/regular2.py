
s = 'First line.\nSecond line.'
print(s)

s1 = 'First line.\tSecond line.'
print(s1)

print('(Hello\n world)')
print(r'(Hello\n world)')

print('''\
Hi there
How are you?  
Blah
blah
''')

print(3 * 'blah ')
print(80 * '=')
print(3.5 * 'blah ')
print('weird ' * 'blah ')

def simple(word):
    return word[:2]

simple('Corona')

import time

time.sleep(10)
print('Was waiting')

any(['Hello', 1, 2.3, False])
any([False, False])

if 1.0 in [1.0, 2.0]:
    print('1.0 is in the list')
    



