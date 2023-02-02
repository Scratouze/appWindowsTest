import itertools


class Account(object):
    accounts = []
    _idCounter = itertools.count()
    separator = "-" * 25

    def __init__(self, lastName: str, firstName: str, balance: int):
        assert balance > 0
        self._id = next(Account._idCounter)
        self._lastName = lastName
        self._firstName = firstName
        self._balance = balance
        Account.accounts.append(self)

    def get_id(self):
        return self._id

    def get_lastName(self):
        return self._lastName

    def set_lastName(self, lastName):
        self._lastName = lastName

    def get_firstName(self):
        return self._firstName

    def set_firstName(self, firstName):
        self._firstName = firstName

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        self._balance = balance

    @staticmethod
    def createAccount(firstName: str, lastName: str, balance: str):
        pass

    @staticmethod
    def deleteAccount(idAccount: int):
        pass

    @staticmethod
    def payement(pullout: bool, targetAccountId=0, amount=0):
        pass

    @staticmethod
    def transfert():
        pass

    @staticmethod
    def viewAllJsonAccounts():
        pass

    @staticmethod
    def viewAllAccounts():
        pass

    @staticmethod
    def checkAccountId(Id: int):
        pass

    def __str__(self) -> str:
        return f'id: {self.get_id()} \nlastName: {self.get_lastName()} \nfirstName: {self.get_firstName()} \nbalance: {self.get_balance()} \n'
