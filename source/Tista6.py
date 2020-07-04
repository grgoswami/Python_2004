import difflib

animals = ['dog', 'cat', 'horse', 'bear', 'chicken', 'lizard', 'snake', 
           'snail', 'slug', 'unicorn', 'gryphon', 'elephant', 'dragon', 
           'tiger', 'lion', 'jaguar', 'panther', 'leopard', 'rhino', 
           'peacock', 'bird', 'canary', 'monkey', 'chimpanzee', 'chimp', 
           'orangutan', 'bunny', 'butterfly', 'squirrel', 'rabbit', 'cow',
           'parrot', 'puppy', 'pup', 'fish', 'octopus', 'squid', 'sheep',
           'lamb', 'pig', 'penguin', 'kitty', 'fox', 'turtle', 'tortoise',
           'frog', 'alligator', 'croc', 'crocodile', 'rat', 'mouse', 
           'hamster', 'guinea pig', 'iguana', 'dinosaur', 'dino',
           'dolphin', 'shark', 'jellyfish', 'ant', 'centipede', 
           'kangaroo', 'joey', 'crab', 'llama', 'zebra', 'giraffe', 
           'bee', 'buffalo', 'bison', 'bull', 'beaver', 'possum', 
           'porcupine', 'scorpion', 'turkey', 'hedgehog', 'sea cucumber',
           'aardvark', 'owl', 'pirhana', 'baracuda', 'tuna', 'coyote', 
           'badger', 'caterpillar', 'catfish', 'toad', 'cheetah', 'bat',
           'chupacabra', 'cobra', 'chameleon', 'chinchilla', 'spider', 
           'whale', 'hare', 'armadillo', 'racoon', 'hornet', 'wolf', 
           'wolves', 'anteater', 'crane', 'pelican', 'lobster', 'panda',
           'toucan', 'worm', 'worms', 'flies', 'fly', 'firefly', 'fireflies']

def spellcheck(string):
    for word in string.casefold().split():
        if word not in animals:
            suggest = difflib.get_close_matches(word, animals)
            print('Did you mean : ' + ' or '.join(suggest))
        else:
            print("Correct Spelling")
           
animal_or_animals = input('Enter an animal(s): ')

spellcheck(animal_or_animals)
