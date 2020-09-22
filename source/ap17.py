
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

s0 = 'Awesome'
print(s0)
print(s0.upper())

print(s0.replace('esome', 'ful'))

s1 = 'Jane is an excellent student. I highly recommend her.'
print(s1.replace('Jane', 'Sarah'))
    
s2 = 'John is an excellent student. I highly recommend him.'
print(s2.replace('John', 'Mike'))
print(s2.replace('highly', 'some what'))

print(s2.startswith('Jane'))
print(s2.startswith('John'))
    
l1 = ['My', 'name', 'is', 'Peter']
print(' '.join(l1))
    