from datetime import date
from random import randrange


class BankAccount:
    def __init__(self, acct_holder, branch_id):
        self._account_holder = acct_holder
        self._branch_id = branch_id
        self._date_opened = date.today()
        self._account_id = ''.join(["ACCT", str( randrange(1,1_000_000))])
        self._account_status = "Open"
        #Other attributes will be assigned soon
    @property
    def account_holder(self):
        return self._account_holder
    
    @property
    def branch_id(self):
        return self._branch_id
    
    @property
    def status(self):
        return self._account_status
    
    @property
    def date(self):
        return self._date_opened
    
    @property
    def acctId(self):
        return self._account_id

def main():
    my_account = BankAccount("Fred Flintstone", "BR12")
    your_account = BankAccount("Barney Rubble", "BR45")
    #print(f'{my_account =}\n{type(my_account) = }')
    #print(f'{your_account =}\n{type(your_account) = }')
    print(f'my_account has an account name {my_account._account_holder} opened in branch {my_account._branch_id} on {my_account.date} with status = {my_account.status} with id {my_account.acctId}')
    print(f'your_account has an account name {your_account._account_holder} opened in branch {my_account.status} on {your_account.date} with status = {my_account.status} with id {my_account.acctId}')


if __name__=="__main__":
    main()