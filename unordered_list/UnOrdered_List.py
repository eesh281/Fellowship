# *********************************************************************************************************************************************
# @purpose :Implement UnOrdered list Using LinkedList
# @file    :UnOrdered_List.py
# @author  :GursheeshKour
# *********************************************************************************************************************************************
from util.utility.py import Linked_List

def open_file():
    i = 0
    f = open("text_file.txt", "r+")
    line = f.read()
    li = Linked_List()
    for word in line.split(" "):
        li.add(word)
        i += 1

    li.display()
    li.isEmpty()
    li.size()
    s_word = input("enter a word to search: ")
    li.search(s_word)
    li.append(s_word)
    li.append(s_word)
    li.display()
    f.write(str(s_word))
    f.close()
open_file()
