def concat(*args, sep="/"):
    print(args)
    return sep.join(args)
print(concat('a', 'b', 'c'))
print(concat('a', 'b', 'c', 'd', 'e', sep='|'))
def collect(**keywords):
    print(keywords)
    for kw in keywords:
        print(kw, keywords[kw])
    for key, value in keywords.items():
        print(key, value)
collect(color='blue', shape='circle', radius=3.14)
collect(color='blue', shape='circle', radius=3.14, blah='blah')
a = 0
b = 1
a, b = 0, 1
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")
d = {"voltage": "four million", 
     "state": "bleedin' demised", 
     "action": "VOOM"}
parrot(**d)
parrot(voltage="four million", 
     state="bleedin' demised", 
     action="VOOM")
parrot("four million", "bleedin' demised", "VOOM")
args = ("four million", "VOOM", "bleedin' demised")
parrot(*args)