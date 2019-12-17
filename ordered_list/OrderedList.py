# *********************************************************************************************************************************************
# @purpose :Implement Ordered list Using LinkedList
# @file    :Ordered_List.py
# @author  :GursheeshKour
# *********************************************************************************************************************************************
from business_logic import linked_lists


def openfile():
    file = open("Num_File.txt", "r+")
    x = file.read()
    li = linked_list()
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

