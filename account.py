class account:
    """class account  is to create  objects with basic methods  withdraw , deposit , getbalance and getname"""

    def __init__(self, name):
        """__init__ to objects of class account """
        self.__account_name = name  # private data variables initialising
        self.__account_balance = 0

    def deposit(self, amount):
        """deposit(amount) method to add specified money to the account balance"""
        # deposit method
        if amount > 0:  # amount CK
            self.__account_balance = self.__account_balance + amount
            # updating account_balance here
            return True
        else:
            return False

    def withdraw(self, amount):
        """withdraw(amount) method to take some money from the account"""
        # withdraw method
        if amount > 0:  # amount of checking account
            if amount <= self.__account_balance:  # limit of checking account
                self.__account_balance = self.__account_balance - amount  # bank amount and balance updated
                return True
            else:
                return False
        else:
            return False

    def getbalance(self):
        """getbalance method to get account balance with bank"""
        return self.__account_balance  # returning balance statement

    def getname(self):
        """getname method to get account name with bank"""
        return self.__account_name  # returning name statement
