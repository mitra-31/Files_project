import getpass
class User:

    def __init__(self):
        pass

    def login(self,E_user):
        E_password = getpass.getpass("Password :")
        user = open('users/user.txt','r')
        username,password = user.readline().split("&")[:-2]
        if username == E_user and password == E_password:
            print("Successfull logged in")
        else:
            return "Unsuccessfull Try again"

    def add_user(self):
        username = input("Username : ")
        password = getpass.getpass("Password :")
        user = open('user/user.txt','a+')
        user.write(username+"&"+password+"&"+False+"&")
        user.close()
        print("Successfully User added")

    
