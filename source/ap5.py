
import random

num = int(input('Enter what number you want to guess up to, greater than 3: '))

done = False
throw = random.randrange(1, num)
    
while not done:
    guess = int(input('Enter your guess for the face on the dice : '))
    if guess < throw:
        print('The number is bigger than ' + str(guess))
    elif guess > throw:
        print('The number is less than ' + str(guess))
    else:
        print('You got it right')
        done = True
              
