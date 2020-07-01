
done = False
while not done:
    riddle = input('What has 2 hands, no feet, a face and never stops running? :')
    if riddle == 'clock':
        print('Woho! you got it right!')
        done = True
    else:  
        print('Boo hoo. You got it wrong. :( please try again')
