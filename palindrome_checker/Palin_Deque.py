# *********************************************************************************************************************************************
# @purpose :Implement Palindrome check Using LinkedList
# @file    :Palin_Deque.py
# @author  :GursheeshKour
# *********************************************************************************************************************************************
#importing class Deque from utility.py from folder utilss
from util.utility.py import Deque

#method to check whether string is palindrome or not
def palindrome(string):
    rev = string[::-1]
    if string == rev:
        return True
    return False


#input a string to be checked 
string = input("enter a string: ")
#create an object of class Deque
d = Deque()
for word in string:
    d.addRear(word)
d.display()
d.reverse()
d.display()
print(palindrome(string))
