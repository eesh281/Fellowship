import json

class :

    def openning_file(self):

        file = open("/home/user/Desktop/newfolder/Fellowship/addressbook/user_detail.json", "r")
        data_dict = json.load(file)
        return data_dict

    def user_details(self):

        add_user = {}
        add_user["first_name"] = input("enter your first name: ") 
        add_user["last_name"] = input("enter your last name: ")
        add_user["address"] = input("enter your address: ")
        add_user["city"] = input("enter your city: ")
        add_user["zip_code"] = input("enter your zip: ")
        return add_user

    def adding_user(self):





obj = OpenFile()
obj.openning_file()
obj.user_details()
