
import random

name = input('Enter your name:')
# age1 = input('Enter your age1:')
# age2 = int(input('Enter your age2:'))
age = input('Enter your age:')
place = input('Enter wher you live:')
boy_girl = input('Enter if you are a boy or girl:')
adjective = input('Enter an adjective which you would use to describe yourself:')
why_adjective = input('Why did you describe yourself ' + adjective + '?')
what_to_do = input('What do you like to do outside if it is a little windy, sunny, or warm?')
what_to_do1 = input('What do you like to do when it is snowing outside?')
food = input('Enter you favorite food')
why_that_food = input('Why is ' + food + ' your favorite food')
relative = input('Enter a relative')
girl = 'girl'
boy = 'boy'

weather = ['rainy','really windy', 'a little windy','sunny','warm','snowing','cloudy','really cold','really hot']
print('                                                                                                              ')

random_weather = random.choice(weather)
print(random_weather)

if boy_girl == girl:
    print ('There was once a girl named ' + name + '. She was ' + str(age) + ' years old.')
    print (name + ' lived in ' + place + '. ' + 'She was ' + adjective + '.' )
    print ('She was ' + adjective + ' because ' + why_adjective)
    print ('The next day ' + name + ' went outside. It was ' + random_weather)
   
if boy_girl == boy :
    print ('There was a boy named ' + name + '. he was ' + str(age) + ' years old.')
    print (name + ' lived in ' + place + '. ' + name + ' was ' + adjective + '.' )
    print ('He was ' + adjective + ' because ' + why_adjective)
    print ('The next day ' + name + ' went outside. It was' + random_weather)
   
if boy_girl == girl:
    if random_weather == 'rainy' or 'cloudy' or 'really hot' or 'really cold' or 'really windy':
        print("She didn't really like it when it was " + random_weather + ' so she went back inside')
    if random_weather == 'a little windy' or 'sunny' or 'snowing' or 'warm':
        print ('She liked it when it was ' + random_weather + '.')
if boy_girl == boy:
    if random_weather == 'rainy' or 'cloudy' or 'really hot' or 'really cold' or 'really windy':
        print("He did't really like it when it was " + random_weather + ' so he went back inside')
    elif random_weather == 'a little windy' or 'sunny' or 'snowing' or 'warm':
        print ('He liked it when it was ' + random_weather + '.')
if random_weather == 'sunny' or 'a little windy' or 'warm':
    print(name + ' decided to ' + what_to_do + '.')
elif random_weather == 'snowing':
    print(name + ' decided to ' + what_to_do1 )

if boy_girl == girl:
    print('When she came back into her house she had lunch. For lunch she had her favorite food which was' + food + '.')
    print (name + ' liked to eat that food because ' + why_that_food + '.')
    print(name + ' found out that next week was her ' + relative + "'s birthday")
if boy_girl == boy:
    print('When he came back into her house he had lunch. For lunch he had his favorite food which was ' + food + '.')
    print (name + ' liked to eat that food because ' + why_that_food + '.')
    print(name + ' found out that next week was his ' + relative + "'s birthday")
