from abc import ABC, abstractmethod
import datetime

"""
Back Account

Создайте класс Account, который будет абстрактным классом для трех классов CheckingAccount(контокоррентный счет), 
SavingsAccount (сберегательный вклад) и BusinessAccount (счет, возникающий при создании бизнеса). 
Управляйте кредитами и дебитами с этих счетов в стиле программы для банкомата.
"""


class Account(ABC):
    
    def __init__(self):
        self.__balance = 0
        self.__history = {}
        self.__pin = 1234

    def checkPINCode(self, value):
        return self.__pin == value

    def changePINCode(self, old, new):
        if self.checkPINCode(old):
            self.__pin = new
            print('Pin code has been successfully changed.')
        else:
            print('Wrong pin code. Try again.')

    def checkBalance(self):
        print(f'Current balance is {str(self.__balance)} $.')

    def checkTransactions(self):
        print('Previous transactions:')
        for item in sorted(self.__history):
            print(item + '\t\t' + str(self.__history[item]) + ' $.')

    @abstractmethod
    def withdraw(self, pin, value):
        if self.checkPINCode(pin):
            if value <= self.__balance:
                currentTime = datetime.datetime.now()
                self.__history[str(currentTime)] = -value
                self.__balance -= value
                print(f'Successfully withdrawn {str(value)}$ from your account.')
            else:
                print('Not enough balance.')
        else:
            print('Wrong pin code. Try again.')

    def deposit(self, pin, value):
        if self.checkPINCode(pin):
            self.__balance += value
            self.__history[str(datetime.datetime.now())] = '+' + str(value)
            print('Successfully deposited ' + str(value) + ' euros from your account.')
        else:
            print('Wrong pin code. Try again.')


class CheckingAccount(Account):
    def __init__(self, credit_range):
        Account.__init__(self,)
        self.credit_range = credit_range

    def withdraw(self, pin, value):
        ''' balance must be > credit range '''
        amount = min(value,abs(self.__balance + self.credit_range))
        cash = Account.withdraw(self, pin, amount)
        return cash


class SavingsAccount(Account):
    def __init__(self):
        Account.__init__(self,)

    def withdraw(self, pin, value):
        cash = Account.withdraw(self, pin, value)
        return cash
