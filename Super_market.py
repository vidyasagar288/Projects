from datetime import datetime

Groceries='''               
Available Groceries

rice    RS 20kg
sugar   RS 30kg
salt    RS 10kg
oil     RS 110/ltr
maggie  RS 50/kg
moondal RS 100/kg
toordal RS 120/kg 

'''

users = {"abc":123, "def":456} 
user=input("Enter the user name: ")
if user in users.keys():
    password = int(input("enter the password: "))
    if password== users[user]:
        
        print("--------------------------------------------------Welcome to **Super market**----------------------------------------------")
        print("---------------------------------------------------------------------------------------------------------------------------")
        #print(Groceries)
    else:
        print("Wrong credentials")
        
    
    
price=0
pricelist=[]
total_Price=0
Final_Price=0
ilist=[]
qlist=[]
plist=[]

items={'rice':20,
'sugar':30,
'salt':10,
'oil':110,
'maggie':50,
'moondal':100,
'toordal':120}    
   
option= int(input("for list of items press 1: "))    
if option==1:
    print(Groceries)

for i in range(len(items)):
    inp1= int(input("if you want to buy press 1 or 2 for exit: "))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter the your items: ")
        quantity= int(input("Enter the your Quntity: "))
        #inp1= int(input("if you want to buy more press 1 or 2 for exit: "))
        
        # item2=input("Enter the your items: ")
        # quantity2= int(input("Enter the your Quntity: "))
    
        if item in items.keys():
            price= quantity*(items[item])
        #price2= quantity2*(items[item2])
            pricelist.append((item,quantity,items,price))
            total_Price+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(total_Price*5)/100
            Final_Price= gst+total_Price
        else:
            print("sorry you entered item is not available")
    else:
        print("Your enteres wrong number")
    inp= input("can i bill the items yes/no: ")
    if inp=='yes':
        pass
        if Final_Price!=0:
            print(30*"=","super_market",30*"=")
            print(32*" ","Hyderabad")
            print("Name: ",34*" ", "Date",datetime.now())
            print(75*"-")
            print("sno",7*" ", 'items',12*" ", 'qunatity',15*" ",'price')
            
            
            for i in range(len(pricelist)):
                print(i, 8*'', 8*' ',ilist[i],8*"  ",qlist[i],10*"  ", plist[i])
            print(75* "-")
            print(50*" ",'Total_Amount:', 'Rs', total_Price)
            print(50*" ","gst amount  :", 'Rs',gst)
            print(75* "-")
            print(50*" ",'Final_amount:', 'Rs', Final_Price)
            print(75* "-")
            print(50*" ","Thanks for visiting")
            print(75* "-")
            
    
    
    
    
    
    
    
    
    
    
    


