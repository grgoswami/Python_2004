
age = 2
# The following is an if conditional statement
if age < 2:
    print('baby')
else:
    print('not a baby')
    
age = 3
if age < 2:
    print('baby')
elif age < 4:
    print('toddler')
else:
    print('not a baby or toddler')

# You can have only one if, followed by many many elif and ending in 
# only one else
age = 7
if age < 2:
    print('baby')
elif age < 4:
    print('toddler')
elif age < 13:
    print('kid')
else:
    print('not a baby or toddler or kid')
    
def pretty_number(num_emails):
    print(num_emails)
    if num_emails < 1000:
        print('number of emails is: ' + str(num_emails))
    else:
        print('number of emails: 1000+')

pretty_number(6422)
pretty_number(32)

