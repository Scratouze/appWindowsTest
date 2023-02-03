from tkinter import *
from myBank.Controller import UserController
from myBank.Controller.AccountController import createValidAccount
from myBank.Controller.UserController import createValidUser
from myBank.model.CheckingAccount import CheckingAccount
from myBank.repository.dataBase_util import selectAllUsers, selectAllAccounts
from utils.utils import two_funcs


def userMainMenu():
    first_frame.destroy()
    auth_frame = Frame(container, bg='#1D4291')
    auth_frame.pack(expand=YES)
    auth_label_title = Label(master=auth_frame, text="Bienvenue sur l'interface de connexion", background='#1D4291',
                             foreground='white',
                             font=('Courrier', 20))
    auth_label_title.pack(expand=YES)

    select_auth_frame = Frame(auth_frame, bg='#1D4291')

    connection_button = Button(select_auth_frame, text="Connexion", background='#1D4291', foreground='white',
                               font=('Courrier', 15),
                               command=user_connection)
    connection_button.pack(pady=5)
    connection_button.config(width=30)

    all_users_button = Button(select_auth_frame, text="Afficher tout les utilisateurs", background='#1D4291',
                              foreground='white',
                              font=('Courrier', 15),
                              command=view_all_users)
    all_users_button.pack(pady=5)
    all_users_button.config(width=30)

    create_user_button = Button(select_auth_frame, text="Créer un utilisateur", background='#1D4291',
                                foreground='white',
                                font=('Courrier', 15),
                                command=create_user)
    create_user_button.pack(pady=5)
    create_user_button.config(width=30)

    exit_button = Button(select_auth_frame, text="Quitter", background='#1D4291',
                         foreground='white',
                         font=('Courrier', 15),
                         command=closeApp)
    exit_button.pack(pady=5)
    exit_button.config(width=30)
    auth_frame.pack(expand=YES)
    select_auth_frame.pack(expand=YES, padx=50, pady=50)


def userHome():
    for child in container.winfo_children():
        child.destroy()
    userMainMenu()


def closeApp():
    for child in container.winfo_children():
        child.destroy()
    container.destroy()


def view_all_users():
    for child in container.winfo_children():
        child.forget()
    users_frame = Frame(container, bg='#1D4291')

    home_button = Button(container, text="Retour", background='#1D4291',
                         foreground='white',
                         font=('Courrier', 10),
                         command=userHome)
    home_button.pack(side=BOTTOM)
    home_button.config(width=15)

    users_frame.pack(expand=YES)
    users_frame_title = Label(master=users_frame, text="Liste des utilisateurs enregistrés", background='#1D4291',
                              foreground='white',
                              font=('Courrier', 20))

    users_frame_title.pack(expand=YES)
    users_list_frame = Frame(users_frame, bg='#1D4291')
    users_list_frame.pack(pady=10)
    from myBank.model.User import User
    users = selectAllUsers().fetchall()
    if not users:
        user_error_label = Label(master=users_list_frame, text="Pas d'utilisateur créé", background='#1D4291',
                                 foreground='white',
                                 font=('Courrier', 15))
        user_error_label.pack(pady=5, side=LEFT)
        user_error_label.config(width=30)
    else:
        for user in users:
            userId: str = str(user[0])
            username: str = user[1]

            user_frame = Frame(users_frame, bg='#1D4291')

            user_info_label = Label(master=user_frame, text=username, background='#1D4291', foreground='white',
                                    font=('Courrier', 15))
            user_info_label.pack(pady=5, side=LEFT)
            user_info_label.config(width=30)

            user_delete_button = Button(user_frame, text="Supprimer", background='#1D4291', foreground='white',
                                        font=('Courrier', 10),
                                        command=two_funcs((lambda: User.deleteUser(int(userId))), userHome))
            user_delete_button.pack(pady=5, side=RIGHT)
            user_delete_button.config(width=30)

            user_frame.pack(expand=YES)


def create_account():
    for child in container.winfo_children():
        child.forget()
    ################################################################
    new_account_frame = Frame(container, bg='#1D4291')

    home_button = Button(container, text="Retour", background='#1D4291', foreground='white',
                         font=('Courrier', 10),
                         command=userHome)
    home_button.pack(side=BOTTOM)
    home_button.config(width=15)
    new_account_frame.pack(expand=YES)
    ################################################################
    account_frame_title = Label(master=new_account_frame, text="Nouveau compte", background='#1D4291',
                                foreground='white',
                                font=('Courrier', 20))
    account_frame_title.pack()
    ################################################################
    account_asset_frame = Frame(new_account_frame, bg='#1D4291')
    ################################
    account_first_name = Frame(account_asset_frame, bg='#1D4291')
    account_first_name_label = Label(master=account_first_name, text="Prénom", background='#1D4291', foreground='white',
                                     font=('Courrier', 20))
    account_first_name_entry = Entry(master=account_first_name, background='#1D4291', foreground='white',
                                     font=('Courrier', 20))
    ################################################################
    account_last_name = Frame(account_asset_frame, bg='#1D4291')
    account_last_name_label = Label(master=account_last_name, text="Nom", background='#1D4291', foreground='white',
                                    font=('Courrier', 20))
    account_last_name_entry = Entry(master=account_last_name, background='#1D4291', foreground='white',
                                    font=('Courrier', 20))
    ################################################################
    account_balance = Frame(account_asset_frame, bg='#1D4291')
    account_balance_label = Label(master=account_balance, text="Solde actuel", background='#1D4291', foreground='white',
                                  font=('Courrier', 20))
    account_balance_entry = Entry(master=account_balance, background='#1D4291', foreground='white',
                                  font=('Courrier', 20))
    ################################################################

    account_first_name.pack()
    account_last_name.pack(pady=10)
    account_balance.pack(pady=10)
    ###################
    account_first_name_label.pack(side=LEFT)
    account_first_name_entry.pack(after=account_first_name_label)
    account_first_name_label.config(width=30)
    account_first_name_entry.config(width=30)
    ###################
    account_last_name_label.pack(side=LEFT)
    account_last_name_entry.pack(after=account_last_name_label)
    account_last_name_label.config(width=30)
    account_last_name_entry.config(width=30)
    ###################
    account_balance_label.pack(side=LEFT)
    account_balance_entry.pack(after=account_balance_label)
    account_balance_label.config(width=30)
    account_balance_entry.config(width=30)
    ###################
    account_asset_frame.pack(expand=YES, padx=50, pady=50)

    create_account_button = Button(account_asset_frame, text="Créer", background='#1D4291', foreground='white',
                                   font=('Courrier', 10),
                                   command=lambda: [
                                       createValidAccount(account_first_name_entry, account_last_name_entry,
                                                          account_balance_entry)])

    create_account_button.pack(side=BOTTOM)
    create_account_button.config(width=15)


def create_user():
    for child in container.winfo_children():
        child.forget()
    ################################################################
    new_user_frame = Frame(container, bg='#1D4291')

    home_button = Button(container, text="Retour", background='#1D4291', foreground='white',
                         font=('Courrier', 10),
                         command=userHome)
    home_button.pack(side=BOTTOM)
    home_button.config(width=15)
    new_user_frame.pack(expand=YES)
    ################################################################
    user_frame_title = Label(master=new_user_frame, text="Nouvel utilisateur", background='#1D4291', foreground='white',
                             font=('Courrier', 20))
    user_frame_title.pack()
    ################################################################
    user_asset_frame = Frame(new_user_frame, bg='#1D4291')

    user_name = Frame(user_asset_frame, bg='#1D4291')
    user_name_label = Label(master=user_name, text="Nom d'utilisateur", background='#1D4291', foreground='white',
                            font=('Courrier', 20))
    user_name_entry = Entry(master=user_name, background='#1D4291', foreground='white',
                            font=('Courrier', 20))

    ################################################################
    user_pwd = Frame(user_asset_frame, bg='#1D4291')
    user_pwd_label = Label(master=user_pwd, text="Mot de passe", background='#1D4291', foreground='white',
                           font=('Courrier', 20))
    user_pwd_entry = Entry(master=user_pwd, background='#1D4291', foreground='white',
                           font=('Courrier', 20), show="*")
    ################################################################
    user_name.pack()
    user_pwd.pack(pady=10)
    ###################
    user_name_label.pack(side=LEFT)
    user_name_entry.pack(after=user_name_label)
    user_name_label.config(width=30)
    user_name_entry.config(width=30)
    ###################
    user_pwd_label.pack(side=LEFT)
    user_pwd_entry.pack(after=user_pwd_label)
    user_pwd_label.config(width=30)
    user_pwd_entry.config(width=30)
    ###################
    user_asset_frame.pack(expand=YES, padx=50, pady=50)

    create_user_button = Button(user_asset_frame, text="Créer", background='#1D4291', foreground='white',
                                font=('Courrier', 10),
                                command=lambda: [createValidUser(user_name_entry, user_pwd_entry)])

    create_user_button.pack(side=BOTTOM)
    create_user_button.config(width=15)


def user_connection():
    for child in container.winfo_children():
        child.forget()
    connection_frame = Frame(container, bg='#1D4291')

    home_button = Button(container, text="Retour", background='#1D4291', foreground='white',
                         font=('Courrier', 10),
                         command=userHome)
    home_button.pack(side=BOTTOM)
    home_button.config(width=15)

    connection_frame.pack(expand=YES)
    users_frame_title = Label(master=connection_frame, text="Connexion", background='#1D4291', foreground='white',
                              font=('Courrier', 20))

    users_frame_title.pack(expand=YES)
    users_connection_frame = Frame(connection_frame, bg='#1D4291')
    users_connection_frame.pack(pady=10)
    users = selectAllUsers().fetchall()
    if not users:
        user_error_label = Label(master=users_connection_frame, text="Pas d'utilisateur créé", background='#1D4291',
                                 foreground='white',
                                 font=('Courrier', 15))
        user_error_label.pack(pady=5, side=LEFT)
        user_error_label.config(width=30)
    else:
        pass
        ################################################################
        user_asset_frame = Frame(users_connection_frame, bg='#1D4291')

        user_name = Frame(user_asset_frame, bg='#1D4291')
        user_name_label = Label(master=user_name, text="Nom d'utilisateur", background='#1D4291', foreground='white',
                                font=('Courrier', 20))

        user_name_entry = Entry(master=user_name, background='#1D4291', foreground='white',
                                font=('Courrier', 20))
        ################################################################
        user_pwd = Frame(user_asset_frame, bg='#1D4291')
        user_pwd_label = Label(master=user_pwd, text="Mot de passe", background='#1D4291', foreground='white',
                               font=('Courrier', 20))
        user_pwd_entry = Entry(master=user_pwd, background='#1D4291', foreground='white',
                               font=('Courrier', 20), show="*")
        user_name.pack()
        user_pwd.pack(pady=10)
        ###################
        user_name_label.pack(side=LEFT)
        user_name_entry.pack(after=user_name_label)
        user_name_label.config(width=30)
        user_name_entry.config(width=30)
        ###################
        user_pwd_label.pack(side=LEFT)
        user_pwd_entry.pack(after=user_pwd_label)
        user_pwd_label.config(width=30)
        user_pwd_entry.config(width=30)
        ###################
        user_asset_frame.pack(expand=YES, padx=50, pady=50)

        connect_user_button = Button(user_asset_frame, text="Connexion", background='#1D4291', foreground='white',
                                     font=('Courrier', 10),
                                     command=lambda: [
                                         UserController.userConnect(user_name_entry.get(), user_pwd_entry.get())])
        connect_user_button.pack(side=BOTTOM)
        connect_user_button.config(width=15)


def accountMainMenu():
    for child in container.winfo_children():
        child.forget()
    accounts_frame = Frame(container, bg='#1D4291')
    accounts_frame.pack(expand=YES)
    accounts_label_title = Label(master=accounts_frame, text="Bienvenue sur l'interface de Gestion des comptes",
                                 background='#1D4291',
                                 foreground='white',
                                 font=('Courrier', 20))
    accounts_label_title.pack(expand=YES)

    select_account_menu_frame = Frame(accounts_frame, bg='#1D4291')

    connection_button = Button(select_account_menu_frame, text="Voir tout les comptes", background='#1D4291',
                               foreground='white',
                               font=('Courrier', 15),
                               command=view_all_accounts)
    connection_button.pack(pady=5)
    connection_button.config(width=30)

    create_account_button = Button(select_account_menu_frame, text="Créer un compte", background='#1D4291',
                                   foreground='white',
                                   font=('Courrier', 15),
                                   command=create_account)
    create_account_button.pack(pady=5)
    create_account_button.config(width=30)

    exit_button = Button(select_account_menu_frame, text="Quitter", background='#1D4291',
                         foreground='white',
                         font=('Courrier', 15),
                         command=userHome)
    exit_button.pack(pady=5)
    exit_button.config(width=30)
    select_account_menu_frame.pack(expand=YES, padx=50, pady=50)


def view_all_accounts():
    for child in container.winfo_children():
        child.forget()
    accounts_frame = Frame(container, bg='#1D4291')

    home_button = Button(container, text="Retour", background='#1D4291',
                         foreground='white',
                         font=('Courrier', 10),
                         command=accountMainMenu)
    home_button.pack(side=BOTTOM)
    home_button.config(width=15)

    accounts_frame.pack(expand=YES)
    accounts_frame_title = Label(master=accounts_frame, text="Liste des comptes enregistrés", background='#1D4291',
                                 foreground='white',
                                 font=('Courrier', 20))

    accounts_frame_title.pack(expand=YES)
    accounts_list_frame = Frame(accounts_frame, bg='#1D4291')
    accounts_list_frame.pack(pady=10)

    accounts = selectAllAccounts().fetchall()
    if not accounts:
        user_error_label = Label(master=accounts_list_frame, text="Pas de compte créé", background='#1D4291',
                                 foreground='white',
                                 font=('Courrier', 15))
        user_error_label.pack(pady=5, side=LEFT)
        user_error_label.config(width=30)
    else:
        for account in accounts:
            accountId: str = str(account[0])
            accountLastName: str = account[1]
            accountFirstName: str = account[2]
            accountBalance: int = account[3]

            account_frame = Frame(accounts_frame, bg='#1D4291')

            account_info_label = Label(master=account_frame,
                                       text=accountId + " -> " + accountLastName + " " + accountFirstName + " -- " + str(
                                           accountBalance) + " €",
                                       background='#1D4291', foreground='white',
                                       font=('Courrier', 15))
            account_info_label.pack(pady=5, side=LEFT)
            account_info_label.config(width=30)

            user_delete_button = Button(account_frame, text="Supprimer", background='#1D4291', foreground='white',
                                        font=('Courrier', 10),
                                        command=two_funcs((lambda: CheckingAccount.deleteAccount(int(accountId))),
                                                          accountMainMenu))
            user_delete_button.pack(pady=5, side=RIGHT)
            user_delete_button.config(width=30)

            account_frame.pack(expand=YES)


def userMasterWindow():
    # personnalisation fenêtre de base
    container = Tk()
    container.title("My bank")
    container.geometry("1080x720")
    container.minsize(680, 440)
    container.iconbitmap("assets/test.ico")
    container.config(background='#1D4291')

    # Page intro
    first_frame = Frame(container, bg='#1D4291')
    label_title = Label(master=first_frame, text="Bienvenue sur MyBank", background='#1D4291', foreground='white',
                        font=('Courrier', 40))
    label_title.pack(expand=YES)
    label_subtitle = Label(master=first_frame, text="Votre interface de gestion de comptes", background='#1D4291',
                           foreground='white',
                           font=('Courrier', 20))
    label_subtitle.pack(expand=YES)

    start_button = Button(first_frame, text="Démarrer l'application", background='#1D4291', foreground='white',
                          font=('Courrier', 15),
                          command=userMainMenu)
    start_button.pack(pady=25)

    first_frame.pack(expand=YES)

    return container, first_frame


container, first_frame = userMasterWindow()
