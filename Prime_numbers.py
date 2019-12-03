
def prime_num(lower, upper):
    num_list=[]
    for num in range(0, 1000):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                num_list.append(num)

    return num_list

x = prime_num(0, 1000)
print(x)

def Anagram(a_list):
    for j in range(0,len(a_list)-1):
        for k in range(1,len(a_list)):
            x=str(a_list[j])
            y =str(a_list[k])
            if sorted(x)==sorted(y):
                print(a_list[j],"and",a_list[k],"are anagrams")

    return a_list
Anagram(x)

def Palindrome(p_list):

    for s in range(0,len(p_list)):
        z=str(p_list[s])
        if z==z[::-1]:
            print(p_list[s],"is a palindrome")
    return p_list
Palindrome(x)


