
all_lang = {
    'English':
        {
            'Hi': 'Hi',
            'Bye': 'Bye',
            'Good morning!': 'Good morning!'
        },
        
    'Espanol':
        { 
            'Hi': 'Hola',
            'Bye': 'Adios',
            'Good morning!': 'Buenos dias'
        }
    }
    
all_lang['Espanol']
all_lang['Espanol']['Bye']

lang = input('Enter language: ')
what = input('What word are you looking for: ')
#print(lang)
#print(what)
print(all_lang[lang][what])

all_lang['Hindi']

if 'Hindi' in all_lang:
    print(all_lang['Hindi'])
else:
    lang = input('Enter a new language')
    