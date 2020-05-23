
import random

while True:
    num = int(input('Enter what number you want to guess up to, greater than 3: '))
    if num <= 3:
        print('Number is too small')
    else:
        break

throw = random.randrange(1, num)

for count in range(0, num + 1):    
    guess = int(input('Enter your guess for the face on the dice : '))
    if guess < throw:
        print('The number is bigger than ' + str(guess))
    elif guess > throw:
        print('The number is less than ' + str(guess))
    else:
        print('You got it right')
        break 
     
