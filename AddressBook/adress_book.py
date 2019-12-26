import json
from file_system import FileSystem

class AddressBook:

    def add_person(self,file):

        add_user = {}
        add_user["first_name"] = input("enter your first name: ") 
        add_user["last_name"] = input("enter your last name: ")
        add_user["address"] = input("enter your address: ")
        add_user["city"] = input("enter your city: ")
        add_user["zip_code"] = input("enter your zip: ")
        json.dump(add_user,file,indent=4)
        return add_user

   


obj1 = FileSystem()
file = obj1.openning_file()
obj = AddressBook()
obj.add_person(file)
