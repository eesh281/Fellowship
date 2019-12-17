# *********************************************************************************************************************************************
# @purpose :Implement Ordered list Using LinkedList
# @file    :Ordered_List.py
# @author  :GursheeshKour
# *********************************************************************************************************************************************
#importing Linked_List from utility.py from package util
from util.utility import Linked_List

#method to open file
def openfile():
    file = open("Num_File.txt", "r+")
    x = file.read()
    #creating an object of Linked_List class
    li = Linked_List()
    #adding words to linkedlist
    for word in x.split():
        li.add(word)
    li.display()
    li = li.sort()
    li.display()
    #taking the word to be searched from user
    s_word = input("enter a word to search: ")
    li.search(s_word)
    li.append(s_word)
    li.sort()
    li.display()
    file.write(s_word)
    file.close()

#calling the method created
openfile()

