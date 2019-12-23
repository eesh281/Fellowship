import json

class StockAccount:

    def openning_file(self):
        file = open("/home/user/Desktop/newfolder/Fellowship/commercial_data/client_data.json", "r")
        data_dict = json.load(file)
     
        #user_arr = data_dict["Users"]
        share_arr = data_dict["Shares"]
        x = input("Type: 0 for HCL \n Type: 1 for TATA \n Type: 2 for BRIDGELABZ \n")

        if x == 0:
            print("hello")
            share_amount = share_arr[2]
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
        
        

        

    def update_json(self, final_amount):
       
        input_amount = int(input("enter the amount for the shares: "))
        substract = final_amount - input_amount
        print(substract)
        return substract 

    

obj = StockAccount()
a= obj.openning_file()
data = obj.update_json(a)


if __name__ == '__main__' :

    inp = input(" type : Y if you are an existing user and type : N if you are a new user:")
    if (inp == "y") or (inp == "Y"):
        obj.openning_file()
        file2 = open("/home/user/Desktop/newfolder/Fellowship/commercial_data/file.json", "w") 
        json.dump(data, file2, indent=4)
        
    else:
        f = open("/home/user/Desktop/newfolder/Fellowship/commercial_data/company_data.json","a+")
        name = input("Enter the Name: ")
        age = int(input("Enter the age: "))
        number = int(input("Enter your Mobile Number: "))
        address = (input("Enter the Address: "))
        writting = f.write(' [{'+'     "Name" : "'+ name +'",\n' + '        "Age"  : "'+str(age)+'",\n'+'       "Ph.No" : "'+str(number)+'",\n'+'"Address" : "'+str(address)+'" }]')
        print("The Data has been Stored Successfully in the file. ")



       








    