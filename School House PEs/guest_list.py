guests = ['j-lo', 'tyrese', 'denzel washington', 'fat amy', 'will smith']
print("\nHere's the list so far...", guests, '\n')

print(f"However bougie Mrs {guests[0].title()} couldn't make it...\n")
guests[0] = 'jill'
print(f"So we replaced her stankin ass with {guests[0].title()}\n")
print("New list is ", guests, '\n')

#print(f"Hello, {guests[0].title()} you are invited to our wedding" )
#print(f"Hello, {guests[1].title()} you are invited to our wedding" )
#print(f"Hello, {guests[2].title()} you are invited to our wedding" )
#print(f"Hello, {guests[3].title()} you are invited to our wedding" )
#print(f"Hello, {guests[4].title()} you are invited to our wedding",'\n' )

print("We got another table and can add more people!")
guests.insert(0, 'anna')
guests.insert(3, 'brittany')
guests.append('pentatonix')
print (guests,'\n')

print(f"Hello, {guests[0].title()} you are invited to our wedding" )
print(f"Hello, {guests[1].title()} you are invited to our wedding" )
print(f"Hello, {guests[2].title()} you are invited to our wedding" )
print(f"Hello, {guests[3].title()} you are invited to our wedding" )
print(f"Hello, {guests[4].title()} you are invited to our wedding" )
print(f"Hello, {guests[5].title()} you are invited to our wedding" )
print(f"Hello, {guests[6].title()} you are invited to our wedding" )
print(f"Hello, {guests[7].title()} you are invited to our wedding\n" )

guests.sort()
print(guests)
print("We invited", len(guests), "people to the wedding")

