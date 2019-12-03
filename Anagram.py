def anagram(s1, s2):
    if sorted(s1) == sorted(s2):
        print("Anagrams")
    else:
        print("Not Anagram")
    return s1, s2


s1 = input("give first string: ")
s2 = input("give second string: ")
anagram(s1, s2)
