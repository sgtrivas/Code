 #Python 3.x code to demonstrate star pattern
 
# Function to demonstrate printing pattern triangle
def triangle(n,c):
     
    # number of spaces
    k = n - 1
 
    # outer loop to handle number of rows
    for i in range(0, n):
     
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")
     
        # decrementing k after each loop
        k = k - 1
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
            if i % 2 !=1:
                # printing charachters
                print(f"{c}", end="")
    
     
        # ending line after each row
        print("\r")
    print(f"Height: {n}")        
 
# Driver Code
n = 5
#n = int(input("Enter height: "))
c = input("Enter the Character: ")
triangle(n,c)