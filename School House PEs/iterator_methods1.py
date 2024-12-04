my_list = [1,2,3,4,6,7]
print(f"Old list is :{my_list}")
#print(len(my_list))

for item in range(len(my_list)):
    ans = int(input("Enter item to change: "))
    my_list[item] = ans
print(f"new list is: {my_list}")