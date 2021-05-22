

with open('test1.txt', 'r') as f:
    data = f.readlines()
f.close()


menu = {
    'STARTERS': {},
    'THALIS': {},
    'BIRIYANIS': {},
    'DESSERTS': {}
}
for line in data:
    try: 
        cat,item,price = line.split(":")[:-1] 
        menu[cat].update({item:price})
    except ValueError: # To encounter any empty space
        continue
    except KeyError:
        print('Would you like to add new catogery?(y/n)')
        poll = input(">>")
        if poll == "y":
            menu.update({cat:{}})
            menu[cat].update({item:price})
        else:
            continue
print(menu)

