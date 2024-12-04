import pyinputplus as pyip

iterList = ['Moose','Jynx', 'Morrigan', 'Sadie', 'Duke', 'Gizmo']

print("Heres the list of items you can change")
print('*' * 70)
for items in iterList:
    print(items)
print()
listPos = pyip.inputNum(prompt=f"What do you want to change? enter 0 - {len(iterList)-1}> ")

print(f'{iterList[listPos]}',"\n")
newItem = input("What do you want to change it to? ")
print()

iterList[listPos] = newItem
print("Here is the new list.")
print('*' * 70)
for items in iterList:
    print(items)


