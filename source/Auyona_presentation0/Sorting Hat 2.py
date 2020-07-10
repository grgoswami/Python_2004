house_color = {
    'red': 'Gryffindor',
    'green': 'Slytherin',
    'blue' : 'Ravenclaw',
    'yellow' : 'Hufflepuff',
    'purple' : 'Hufflepuff',
    'grey' : 'Ravenclaw',
    'silver' : 'Slytherin',
    'black' : 'Ravenclaw',
    'orange' : "Gryffindor",
    'pink' : 'Hufflepuff',
    'gold' : 'Gryffindor'
        }

colors = list(house_color.keys())
# print(', '.join(colors))
print('Hi! I am your virtual Sorting Hat! I will sort you in to a house at Hogwarts!')
print('What is your favorite color out of : ' + ', '.join(colors))
fav_color = input()


print ("You are a... " +  house_color[fav_color] + '!')

house_alumni = {
    'Gryffindor' : 'Harry Potter',
    'Ravenclaw' : 'Luna Lovegood',
    'Slytherin' : 'Severus Snape',
    'Hufflepuff' : 'Cederic Diggory'
    }
house = house_color[fav_color]

print("A famous person from " + house_color[fav_color] + ' is ' + house_alumni[house] )

