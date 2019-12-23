#******************************************************************************************************
#@purpose:demonstrating stock market using json
#@file   :stock_account.py
#@author :Gursheesh Kour
#*******************************************************************************************************

#importing json module
import json

#creating stock account class
class StockAccount:

    #creating a method to open file
    def openning_file(self):
        file = open("/home/user/Desktop/newfolder/Fellowship/commercial_data/client_data.json", "r")
        data_dict = json.load(file)
        share_arr = data_dict["Shares"]
        x = int(input("Type: 0 for HCL \n Type: 1 for TATA \n Type: 2 for BRIDGELABZ \n"))

        #providing a choice for selecting company
        if x == 0:
            share_amount = share_arr[0]
            final_amount = share_amount["amount"]
            print(final_amount)
            return final_amount

        if x == 1:
            share_amount = share_arr[1]
            final_amount = share_amount["amount"]
            print(final_amount)
            return final_amount

        if x == 2:
            share_amount = share_arr[2]
            final_amount = share_amount["amount"]
            print(final_amount)
            return final_amount
        
        return share_arr   
        
        
    #creating a method to update the json file
    def update_json(self, final_amount):
       
        input_amount = int(input("enter the amount for the shares: "))
        substract = final_amount - input_amount
        print(substract)
        return substract 

    
#creating an object of class
obj = StockAccount()
a= obj.openning_file()
data = obj.update_json(a)


if __name__ == '__main__' :

    #inputting whether to register a user or existing user
    inp = input(" type : Y if you are an existing user and type : N if you are a new user:")
    if (inp == "y") or (inp == "Y"):
        file2 = open("/home/user/Desktop/newfolder/Fellowship/commercial_data/file.json", "w")
        #adding updated data to json file 
        json.dump(data, file2, indent=4)
        
        
    else:
        #openning the file to add new user
        f = open("/home/user/Desktop/newfolder/Fellowship/commercial_data/company_data.json","a+")
        name = input("Enter the Name: ")
        age = int(input("Enter the age: "))
        number = int(input("Enter your Mobile Number: "))
        address = (input("Enter the Address: "))
        writting = f.write(' [{'+'     "Name" : "'+ name +'",\n' + '        "Age"  : "'+str(age)+'",\n'+'       "Ph.No" : "'+str(number)+'",\n'+'"Address" : "'+str(address)+'" }]')
        print("The Data has been Stored Successfully in the file. ")



       








    