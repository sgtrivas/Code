#  This variable will set the height to whatever number you choose.
n = 20

#  This loop will begin drawing our tree and spacing the character out 'n-1' number of spaces
for i in range(0, n):
    print(" " * (n-i), end="")
    #  This loop is responsible for printing our characters starting with '1'
    for j in range(0, i+1):
        #  I added this if statement to only print out odd number of characters.
        if i % 2 != 1:
            print('*', end=" ")
            
    print()