
# open a file, read and print all the lines in it one at a time
with open('Goldilocks.txt', 'r') as file:
    for line in file:
        print(line)
    
# open a file, read all the lines at once as a list of strings and 
# then print the list
with open('Goldilocks.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
    
