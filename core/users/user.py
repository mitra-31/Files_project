import getpass


def changeStatus(filename,username,password):
    currentFile = open("./src/files/"+filename,'w')
    currentFile.write(username+":"+password+":"+str(True))
    currentFile.close()



class User:

    def __init__(self):
        pass

    def login(self,E_user):
        E_password = getpass.getpass("Password :")
        user = open('/src/files/user.txt','r')
        username,password = user.readline().split("&")[:-2]
        if username == E_user and password == E_password:
            changeStatus('admin.txt',username,password)
            print("Successfull logged in")
        else:
            return "Unsuccessfull Try again"

    def add_user(self):
        username = input("Username : ")
        password = getpass.getpass("Password :")
        user = open('/src/files/user.txt','a+')
        user.write(username+"&"+password+"&"+False+"&")
        user.close()
        print("Successfully User added")
        
class Admin:
    
    def __init__(self):
       pass
    def login(self,adminName):
        E_password = getpass.getpass("Password :")
        user = open('./src/files/admin.txt','r')
        username,password = user.readline().split(":")[0:2]
        if username == adminName and password == E_password:
            changeStatus('admin.txt',username,password)
            print("Successfull logged in")
        else:
            print("Unsuccessfull Try again")

    
    def changePassword(self,newPassword):
        currentFile = open("./src/files/admin.txt",'w+').readlines()
        currentAdmin,currentAdminStatus = currentFile.split(":")[0:2:2]
        if currentAdminStatus:
            currentFile.write(currentAdmin+":"+newPassword+":"+currentAdminStatus)
        currentFile.close()
        
    def logout(self):
        currentFile = open("./src/files/admin.txt",'w')
        currentAdmin,password,currentAdminStatus = currentFile.split(":")
        if currentAdminStatus:
            currentFile.write(currentAdmin+":"+password+":"+"False")
        currentFile.close()