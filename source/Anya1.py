

pig = 'ay'
original = 'ANYA'
print('The word we will convert to pig latin is: ' + original)
first = original[0]
print (first)
second = original[1:]
print (second)
new_word = second + first + pig
print (new_word)



def pig_latin(word):
    """
    Arguments
    ----------
    word : string
      
    Returns
    -------
    All but the first letter of the word + the first word + 'ly'.
    Hint: All you'll nee;1d are slicing and string concatenation
    Write your code below
    """
pig_latin('star')
   
word = ['pickle-ball','basketball', ' tennis']
word1 = word[0:2]
print (word1)
pig_latin = 'some'
pig_latin2 = pig_latin[0:1]
pig_latin3 = pig_latin[1:]
print (pig_latin3 + pig_latin2 + "ay")



abc = input('Enter a word : ')
print("This is the word we will convert to pig-latin - " + abc + ".")
new_abc = abc[0]
pig_latin_abc = abc[1:] + new_abc + 'ay'
print("The pig-latin word is " + pig_latin_abc + ".")


