
# Donuts.
# Given an int count of a number of donuts, print a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) prints 'Number of donuts: 5'
# and donuts(23) prints 'Number of donuts: many'
def donuts(count):
    if count < 10:
        print('Number of donuts: ' + str(count))
    else:
        print ('Number of donuts: many')
    
donuts(5)

donuts(23)
