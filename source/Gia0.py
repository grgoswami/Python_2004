

# Intput should be : Create a Class Movie
# Movie has 3 Arguments, name, year, rating convert integer into string
# Output should be: I like the movie, Sound of Music, made in 1970 and had a rating 9. 
# I watched Emoji and Cocoa for a 22 dollar ticket. 

class Movie:
    def __init__(self, name, year, rating):
        print('I like the movie, ' + name + ' made in ' + str(year) + ' and had a rating ' + str(rating))   
    def Character(self, name1, name, candy):
        print('The characters in this movie are ' + name1 + ' and ' + name + ' who made ' + candy)
movie = Movie("Zootopia", 2019,9)
movie.Character("Nick", 'Judy', 'popsicles' )


#class GroceryStore:
 #   def __init__(self, store, place):
  #      print('Creating a Grocery Store object called' + ' ' + store + ' ' + 'in' + ' ' + place)
   # def buy(self, product, quantity):
    #    print('You bought' + ' ' + str(quantity) +  ' ' + product)
    #def show_my_bill (self, product1, quantity1, product2, quantity2):
     #   print('Your bill is: ' + str(quantity1) + ' ' + '+' + ' ' + str(quantity2))
#store = GroceryStore('Trader Joes', 'Millburn')  
#store.buy('Cookies', 3)
#store.buy('Tomatoes', 4) 
#store.show_my_bill('Cookies', 3, 'Tomatoes', 4) 
 
 # The above should print: 
 #  
 # Creating a GroceryStore object called Trader Joes in Millburn 
 # 'You bought 3 Cookies' 
 # 'You bought 4 Tomatoes' 
 # You bill is: 3 + 4 
 
Classes_4.30.py
Displaying Classes_4.30.py.