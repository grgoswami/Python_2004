
Language_Type = input("Choose one of the following Languages:  Espanol or Urdu: ") 

Word = input("Choose a word from the following words: Espanol for hi, Urdu for hi, Espanol for bye, or Urdu for bye : ") 

Espanol = 'Espanol' 
E_hi = "Hola." 
E_bye = "Adios." 

Urdu = 'Urdu' 
U_hi = "As-Salam-u-Alaikum." 
U_bye = "Khuda-hafiz and Allah-hafiz." 

if Language_Type == Espanol: 
    if Word == "Espanol for hi": 
        print("Espanol for hi is " + E_hi) 
    if Word == "Espanol for bye": 
        print("Espanol for bye is " + E_bye)     

if Language_Type == Urdu: 
    if Word == "Urdu for hi": 
        print("Urdu for hi is " + U_hi) 
    if Word == "Urdu for bye": 
        print("Urdu for bye is " + U_bye) 
          
