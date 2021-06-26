
useage = '''

Usage:
    main.py a <username>
'''

catogery = {
    'a' : None,
    's' : 'STARTERS',
    'b' : "BIRIYANIS",
    't' : "THALIS"
}

from docopt import docopt
import core.menu.file as m
import core.users.user as user
import time


def admin_login():
    adminName,adminStatus = open("src/files/admin.txt",'r').readline().split(":")[0::2]
    return adminStatus





def Admin_Dashboard():
    menu = m.Menu() 
    if admin_login():
        while True:
            print("1. Add Item\n2. Update Item\n3. Delete Item\n4. Display Menu\n5. Exit")
            choice = int(input(">> "))

            if choice == 1:
                print("Enter item , price , catogery")
                item,price,cat = input().split()
                menu.add_items(item,price,catogery[cat])
            elif choice == 2:
                print("Enter item , price , catogery")
                item,price,cat = input().split()
                menu.modify_items('update',item,price,catogery[cat])
            elif choice == 3:
                print("Enter item , price , catogery")
                item,cat = input().split()
                menu.modify_items('delete',item,None,catogery[cat])
            elif choice == 4:
                print("All Items or Mention catogery\na - All\ns - starters\nb - biriyani")
                cat = input(">> ")
                menu.display(catogery[cat])
            elif choice == 5:
                print("Bye Admin")
                user.Admin().logout()
                time.sleep(1)
                exit()
            elif choice == 6:
                menu.getCurrentNumber()

            
args = docopt(useage)
if args["a"]:
    user.Admin().login(args['<username>'])
    Admin_Dashboard()
