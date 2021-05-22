useage = '''

Usage:
    main.py add <item> <price> <catogery>
    main.py modify <case> <item> [price] <catogery>
    main.py menu (--a|--r <catogery>)

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


args = docopt(useage)
if args['add']:
    item = args['<item>']
    price = args['<price>']
    cat= args['<catogery>']
    Menu().add_items(item,price,catogery[cat])
elif args['modify']:
    item = args['<item>']
    price = args['<price>']
    cat = args["<catogery>"]
    case = args["<case>"]
    #print(item,price,cat,case)
    Menu().modify_items(case,item,price,cat)
elif args['menu']:
    case = args["<case>"]
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