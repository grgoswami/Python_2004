
word = 'ABCDEFGhijKK'
word1 = ''

for q in word:
    if (q.isupper()) == True:
        word1 += (q.lower())
    elif (q.islower()) == True:
        word1 += (q.upper())
    elif (q.isspace()) == True:
        word1 += q 
    
print (word1)