import pyinputplus as pyip
dictionary = {}

with open('Oxford_dictionary.txt', 'r') as f:
    for line in f:
        w = f.readline()
        x = line.strip().split('(')
        d1 = {x[0].rstrip():line}
        d2 = dictionary.update(d1)
word = ''

while word != 'Q':
    word = pyip.inputStr("Enter word to get the definition (enter q to stop): ").title()
    if word in dictionary and word != 'Q':
        for z in dictionary[word]:
            definition = dictionary[z]
            print(f'\nThe definition for the word {word} is \"{definition.rstrip()}\"')
    elif word not in dictionary and word != 'Q':
        print(f'\nThis {word} is not recognized in the Oxford Dictionary!')
    if word == 'Q':
        print(f'{word} Thank you, Goodbye')
        break   

