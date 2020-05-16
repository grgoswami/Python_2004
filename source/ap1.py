
# open a file, read and print all the lines in it one at a time
with open('Goldilocks.txt', 'r') as file:
    for line in file:
        print(line)
    
# open a file, read all the lines at once as a list of strings and 
# then print the list
with open('Goldilocks.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
    
# os: operating system
    
with open('/home/gopi/Python_202004/source/corona.txt', 'r') as file:
    for line in file:
        print(line)
        
paths = ['/home/gopi/Python_202004/source/corona.txt',
         '/home/gopi/Python_202004/source/class.txt']
for path in paths:
    print('Reading file with path: ' + path)
    with open(path, 'r') as file:
        for line in file:
            print(line)
            
