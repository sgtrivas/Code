"""
Implementation of a BankAccount class in Python
To be filled in as the chapter progresses

*(Attribute) an account identifier
*(Attribute) an account status (opened or closed)
*(Attribute) an account holder name
*(Attribute) a bank branch identifier
*(Attribute) The date the account was opened
*(Behavior) accessing/changing the account holder and account status
*(Behavior) closing an account
*(Behavior) print readable representation of bank accounts

"""

class BankAccount:
    def __init__(self, acct_holder, branch_id):
        self._account_holder = acct_holder
        self._branch_id = branch_id
        #Other attributes will be assigned soon

def main():
    my_account = BankAccount("Fred Flintstone", "BR12")
    your_account = BankAccount("Barney Rubble", "BR45")
    print(f'{my_account =}\n{type(my_account) = }')
    print(f'{your_account =}\n{type(your_account) = }')


if __name__=="__main__":
    main()