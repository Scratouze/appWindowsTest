from myBank.Controller import UserController
from myBank.model.CheckingAccount import CheckingAccount


def myBank(userName):
    print(
        f"{CheckingAccount.separator}\n{CheckingAccount.separator}\nBienvenue {userName} sur la gestion myBank \n{CheckingAccount.separator} "
        f"\n{CheckingAccount.separator}"
    )
    menu = (
        "Choisissez parmi les 5 options suivantes \n"
        "1: Afficher tout les comptes \n"
        "2: Créer un compte  \n"
        "3: Supprimer un compte \n"
        "4: Effectuer un versement sur un compte \n"
        "5: Effectuer un prélèvement depuis un compte \n"
        "6: Effectuer un virement entre 2 comptes \n"
        "7: Quitter \n"
        "Votre choix -> "
    )

    menu_choice = ["1", "2", "3", "4", "5", "6", "7"]
    while True:
        user_choice = ""
        while user_choice not in menu_choice:
            user_choice = input(menu)
            if user_choice not in menu_choice:
                print("\n Veuillez choisir une option valide")
                print(CheckingAccount.separator)
            else:
                print(CheckingAccount.separator)
                match user_choice:
                    case "1":
                        CheckingAccount.viewAllAccounts()
                    case "2":
                        CheckingAccount.createAccount()
                    case "3":
                        CheckingAccount.deleteAccount()
                    case "4":
                        CheckingAccount.payement(False)
                    case "5":
                        CheckingAccount.payement(True)
                    case "6":
                        CheckingAccount.transfert()
                    case "7":
                        print(
                            f"Vous quittez la gestion des comptes !\n{CheckingAccount.separator}"
                        )
                        UserController.Connection()


def createValidAccount(
    account_first_name_entry, account_last_name_entry, account_balance_entry
):
    if CheckingAccount.createAccount(
        account_first_name_entry.get(),
        account_last_name_entry.get(),
        account_balance_entry.get(),
    ):
        from utils.appController import accountMainMenu

        accountMainMenu()


# MonCompte = CheckingAccount("Thomas", "Berta", 1000)
# MonCompte2 = CheckingAccount("Alex", "Tom", 1500)
