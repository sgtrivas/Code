mylist = []
for i in range(1,5050505,23):
    if i % 2 == 1:
        mylist.append(i)

print(sum(mylist))