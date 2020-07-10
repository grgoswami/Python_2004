
house_info = {
    'red': ('Gryffindor', 'Harry Potter'),
    'green': ('Slytherin', 'Severus Snape'),
    'blue' : ('Ravenclaw', 'Luna Lovegood'),
    'yellow' : ('Hufflepuff', 'Cederic Diggory'),
    'purple' : ('Hufflepuff', 'Cederic Diggory'),
    'grey' : ('Ravenclaw', 'Luna Lovegood'),
    'silver' : ('Slytherin', 'Severus Snape'),
    'black' : ('Ravenclaw', 'Luna Lovegood'),
    'orange' : ("Gryffindor", 'Harry Potter'),
    'pink' : ('Hufflepuff', 'Cederic Diggory'),
    'gold' : ('Gryffindor', 'Harry Potter')
        }

print('Hi! I am your virtual Sorting Hat! I will sort you in to a house at Hogwarts!')
print('What is your favorite color out of red, green, blue, yellow, grey, purple, silver, black, orange, pink or gold?')

color = input()
print ("You are a... " +  house_info[color][0] + '!')

# print(house_info[color])

print("A famous person from " + house_info[color][0] + ' is ' + house_info[color][1])

