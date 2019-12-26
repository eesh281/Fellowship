try:
    import json
except ImportError:
    print("Error while Importing")  


class FileOpen:
    def open_file(self):
        file = open("/home/user/Desktop/newfolder/Fellowship/invent_manag.py/inven_json.json", "r")
        data_read_dict = json.load(file)
        rice_arr = data_read_dict["Rice"]
        wheat_arr = data_read_dict["Wheat"]
        pulse_arr = data_read_dict["Pulse"]
        file.close()
