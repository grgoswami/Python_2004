
import random

done = False
throw = random.randrange(1, 7)
    
while not done:
    guess = int(input('Enter your guess a six face dice : '))
    if guess < throw:
        print('The number is bigger than ' + str(guess))
    elif guess > throw:
        print('The number is less than ' + str(guess))
    else:
        print('You got it right')
        done = True
              
