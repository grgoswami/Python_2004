
class GroceryStore:
    def __init__(self, name, place):
        print('Creating a GroceryStore object called ' + name + ' in ' + place)
        
    def buy(self, what, amount):
        print('You bought ' + str(amount) + ' ' + what)
        
    def show_my_bill(self, what1, amount1, what2, amount2):
        print('Your bill is: ' + str(amount1) + ' + ' + str(amount2))

    def welcome_to_store(self, greeting):
        print(greeting)

# Parsing
store = GroceryStore('Trader Joes', 'Millburn')
store.buy('Cookies', 3)
store.buy('Tomtoes', 4)
store.show_my_bill('Cookies', 3, 'Tomatoes', 4)

store.welcome_to_store('Hiya!')
