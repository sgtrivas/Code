#!/bin/usr/env python3
import pyinputplus as pyip
class Account:
    """Simple bank account using classes"""

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f'account created for {self.name}')

    def deposit(self, amount):
       
        if amount > 0:
            self.balance += amount    

    def withdraw(self, amount):

        if amount >0:
            self.balance -= amount

    def show_balance(self):
        print(f'Balance is {self.balance}')


if __name__=='__main__':

    tim = Account("Tim", 0)
    tim.show_balance()
    tim.deposit(1000)
    tim.show_balance()
    tim.withdraw(500)
    tim.show_balance()
