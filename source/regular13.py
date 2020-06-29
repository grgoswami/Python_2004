
s0 = 'Hello'
type(s0)
isinstance(s0, str)

# percentage
print('=' * 40)
print(40 * '=')

d0 = {'a': 1, 'b': 2}

for key, value in d0.items():
    print(key, ':', value)
    
for key in d0:
    print(key, ':', d0[key])
    
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
        
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch",
           test='Test')
        
    