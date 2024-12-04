while True:
    varInput = input("Please enter a letters: ")
    

    if varInput.isdecimal():
        print("Wrong input type")
        break

    else:
        print(f"your letter are {varInput}")