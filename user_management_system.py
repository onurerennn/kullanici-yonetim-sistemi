import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        self.loadUser()

    def loadUser(self):
        if os.path.exists("users.json"):
            with open("users.json", "r", encoding="utf-8") as file:
                users = json.load(file)
                for user in users:
                    newUser=User(username=user["username"],password=user["password"],email=["email"])
                    
                    self.users.append(newUser)
            print(self.users) 
    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print("User created")

    def login(self,username,password):
            for user in self.users:
                if user.username==username and user.password==password:
                    self.isLoggedIn=True
                    self.currentUser=user
                    print("logged in")
                    break
    def logout(self):
            self.isLoggedIn=False
            self.currentUser={}
            print("exit")

    def identity(self):
            if self.isLoggedIn:
                print(f"username: {self.currentUser.username} ")
            else:
                print("not logged in")

        

    def savetoFile(self):
        user_list = [user.__dict__ for user in self.users]
        with open("users.json", "w") as file:
            json.dump(user_list, file, default=str, indent=2)


repository = UserRepository()

while True:
    print("Menu".center(50, '*'))
    secim = input("1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\n choice:")
    if secim == "5":
        break
    else:
        if secim == "1":
            # register
            username = input("username: ")
            password = input("password: ")
            email = input("email: ")
            user = User(username=username, password=password, email=email)
            repository.register(user)

        elif secim == "2":
            # login
            if repository.isLoggedIn:
                print("you are already logged in")
            else:
                username=input("username: ")
                password=input("password")
                repository.login(username,password)

        elif secim == "3":
            # logout
            repository.logout()

        elif secim == "4":
            # identity
            repository.identity()
            pass

        else:
            print("Wrong choice")
