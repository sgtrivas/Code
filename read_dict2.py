dictionary = {}

with open('Oxford_dictionary.txt', 'r') as f:
    for line in f:
        w = f.readline()
        x = line.strip().split('(')
        d1 = {x[0].rstrip():x[1:]}
        d2 = dictionary.update(d1)

#print(len(dictionary))
        
#word = input("enter word to get the definition: ").title()

#print(dictionary[word])

a = dictionary.values()
for i in a:
    print(i)
  
