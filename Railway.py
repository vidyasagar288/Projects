import numpy as np

"""
1.Train PNR
2.Login
3.from To Destination
4.Seats Avilability
5.Date and Time
6.Price
7. user details- name, mobile, adress

"""


requirements='''
1.user details
2.from and destination
3.Search by train number
4.price
5.Book ticket
6.PNR Generate

'''
Trains_list={"godavari":17001,"Prasanthi":17002,"Konark":17004, "Tirupathi":17003,"Konark":17004}
price={"bza-hyd":500,"vizag-hyd":900}

Trains={("bza", "hyd"): [{"godavari":17001,"Prasanthi":17002,"Konark":17004, "Tirupathi":17003}],
        ("vizag", "hyd"): [{"godavari":17001,"Prasanthi":17002,"Konark":17004}]}
        
        
users = {"abc":123, "def":456}              #user id and passward
user_info=[]
user=input("Enter the user name: ")
if user in users.keys(): 
    password = int(input("enter the password: "))
    if password== users[user]:
        print("--------------------------------------------------Welcome to **Indian Railways**----------------------------------------------")
        print("---------------------------------------------------------------------------------------------------------------------------")
        print(requirements)
        option = int(input("Enter the option: "))
        if option==1 :
            name=input("Enter your name: ")
            mobile=int(input("Enter the Mobile Number: "))
            age= int(input("Enter the age: "))
            Gender= input("Enter the Gender: ")
            i= [name,mobile,age,Gender]                 #i= i is used for data store in list
            #print(i)
            user_info.append(i)
            print(user_info)
             
        elif option==2:
            from_station = input("enter the your from station: ")
            Destination= input("enter the your destination: ")
            print("available Trains : ")
            for i in Trains:
                if from_station in ("bza", "hyd"):
                    if Destination in ("bza", "hyd"):
                        print(Trains[("bza", "hyd")])
                        break                                   #for loop break if no break op 2 times reflect
                elif from_station in ("vizag", "hyd"):
                    if Destination in ("vizag", "hyd"):
                        print(Trains[("vizag", "hyd")])
                        break
                else :
                    print("No Trains avaible this in this route")
                
                
        elif option==3:
            Train_Number = int(input("Enter the Train Number: "))
            if Train_Number in Trains_list:
                print(Trains_list.keys())
            else:
                print("Invalid train number")
                
        elif option==4:
            print(price)
        elif option==5:
            from_station = input("enter the your from station: ")
            Destination= input("enter the your destination: ")
            print("available Trains : ")
            for i in Trains:
                if from_station in ("bza", "hyd"):
                    if Destination in ("bza", "hyd"):
                        print(Trains[("bza", "hyd")])
                        print("Amount: ", price["bza-hyd"],"Rs")
                    ans= input("can i Book the ticket yes/no: ")
                    if ans=='yes':
                        booking_train=int(input("Enter the train number: "))
                        print("tour booking confirmed")
                        pnr=np.random.randint(low=000000000,high=999999999)
                        print("Your PNR number: ",pnr)
                        print(30*"=","thanking you for booking",30*"=",)
                        break
                    else:
                        print(30*"=","Visiting Agaian",30*"=") 
                        break 
                elif from_station in ("vizag", "hyd"):
                    if Destination in ("vizag", "hyd"):
                        print(Trains[("vizag", "hyd")])
                        print("Amount: ",price["vizag-hyd"],"Rs")
                    ans= input("can i Book the ticket yes/no: ")
                    if ans=='yes':
                        booking_train=int(input("Enter the train number: "))
                        print("your Booking successfully")
                        pnr=np.random.randint(low=000000000,high=999999999)
                        print("Your PNR number: ",pnr)
                        print(30*"=","thanking you for booking",30*"=",)
                        break
                    else:
                        print(30*"=","Visiting Agaian",30*"=")
                        
                    
        elif option==6:
            pnr=np.random.randint(low=000000000,high=999999999)
            print(pnr)
            
    
    
    else:
        print("Invalid Passward")                           #for wrong pass
        print("Try Again")















