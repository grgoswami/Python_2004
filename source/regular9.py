
for num in range(2, 20):
    # Variables like is_prime below is often reffered to as flag variables
    is_prime = True
    for small in range(2, num):
        if num % small == 0:
            print(num, 'is not a prime:', num, '=', small, '*', num // small )
            is_prime = False
            break
    if is_prime == True:
        print(num, 'is a prime')

def find_primes(number):
    """
    Parameters
    ----------
    num : integer
        Should be positive.

    Returns
    -------
    It prints all the prime numbers less than number.
    """        
    for num in range(2, number):
        # Variables like is_prime below is often reffered to as flag variables
        is_prime = True
        for small in range(2, num):
            if num % small == 0:
                print(num, 'is not a prime:', num, '=', small, '*', num // small )
                is_prime = False
                break
        if is_prime == True:
            print(num, 'is a prime')

find_primes(30)    
find_primes(100)    

def foo(bar, baz, buzz, happy):
    """
    Parameters
    ----------
    bar : TYPE
        DESCRIPTION.
    baz : TYPE
        DESCRIPTION.
    buzz : TYPE
        DESCRIPTION.
    happy : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    
    
for num in range(2, 10):
    if num % 2 == 0:
        print(num, 'is an even number')
    else:
        print(num, 'is an odd number')
        
for num in range(2, 10):
    if num % 2 == 0:
        print(num, 'is an even number')
        continue
    print(num, 'is an odd number')
        
        
        
        
    
    
    
    
    