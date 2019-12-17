# *********************************************************************************************************************************************
# @purpose :Implement Ordered list Using LinkedList
# @file    :Ordered_List.py
# @author  :GursheeshKour
# *********************************************************************************************************************************************
from util.utility.py import Linked_List


def openfile():
    file = open("Num_File.txt", "r+")
    x = file.read()
    li = Linked_List()
    for word in x.split():
        li.add(word)
    li.display()
    li = li.sort()
    li.display()
    s_word = input("enter a word to search: ")
    li.search(s_word)
    li.append(s_word)
    li.sort()
    li.display()
    file.write(s_word)
    file.close()


openfile()

