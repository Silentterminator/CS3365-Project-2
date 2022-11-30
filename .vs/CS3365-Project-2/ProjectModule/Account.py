class Account:
    def __init__(self, name, email, phone, address, password):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.password = password

    def createAccount(self):
        print(f'creating account for {self.name}')
        #code for creating account

    def logIn(self):
        print("logging in")
        #code for logging in

    def logOut(self):
        print("logging out")
        #code for logging out


class UserAccount(Account):
    pass


class AdminAccount(Account):
    def statusReport(self):
        print("status report")
        #code for status report

    def manageShows(self):
        print("manage shows")
        #code for managing shows
