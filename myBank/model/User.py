import itertools
import tkinter
from tkinter.messagebox import showwarning
from myBank.repository.dataBase import bdd
from myBank.repository.dataBase_util import (
    addUserDB,
    selectAllUsers,
    selectByUserName,
    delUserDB,
    selectByUserId,
)


class User:
    _idCounter = itertools.count()

    def __init__(self, userName: str, userPwd: str):
        self._id = next(User._idCounter)
        self._userName = userName
        self._pwd = userPwd

    def get_id(self):
        return self._id

    def set_userName(self, userName):
        self._userName = userName

    def get_userName(self):
        return self._userName

    def set_pwd(self, pwd):
        self._pwd = pwd

    def get_pwd(self):
        return self._pwd

    @staticmethod
    def createUser(userName: str, userPwd: str):
        from myBank.Controller.UserController import password_check

        if userName == "" or userPwd == "":
            tkinter.messagebox.showerror(
                "Champs non complets", "Les champs ne sont pas complets"
            )
        elif len(userName) <= 2 or len(userName) >= 19 or userName.isdigit():
            tkinter.messagebox.showerror(
                "Erreur utilisateur",
                "Entrez un nom d'utilisateur entre 3 et 20 caractères contenant au moins 1 "
                "lettre",
            )

        elif len(userPwd) == 0:
            tkinter.messagebox.showerror(
                "Erreur mot de passe", "Veuillez entrer un mot de passe"
            )

        elif not password_check(userPwd):
            tkinter.messagebox.showerror(
                "Erreur mot de passe",
                "Veuillez entrez un mot de passe contenant au moins un chiffre, une lettre "
                "minuscule "
                ", une lettre majuscule ainsi qu'1 caractère spécial ('$@#%+-*!?')",
            )

        elif User.checkUserName(userName):
            tkinter.messagebox.showerror(
                "Doublon utilisateur",
                "Ce nom d'utilisateur existe déjà, veuillez entrez un autre nom d'utilisateur",
            )
        else:
            try:
                addUserDB(userName.lower(), userPwd)
                bdd.commit()
            finally:
                tkinter.messagebox.showinfo(
                    "Utilisateur créé", "Vous pouvez retourner l'accueil"
                )
                return True

    @staticmethod
    def deleteUser(idUser: int) -> None:
        if not User.checkUsers():
            pass
        else:
            users = selectByUserId(idUser)
            for user in users:
                if user:
                    userName = user[1]
                    try:
                        delUserDB(idUser)
                        bdd.commit()
                    finally:
                        tkinter.messagebox.showinfo(
                            "Utilisateur " + userName,
                            "Utilisateur " + userName + " supprimé",
                        )
                        pass

    @staticmethod
    def checkUserId(userId: int):
        users = selectByUserId(userId)
        for user in users:
            if user.get_id() == userId:
                return user

    @staticmethod
    def checkUserName(userName: str):
        results = selectByUserName(userName)
        for user in results:
            if user and user[1] == userName:
                return user

    @staticmethod
    def checkUsers():
        users = selectAllUsers().fetchall()
        if len(users) == 0:
            tkinter.messagebox.showerror("Il n'y a pas d'utilisateur créé")
        else:
            return users

    @staticmethod
    def checkUser(pwd: str, userName: str):
        users = selectByUserName(userName)
        for user in users:
            if user.get_pwd() == pwd and user.get_userName() == userName:
                return user


def __str__(self) -> str:
    return f"id: {self.get_id()} \nlastName: {self.get_userName()} \nfirstName: {self.get_pwd()}"
