languages = {'Arabic' : {
    
    'Hi' : 'Marhabaan',
    'Bye' : 'Wadaeaan'
    },
             'Bangla' : {
                 
    'Hi' : 'Ōhē', 
    'Bye' : 'Bidāẏa'
    },
             'Chinese' : {
    'Hi' : 'Hāi', 
    'Bye' : 'Zàijiàn'
    },
             'Danish' : {
    'Hi' : 'Hej', 
    'Bye' : 'Farvel'
    },
             'Espanol' : {
    'Hi' : 'Hola', 
    'Bye' : 'Adiós'
    },
             'French' : { 
    'Hi' : 'Salut & Bonjour',
    'Bye' : 'Au revoir' 
    },
             'German' : { 
    'Hi' : 'Hallo', 
    'Bye' : 'Tschüss'
    },
             'Hawaiian' : {
    'Hi' : 'Aloha', 
    'Bye' : 'Mahalo'
    },
             'Irish' : {
    'Hi' : 'Haigh', 
    'Bye' : 'Slan'
    },
             'Japanese' : {
    'Hi' : 'Konnichiwa', 
    'Bye' : 'Sayōnara'
    },
             'Korean' : {
    'Hi' : 'Annyeong', 
    'Bye' : 'Jalga'
    },
             'Latvian' : {
    'Hi' : 'čau', 
    'Bye' : 'Atā'
    },
             'Mongolian' : { 
    'Hi' : 'Sain uu & sain baina uu', 
    'Bye' : 'Bayartai'
    },
             'Nepali' : { 
    'Hi' : 'Namastē', 
    'Bye' : 'Bāī'
    },
             'Oromo' : {
    'Hi' : 'Akkam', 
    'Bye' : 'Nagaatti'
    },        
             'Polish' : {
    'Hi' : 'Hej', 
    'Bye' : 'gracz bez pary'
    },        
             'Romanian' : {
    'Hi' : 'Bună', 
    'Bye' : 'pa'
    },         
             'Samoan' : {
    'Hi' : 'malo', 
    'Bye' : 'fa'
    },          
             'Thai' : {
    'Hi' : 'S̄wạs̄dī', 
    'Bye' : 'Bāy'
    },
             'Ukrainian' : {
    'Hi' : 'Pryvit', 
    'Bye' : 'Do pobachennya'
    },
             'Vietnamese' : {
    'Hi' : 'Chào', 
    'Bye' : 'tạm biệt'
    },
             'Xhosa' : { 
    'Hi' : 'Mholo', 
    'Bye' : 'Molo'
    },
             'Yoruba' : { 
    'Hi' : 'Bawo', 
    'Bye' : 'O digba'
    }
             }
hi_bye = input('Do you want Hi or Bye : ')
#print(languages.keys())
#print(list(languages.keys()))
#print(' , '.join(list(languages.keys())))
a = ' , '.join(list(languages.keys()))
language0 = input('Choose one of the following languages : ' + a + ' : ')
print(hi_bye + ' in ' + language0 + ' : ' + languages[language0][hi_bye])