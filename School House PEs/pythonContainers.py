empty = list()
also_empty = []
numbers = [20, 3, 7, 82, -3, 45.6, 3, 65, 23]
pets = ['Moose', 'Jynx', 'Morrigan', 'Sadie', 'Duke', 'Gizmo']

numbers_and_pets = numbers + pets

print(f'Empty lists: {empty} : {also_empty}')
print(f'Numbers: {numbers}')
print(f'Pets: {pets} ')
print(f'Numbers and pets: {numbers_and_pets}')

print(f'numbers[0] is {numbers[0]}')
print(f'pets[2] is {pets[2]}')

slice = numbers_and_pets[7:11]
print(f'Slice: {slice}')

print(f'Some pets: {pets[1:4]}')
print(f'Last pets: {pets[-3:-1]}')
print(len(numbers_and_pets))