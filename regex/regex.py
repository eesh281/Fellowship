#*****************************************************************************************************
#@purpose: to implement regex
#@file:regex.py
#@author:Gursheesh Kour
#*****************************************************************************************************

#importing regex module
import re
#importing datetime module
import datetime

#creating a class named Reg_ex for implementing regular expression
class RegexImplementation:

    #method created
    def regex(self):
        #file opened with read and writing permission
        file = open("/home/user/Desktop/newfolder/Fellowship/regex/reg_text.txt", "r+")
        x = file.read()
        #using regex function sub
        data = re.sub(r"[<]{2}[a-zA-Z]{4}[>]{2}", "Gursheesh", x) 
        data = re.sub(r"[<]{2}[a-z]{8}[>]{2}", "Gursheesh Kour" , data)
        data = re.sub(r"[x]{10}", "9419624315" , data)
        today = str(datetime.date.today())
        data = re.sub("01/01/2016",today , data)
        #writing into the file
        file.write(data)
        file.write("\n")
        #closing file
        file.close()


obj = RegexImplementation()
obj.regex()