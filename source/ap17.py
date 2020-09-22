
# Write a function that return the odd numbers up to the given argument
def get_odd_numbers(number):
    ret = []
    for num in range(number):
        if num % 2 == 1:
            ret.append(num)
    return ret
            
print(get_odd_numbers(8)) 
print(get_odd_numbers(13)) 
           
# Write a function that uses Camel casing on a given list of words and returns
# the modified list
def camel_casing(list_of_words):
    ret = []
    for word in list_of_words:
        cword = word[0].upper() + word[1:]
        ret.append(cword)
    return ret

print(camel_casing(['Jane', 'is', 'a', 'nice', 'girl']))
print(camel_casing(['John', 'is', 'a', 'good', 'boy']))

print(' '.join(camel_casing(['John', 'is', 'a', 'good', 'boy'])))

    
    