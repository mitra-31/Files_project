

useage = '''

Usage:
    main.py user <username>
    main.py add <item> <price> <catogery>
    main.py del <item> <catogery>
    main.py update <item> <price> <catogery>
    main.py menu (--a|--r <catogery>)
    main.py user -login
    main.py basket <item>
    main.py total
    main.py order

Helper:
    <catogery> = 's' : 'STARTERS',
                'b' : "BIRIYANIS",
                't' : "THALIS"

Options:
    -l,--list  list all.
    -h,--help  show commands.
'''

catogery = {
    's' : 'STARTERS',
    'b' : "BIRIYANIS",
    't' : "THALIS"
}

from docopt import docopt
from menu.file import *
from users.user import *


cred = open('users/user.txt',"r")
username,password,status = cred.readline().split("&")[:-1]
cred.close()

args = docopt(useage)


if args['user']:
    User().login(args['<username>'])
elif args['add']:
    item = args['<item>']
    price = args['<price>']
    cat= args['<catogery>']
    Menu().add_items(item,price,catogery[cat])
elif args['del']:
    item = args['<item>']
    cat = args["<catogery>"]
    Menu().modify_items('delete',item,cat)
elif args['update']:
    item = args['<item>']
    price = args['<price>']
    cat = args["<catogery>"]
    Menu().modify_items('update',item,price,cat)
elif args['menu']:
    item = args['<item>']
    price = args['<price>']
    cat = args['<catogery>']
    if args['--r']:
        Menu().display(catogery[cat])
    elif args['--a']:
        Menu().display()
    elif args['--help']:
        print(useage)
elif args[':q']:
    exit()