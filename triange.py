def triangle(base,charActer):
    for n in range(0,base):
        print(f"{charActer}")
        for i in range(0,n+1):
            print(f"{i}")
        
    print(f"height: {base}")

charActer = input("Enter character to draw: ")
base = int(input("how tall: "))
triangle(base,charActer) 