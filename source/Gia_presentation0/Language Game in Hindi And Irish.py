Language_Type = input("Choose one of the following Languages:  Irish, Hindi : ") 
Word = input("Choose a word from the following words: Hindi for hi, Irish for hi, Hindi for bye, Irish for bye : ") 
Irish = 'Irish' 
I_hi = "haigh" 
I_bye = "slan" 
Hindi = 'Hindi' 
H_hi = "namaskar" 
H_bye = "alavida"
if Language_Type == Irish: 
    if Word == "Irish for hi": 
        print("Irish for hi is " + I_hi) 
    if Word == "Irish for bye": 
        print("Irish for bye is " + I_bye)     
if Language_Type == Hindi: 
    if Word == "Hindi for hi": 
        print("Hindi for hi is " + H_hi) 
    if Word == "Hindi for bye": 
        print("Hindi for bye is " + H_bye) 
         