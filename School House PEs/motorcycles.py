motorcycles = []
#print(motorcycles)

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.insert(0, 'ducati')
#print(motorcycles)

#del motorcycles[0]
#print(motorcycles)

#del motorcycles[1]
#print(motorcycles)

#print(motorcycles)
#popped_motorcycles = motorcycles.pop(1)
#print(motorcycles, '\n')
#print(popped_motorcycles)

#print(f"The last motorcycle I owned was a {popped_motorcycles.title()}")

print(motorcycles)

too_expensive = motorcycles[0]
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

