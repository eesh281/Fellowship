#******************************************************************************************************
#@purpose:demonstrating stock market using json
#@file   :stock_account.py
#@author :Gursheesh Kour
#*******************************************************************************************************

#importing json module
import json

class StockAccount:

    #getting details from json file
    def stock_details(self):
        
        #openning a file to read 
        file=open("/home/user/Desktop/newfolder/Fellowship/commercial_data/client_data.json","r")
       
        #loading data from json file
        data_dict= json.load(file)
        share_arr =data_dict["Shares"]

        x = int(input("\n0 for HCL \n1 for TATA \n2 for BRIDGELABZ"))
        
        #comparing the input value for running various conditions
        if x == 0:
            
            for data in data_dict["Shares"]:
                
                if data['share'] == "HCL":
                    
                    input_amount=int(input("enter amount"))  
                    data['amount'] -= input_amount
                    
                    json_file = open("/home/user/Desktop/newfolder/Fellowship/commercial_data/client_data.json", "w")
                    json.dump(data_dict, json_file)
       
        if x == 1:
            
            for data in data_dict["Shares"]:
               
                if data['share'] == "TATA": 
                    
                    input_amount=int(input("enter amount"))
                    data['amount'] -= input_amount
                    
                    json_file = open("/home/user/Desktop/newfolder/Fellowship/commercial_data/client_data.json", "w")
                    json.dump(data_dict, json_file)
        
        if x == 2:
            
            for data in data_dict["Shares"]:
                
                if data['share'] == "BRIDGELABZ":
                    
                    input_amount=int(input("enter amount"))
                    data['amount'] -= input_amount
                    
                    json_file = open("/home/user/Desktop/newfolder/Fellowship/commercial_data/client_data.json", "w")
                    json.dump(data_dict, json_file)
    #closing the file after performing the operation
        file.close()

if __name__ == '__main__' :

    inp = input(" Are you an existing user(y/n):")
    file=open("/home/user/Desktop/newfolder/Fellowship/commercial_data/client_data.json","r")
    #loading data from json file
    data_dict= json.load(file)
    user_arr =data_dict["Users"]

    #condition to check whether the costumer is registered or not
    if (inp == "y") or (inp == "Y"):
        
        costumer_key = input("enter costumer id - 'registered name': ")
        
        for data in data_dict["Users"]:
           
            if costumer_key == data["name"]:
               
                print("welcome back!")
                obj1 = StockAccount()
                obj1.stock_details()
            
            else: 
                print("Not an existing user!")
      
    else:
        
        #appending a new user into the file
        f = open("newUser.json","a+")
       
        name = input("Enter the Name: ")
        Age = int(input("Enter the Age: "))
        phnum = int(input("Enter your Mobile Number: "))
        amount = int(input("Enter the Amount for Shares: "))
        cont = f.write(' [{'+'     "Name" : "'+ name +'",\n' + '        "Age"  : "'+str(Age)+'",\n'+'       "Ph.No" : "'+str(phnum)+'",\n'+'"Share Amount" : "'+str(amount)+'" }]\n'+''         )
       
        print("The Data has been Stored Successfully in 'newUser.json' file. ")
    #closing the file after use
    file.close()








    