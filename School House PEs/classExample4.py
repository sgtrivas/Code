class BankAccount:
    def __init__(self, acct_holder, branch_id):
        self._account_holder = acct_holder
        self._branch_id = branch_id
        #Other attributes will be assigned soon

def main():
    my_account = BankAccount("Fred Flintstone", "BR12")
    your_account = BankAccount("Barney Rubble", "BR45")
    #print(f'{my_account =}\n{type(my_account) = }')
    #print(f'{your_account =}\n{type(your_account) = }')
    print(f'my_account has an account name {my_account._account_holder} opened in branch {my_account._branch_id}')
    print(f'your_account has an account name {your_account._account_holder} opened in branch {your_account._branch_id}')


if __name__=="__main__":
    main()