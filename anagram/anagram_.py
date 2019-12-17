#*********************************************************************************************************
#@purpose    :to check for anagram
#@file name  :anagram.py
#@author name:Gursheesh Kour
#*******************************************************************************************************

#method to check anagram
def anagram( s1, s2 ):
    if sorted(s1) == sorted(s2):
        print("Anagrams")
    else:
        print("Not Anagram")
    return s1, s2

#taking values from user
s1 = input("give first string: ")
s2 = input("give second string: ")

#calling method anagram
anagram( s1, s2 )
