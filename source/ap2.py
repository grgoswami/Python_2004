
import random

done = False
    
while not done:
    throw = random.randrange(1, 7)
    guess = int(input('Enter your guess a six face dice : '))
    if guess == throw:
        print('You got it right')
        done = True
    else:
        print('Try again; the dice showed up: ' + str(throw))
              
    
    
    