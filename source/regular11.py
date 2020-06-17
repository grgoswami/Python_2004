# tuple
# major difference with list: tuples are immutable
t0 = (1, 2, 3)
t0[1] = 100

# lists are multable
l0 = [1, 2, 3]
l0[0] = 100
print(l0)

# strings are immutable
s0 = 'Hello'
s0[1] = 'B'

# raising an exception
# exception is a fancy word for problem

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Do you want to play again?')

i = 5

def f(arg=i):
    print(arg)

# if you provide a value for the optional argument, the function will use it
# if you don't then the function will use the default value    
f(100)

f()

i = -5

# Note the default value is computed or evaluated only once
f()


        