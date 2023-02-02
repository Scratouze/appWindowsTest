import tkinter
from myBank.model.User import User
from myBank.repository.dataBase_util import selectByUserNameAndPwd


def password_check(pwd) -> bool:
    SpecialChar = ['$', '@', '#', '%', '+', '-', '*', '!', '?']
    result = True
    if not any(char.isdigit() for char in pwd):
        result = False
    if not any(char.isupper() for char in pwd):
        result = False
    if not any(char.islower() for char in pwd):
        result = False
    if not any(char in SpecialChar for char in pwd):
        result = False
    if result:
        return result


def createValidUser(user_name_entry, user_pwd_entry):
    if User.createUser(user_name_entry.get(), user_pwd_entry.get()):
        from utils.appController import userHome
        userHome()


def userConnect(userName: str, userPwd: str):
    if not selectByUserNameAndPwd(userName, userPwd).fetchall():
        tkinter.messagebox.showerror("Erreur de connexion", "Identifiant ou mot de passe incorrect")
        from utils.appController import user_connection
        user_connection()
    else:
        tkinter.messagebox.showinfo("Connexion", "Vous allez arriver sur l'interface de gestion MyBank")
        from utils.appController import accountMainMenu
        accountMainMenu()
