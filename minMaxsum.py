empty = []
numbers = [3,1,-10,54,75,29,4.2]
pets = ['Moose','Jynx', 'Morrigan', 'Sadie', 'Duke', 'Gizmo']

print(f'Empty: {empty}')
print(f'Max empty is: {max(empty, default=None)}')
print(f'Min empty is: {min(empty, default=None)}')
print(f'Sum of empty is: {sum(empty, start=0)}')

print()
print(f'Numbers: {numbers}')
print(f'Max empty is: {max(numbers, default=None)}')
print(f'Min empty is: {min(numbers, default=None)}')
print(f'Sum of empty is: {sum(numbers, start=0)}')

print()
animals = ['bee','zebu','albatross','cat','zebra']
print(f'animals: {animals}')
#furthest from A
print(f'Max animals is: {max(animals, default=None)}')
#closest to A
print(f'Min animals is: {min(animals, default=None)}')
#longest string character count
print(f'Max animals key length is: {max(animals, key=len)}')
#shortest string character count
print(f'Min animals key length is: {min(animals, key=len)}')

print(f'pets: {pets}')
#furthest from A
print(f'Max pets is: {max(pets, default=None)}')
#closest to A
print(f'Min pets is: {min(pets, default=None)}')
#longest string character count
print(f'Max pets key length is: {max(pets, key=len)}')
#shortest string character count
print(f'Min pets key length is: {min(pets, key=len)}')