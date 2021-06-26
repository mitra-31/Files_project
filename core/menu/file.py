from tabulate import tabulate
import os
import webbrowser



RS = "/-"
SEP = ":"
NEXT = "\n"


class Menu:

    def __init__(self):
        self.path = './src/files/Menu.txt'     #Holds the path of Menu file
        self.Menu = self.menu_content() #Store the content of file into self.Menu Var
        self.items = self.get_items()	#Store each type of item in JSON format
        self.currentNumber = self.getCurrentNumber()
        #print(self.items)
        self.create_file()
    
## This is fuction is used to update the self.menu each an class is called
    def menu_content(self):
        with open(self.path,"r") as menu:
            data = menu.readlines()
        return data

# This is fuction is used to update the self.items each an class is called
    def get_items(self):
	## This is the Starter template of menu card.
        items = {
            'STARTERS' :{},
            'THALIS' :{},
            'BIRIYANIS' :{},
            'DESSERTS' :{}
        }
	
	## Lets loop through each dish in menu.
        for dish in self.Menu:
            try: 
                idx,cat,item,price = dish.split(":")[:-1] 
                items[cat].update({item:price})
            except ValueError: # To encounter any empty space
                continue
        return items

    def getCurrentNumber(self):
        try:
            lastline = self.Menu[-1]
        except IndexError:
            return 0
        return int(lastline.split(":")[0])
    
# To create a Menu.txt Where all the content goes.
    def create_file(self):
        files = os.listdir('./src/files') ##this shows all the files present in menu dir
        if "Menu.txt" in files : ## If the file present inside menu dir lets no create it  
            return None
        with open(self.path,'w') as n: ## this methods helps to create a new file in cwd
            pass
        n.close()
        return "Created a new file"
    

    def add_items(self,item,price,catogery):
        if item in self.items[catogery].keys():
            return "Exists"
        file = open(self.path,"a+")
        item = " ".join(item.split("_"))
        currentNumber = self.currentNumber+1
        file.write(str(currentNumber)+SEP+catogery+SEP+item+SEP+price+SEP+NEXT)
        file.close()
        return "Successfull Added"


    def modify_items(self,case,item,UpdatedPrice=None,catogery=None):
        try:
            temp_file = open("./src/files/temp.txt","x")
        except FileExistsError:
            os.remove("./src/files/temp.txt")
            temp_file = open("./src/files/temp.txt","x")
		
        file = open('./src/files/Menu.txt','r')
        if case == "update":
            if catogery:
                for line in file:
                    try: 
                        idx,cat,MenuItem,CurrentPrice = line.split(":")[:-1]
                    except ValueError:
                        continue
                    if item == MenuItem:
                        temp_file.write(idx+SEP+cat+SEP+MenuItem+SEP+UpdatedPrice+SEP+NEXT)
                        continue
                    temp_file.write(line)
        elif case == "delete":
            if catogery:
                for i,line in enumerate(file):
                    currentNumber = i+1
                    try: 
                        idx,cat,MenuItem,CurrentPrice = line.split(":")[:-1]
                    except ValueError:
                        continue
                    if item == MenuItem:
                        continue
                    temp_file.write(line+NEXT)
        temp_file.close()
        file.close()
	
        os.remove('./src/files/Menu.txt')
        os.rename("./src/files/temp.txt","./src/files/Menu.txt")
        return 
        
    def display_html(self):
        code = "<html>"
        for item in self.items.keys():
            code += "<h2>"+item+"</h2>"
            d = list(self.items[item].items())
            code += tabulate(d,headers=["Items",'price'],tablefmt='html')
        webbrowser.register('chrome',None,
	    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        html = open('./page.html','w')
        html.write('<html>'+code+"</html>")
        html.close()
        path = "file:///"+os.getcwd()+"/"+'page.html'
        webbrowser.get('chrome').open_new(path)
        #webbrowser.open(path)

    def display(self,catogery=None):
        #print(self.items)
        if catogery:
            d = list(self.items[catogery].items())
            print(" * * {} * *".format(catogery))
            print(tabulate(d,headers=["Items",'price']))
            print()
        else:
            for item in self.items.keys():
                d = list(self.items[item].items())
                print(" * * {} * *".format(item))
                print(tabulate(d,headers=["Items",'price']))
                print()

