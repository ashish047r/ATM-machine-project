# -*- coding: utf-8 -*-
"""ATM machine code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DqyNL_fWUOIB3Rll-6pzXahlNs0DKbwq
"""

class Atm:
    def __init__(self):
        self.pin = ''
        self.__balance = 0
        self.__menu__()

    def __menu__(self):
        user_input = input("""
        Hi, how can I help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit
        """)

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input('Enter your pin: ')
        self.pin = user_pin

        user_balance = int(input('Enter balance: '))
        self.__balance = user_balance

        print('Pin created successfully')

        self.__menu__()

    def change_pin(self):
        old_pin = input('Enter old pin: ')

        if old_pin == self.pin:
            new_pin = input('Enter new pin: ')
            self.pin = new_pin
            print('Pin change successful')
            self.__menu__()
        else:
            print('Cannot process further')
            self.__menu__()

    def check_balance(self):
        user_pin = input('Enter your pin: ')
        if user_pin == self.pin:
            print('Your balance is ', self.__balance)
            self.__menu__()
        else:
            print('Enter correct pin')
            self.__menu__()

    def withdraw(self):
        user_pin = input('Enter the pin: ')
        if user_pin == self.pin:
            amount = int(input('Enter the amount: '))
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                print('Withdrawal successful. Balance is', self.__balance)

            else:
                print('Amount not available')

        else:
            print('Enter correct pin')
        self.__menu__()



