import json

class FileSystem:

    def openning_file(self):

        file = open("/home/user/Desktop/newfolder/Fellowship/addressbook/user_detail.json", "r+")
        data_dict = json.load(file)
        return file, data_dict

