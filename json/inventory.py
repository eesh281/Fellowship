import json

file = open("/home/user/Desktop/newfolder/Fellowship/json/json_file.json","r")
data_read = json.load(file)
#print(data_read)

def inventory_rice():
    for rice in data_read["Rice"]:
        print(rice)
        rice_variety(rice)
        
        def rice_variety(i):
            for name in i["name"]:
                print(name)

def inventory_pulse():
    for pulse in data_read("Pulse"):
        print(pulse)

inventory_rice()       