import json

class StockAccount:

    def openning_file(self):
        file = open("/home/user/Desktop/newfolder/Fellowship/commercial_data/client_data.json", "r")
        data_dict = json.load(file)
     
        #user_arr = data_dict["Users"]
        share_arr = data_dict["Shares"]
        return share_arr

    def update_json(self, share_arr):
        result_list = [ sub["amount"] for sub in share_arr ]
        input_amount = int(input("enter the amount for the shares: "))
        for item in result_list:
            leftover = item - input_amount
            print(leftover)
            return leftover




obj = StockAccount()
a= obj.openning_file()
data = obj.update_json(a)


if __name__ == '__main__' :

    inp = input(" type : Y if you are an existing user and type : N if you are a new user:")
    if (inp == "y") or (inp == "Y"):
        obj.openning_file()
        file2 = open("/home/user/Desktop/newfolder/Fellowship/commercial_data/file.json", "w") 
        data = json.dumps(data)
        json.dump(data, file2, indent=4)
        #file2.write(data)
    else:
        f = open("/home/user/Desktop/newfolder/Fellowship/commercial_data/company_data.json","a+")
        name = input("Enter the Name: ")
        age = int(input("Enter the age: "))
        number = int(input("Enter your Mobile Number: "))
        address = (input("Enter the Address: "))
        writting = f.write(' [{'+'     "Name" : "'+ name +'",\n' + '        "Age"  : "'+str(age)+'",\n'+'       "Ph.No" : "'+str(number)+'",\n'+'"Address" : "'+str(address)+'" }]')
        print("The Data has been Stored Successfully in 'newUser.json' file. ")



       








    