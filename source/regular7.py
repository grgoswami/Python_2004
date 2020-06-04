words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w), w + '!')
    
l0 = ['a', 'b', 'c']
l0[1] = 'BBB'
print(l0)
l0[1] = 'Bye'
print(l0)

active_users = {}
active_users['John'] = 'awake'
active_users['Jane'] = 'slepping'
print(active_users)

for user, status in active_users.items():
    print(user, status)
    
active_users['John'] = 'sleeping'
print(active_users)

print(list(range(0, 10, 3)))

print(list(range(0, 10, 4)))

print(list(range(0, 10, 2)))
print(list(range(1, 10, 2)))
    
range(-10, -100, -30)
