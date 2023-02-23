from myBank.repository.dataBase import bdd


def createDB():
    con = bdd.cursor()
    con.execute(
        "CREATE TABLE IF NOT EXISTS users ("
        " id INTEGER PRIMARY KEY AUTOINCREMENT,"
        " username TEXT NOT NULL,"
        " userPwd TEXT NOT NULL)"
    )
    con.execute(
        "CREATE TABLE IF NOT EXISTS accounts ("
        " id INTEGER PRIMARY KEY AUTOINCREMENT,"
        " lastName TEXT NOT NULL,"
        " firstName TEXT NOT NULL,"
        " balance INTEGER)"
    )
    con.close()


def addUserDB(userName: str, userPwd: str):
    values = [(userName, userPwd)]
    for value in values:
        con = bdd.cursor()
        con.execute("INSERT INTO users (username, userPwd) VALUES (?, ?)", value)
        con.close()


def addAccountDB(lastName: str, firstName: str, balance: int):
    values = [(lastName, firstName, balance)]
    for value in values:
        con = bdd.cursor()
        con.execute(
            "INSERT INTO accounts (lastName, firstName, balance) VALUES (?, ?, ?)",
            value,
        )
        con.close()


def delUserDB(*userId: int):
    con = bdd.cursor()
    con.execute("DELETE FROM users WHERE id = ?", userId)
    con.close()


def delAccountDB(*accountId: int):
    con = bdd.cursor()
    con.execute("DELETE FROM accounts WHERE id = ?", accountId)
    con.close()


def selectAllUsers():
    con = bdd.cursor()
    users = con.execute("SELECT * FROM users")
    if users:
        return users


def selectAllAccounts():
    con = bdd.cursor()
    accounts = con.execute("SELECT * FROM accounts")
    if accounts:
        return accounts


def selectByUserName(*userName: str):
    con = bdd.cursor()
    users = con.execute("SELECT * FROM users WHERE username = ?", userName)
    if users:
        return users


def selectByAccountId(*accountId: int):
    con = bdd.cursor()
    accounts = con.execute("SELECT * FROM accounts WHERE id = ?", accountId)
    if accounts:
        return accounts


def selectByUserId(*userId: int):
    con = bdd.cursor()
    users = con.execute("SELECT * FROM users WHERE id = ?", userId)
    if users:
        return users


def selectByUserNameAndPwd(userName: str, userPwd: str):
    con = bdd.cursor()
    user = con.execute(
        "SELECT * FROM users WHERE username= ? AND userPwd = ?", (userName, userPwd)
    )
    if user:
        return user
