import random

done = False
throw = random.randrange(1, 7)
    
while not done:
    guess = int(input('Enter your guess a six face dice : '))
    if guess == throw:
        print('You got it right')
        done = True
    else:
        print('Try again')
              

while True:
    print('blah')