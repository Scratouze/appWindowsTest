import json
import tkinter
from tkinter.messagebox import showerror

from myBank.model.Account import Account
from myBank.repository.dataBase import bdd
from myBank.repository.dataBase_util import selectAllAccounts, selectByAccountId, delAccountDB, addAccountDB


class CheckingAccount(Account):

    def __init__(self, lastName: str, firstName: str, balance: int):
        assert balance > 0, "Le solde d'un nouveau compte doit être positif"
        super().__init__(lastName, firstName, balance)

    def get_id(self):
        return super().get_id()

    def get_lastName(self):
        return super().get_lastName()

    def set_lastName(self, lastName):
        super().set_lastName(lastName)

    def get_firstName(self):
        return super().get_firstName()

    def set_firstName(self, firstName):
        super().set_firstName(firstName)

    def get_balance(self):
        return super().get_balance()

    def set_balance(self, balance):
        super().set_balance(balance)

    @staticmethod
    def createAccount(firstName: str, lastName: str, balance: str):
        if firstName == "" or lastName == "" or balance == "":
            tkinter.messagebox.showerror("Champs non complets",
                                         "Les champs ne sont pas complets")
        elif len(firstName) <= 2 or len(firstName) >= 19 or len(lastName) <= 2 or len(
                lastName) >= 19 or firstName.isdigit() or lastName.isdigit():
            tkinter.messagebox.showerror("Erreur de saisie",
                                         "Entrez un prénom et un nom entre 3 et 20 caractères")

        elif len(balance) == 0 or balance == 0:
            tkinter.messagebox.showerror("Erreur de saisie", "Vous ne pouvez pas créer un compte à 0 €")
        elif not balance.isdigit():
            tkinter.messagebox.showerror("Erreur de saisie",
                                         "Le solde doit-être en caractères alphanumériques")
        else:
            try:
                balance = int(balance)
                addAccountDB(firstName, lastName, balance)
                bdd.commit()
            finally:
                tkinter.messagebox.showinfo("Compte créé",
                                            "Vous allez retourner à l'accueil")
                return True

    @staticmethod
    def deleteAccount(idAccount: int):
        if not CheckingAccount.checkAccounts():
            pass
        else:
            users = selectByAccountId(idAccount)
            for account in users:
                if account:
                    accountFirstName = account[1]
                    accountLastName = account[2]
                    try:
                        delAccountDB(idAccount)
                        bdd.commit()
                    finally:
                        tkinter.messagebox.showinfo("Compte Id " + str(idAccount),
                                                    "Le compte de " + accountFirstName + accountLastName + "a été "
                                                                                                           "supprimé")
                        pass

    @staticmethod
    def checkAccounts():
        accounts = selectAllAccounts().fetchall()
        if len(accounts) == 0:
            tkinter.messagebox.showerror("Il n'y a pas de compte créé")
        else:
            return accounts

    @staticmethod
    def payement(pullout: bool, targetAccountId=0, amount=0):
        action1 = "vers" if not pullout else "depuis"
        action2 = "versement" if not pullout else "prélèvement"
        if not targetAccountId and not amount:
            targetAccountId: int = int(input(f"{action1} quel compte souhaitez vous effectuer un {action2} (id): "))
            amount = input(f"De quel montant est votre {action2} : ")
        amount = -int(amount) if pullout else int(amount)
        if not CheckingAccount.checkAccountId(targetAccountId):
            print(
                f"{CheckingAccount.separator}Le compte {action1} lequel vous essayer d'effectuer ce {action2}"
                f" n'existe pas")
            pass
        else:
            target = CheckingAccount.checkAccountId(int(targetAccountId))
            action = "dépôt" if (amount > 0) else "retrait"
            if target.get_balance() > 0:
                target.set_balance((target.get_balance() + amount))
                if target.get_balance() < 0:
                    print(
                        f"\nLe compte de {target.get_lastName()} {target.get_firstName()} n'a pas les fonds "
                        f"suffisants, le compte "
                        f"va être à découvert de {target.get_balance()} €")
                print(
                    f"{CheckingAccount.separator}\nVous avez effectué un {action} de {amount} € sur le compte de"
                    f"{target.get_lastName()} {target.get_firstName()}")
            else:
                print(
                    f"{CheckingAccount.separator}\nLe compte de {target.get_lastName()} {target.get_firstName()} est "
                    f"débiteur de {target.get_balance()} €, vous ne pouvez pas faire de {action}")

    @staticmethod
    def transfert():
        originAccountId: int = int(input("Depuis quel compte souhaitez vous effectuer un virement (id): "))
        originAccount: CheckingAccount = CheckingAccount.checkAccountId(originAccountId)
        if not originAccount:
            print(f"Le compte depuis lequel vous essayer d'effectuer ce virement n'existe pas")
            pass
        else:
            targetAccountId: int = int(input("Vers quel compte souhaitez vous effectuer un virement (id): "))
            targetAccount: CheckingAccount = CheckingAccount.checkAccountId(targetAccountId)
            if not targetAccount:
                print(f"Le compte vers lequel vous essayer d'effectuer ce virement n'existe pas")
                pass
            else:
                amount = int(input("De quel montant est votre virement : "))
                originAccount.payement(True, originAccountId, amount)
                targetAccount.payement(False, targetAccountId, amount)

    @staticmethod
    def viewAllJsonAccounts() -> json:
        jsonResult = []
        for account in CheckingAccount.accounts:
            accountDict = {'id': account.get_id(), 'lastName': account.get_lastName(),
                           'firstName': account.get_firstName(),
                           'balance': account.get_balance()}
            jsonAccount = json.dumps(accountDict)
            jsonResult.append(jsonAccount)
        print(CheckingAccount.separator)
        print(jsonResult)
        print(CheckingAccount.separator)

    @staticmethod
    def selectAllAccounts():
        result = ""
        if not CheckingAccount.accounts:
            print("Il n'y a pas de compte créé")
        else:
            for account in CheckingAccount.accounts:
                result += f"id: {account.get_id()}\nlastName: {account.get_lastName()}\nfirstName: " \
                          f"{account.get_firstName()}\nbalance: {account.get_balance()} €\n{CheckingAccount.separator} \n "
            print(result)

    @staticmethod
    def checkAccountId(accountId: int):
        accounts = selectByAccountId(accountId)
        for account in accounts:
            if account.get_id() == accountId:
                return account

    def __str__(self) -> str:
        return super().__str__()
