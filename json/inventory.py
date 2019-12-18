import json

class Json_Inventory:
    
    def json_inventory(self):
        with open("/home/user/Desktop/newfolder/Fellowship/json/json_file.json","r") as file:
            data_read_dict = json.load(file)
            rice_arr = data_read_dict["Rice"]
            wheat_arr = data_read_dict["Wheat"]
            pulse_arr = data_read_dict["Pulse"]

            rice_price = 0
            pulse_price = 0
            wheat_price = 0

            
                
            for rice_key in rice_arr:
                rice_price = rice_price + rice_key["price"]
                
            for pulse_key in pulse_arr:
                pulse_price = pulse_price + pulse_key["price"]

            for  wheat_key in wheat_arr:
                wheat_price = wheat_price + wheat_key["price"]

        
                
            print(f"The price of rice is {rice_price}.\nThe price of wheat is {wheat_price}.\nThe price of Pulse is {pulse_price}. ")

            json_str = json.dumps("/home/user/Desktop/newfolder/Fellowship/json/output_jason.json")

            with open("/home/user/Desktop/newfolder/Fellowship/json/output_jason.json","w") as out_file:
                json.dump(data_read_dict, out_file, indent=3)
            print(json_str)


b = Json_Inventory()
b.json_inventory()


    