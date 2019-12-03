import re

def reg_ex():
    a = "Hello <<name>>, We have your full name as <<full name>> in our system. your contact number is 91-xxxxxxxxxx."
    "Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016"
    p = re.sub("<<name>>", "Gursheesh", a)
    p = re.sub("<<full name>>", "Gursheesh Kour", p)
    p = re.sub("xxxxxxxxxx", "9145623060", p)
    p = re.sub("01/01/2016", "03/12/2019", p)
    print(p)

reg_ex()
