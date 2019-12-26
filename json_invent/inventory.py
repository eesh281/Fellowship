#*****************************************************************************************************
#@purpose: to evaluate value of inventory object
#@file:inventory.py
#@author:Gursheesh Kour
#*****************************************************************************************************

#importing json module 
import json

#creating a class for performing inventory object
class Json_Inventory:
    
    #creating a method named json_inventory
    def json_inventory(self):
        #opening the json file with reading permission and closing it after use
        with open("/home/user/Desktop/newfolder/Fellowship/json/json_file.json","r") as file:
            data_read_dict = json.load(file)
            
            #storing the key values of the dict
            rice_arr = data_read_dict["Rice"]
            wheat_arr = data_read_dict["Wheat"]
            pulse_arr = data_read_dict["Pulse"]

            rice_price = 0
            pulse_price = 0
            wheat_price = 0

            
                
            for rice_key in rice_arr:
                #calculating the total price of all the rice
                rice_price = rice_price + rice_key["price"]
                
            for pulse_key in pulse_arr:
                #calculating the total price of all the pulse
                pulse_price = pulse_price + pulse_key["price"]

            for  wheat_key in wheat_arr:
                #calculating the total price of all the wheat
                wheat_price = wheat_price + wheat_key["price"]

        
                
            print(f"The price of rice is {rice_price}.\nThe price of wheat is {wheat_price}.\nThe price of Pulse is {pulse_price}. ")
            
            #outputing json object as string
            json_str = json.dumps("/home/user/Desktop/newfolder/Fellowship/json/output_jason.json")
            #opening file with writing permission and closing it after use
            with open("/home/user/Desktop/newfolder/Fellowship/json/output_jason.json","w") as out_file:
                #writing json objuect to file
                json.dump(data_read_dict, out_file, indent=3)
            print(json_str)


b = Json_Inventory()
b.json_inventory()


    