
letter = input('Enter a word : ')

guess = input ('Enter a letter')


if guess == letter:
    print('you got it right')
else:
    print('Try again')
    guess2 = input ('Enter another guess')
if guess2 == letter:
    print('you got it right')
else:
    print('You lost 1 point so to bad for you')
    guess3 = input('Enter another guess')
if guess3 == letter:
    print('Yay! You got another point')
else:
    print('Nah nah nah boo boo')
   
    # if all guesses are wrong, nah nah nah boo boo!