
def duplicates(list1, list2):
    for num in list1:
        if num == list1:
            list2.append(num)
    print(set(list2))
my_list = [1,2,3,4,4,5,5,6,7,8,9,9]
new_list = [] 

duplicates(my_list,new_list)
