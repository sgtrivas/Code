import pyinputplus as pyip

def main(acct,passW):
    if acct != 'bob' or 'Bob' and passW != 'pass1234':
        print("Access Denied: User Not found")
    else:
        print("Access Granted!")

if __name__ == "__main__":
    userAcct = pyip.inputStr(prompt="Please enter the username: ")
    userPass = pyip.inputPassword(prompt="Please enter the password: ")

    main(userAcct,userPass)