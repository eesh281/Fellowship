import json 

class FileSystem:
    def __init__(self, filename):  

            with open(filename) as f:
                # json file is loaded
                self.data = json.load(f)  
