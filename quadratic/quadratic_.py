#*********************************************************************************************************
#@purpose    :to solve a quadratic equation
#@file name  :quadratic.py
#@author name:Gursheesh Kour
#*******************************************************************************************************

#method to solve a quadratic equation
def quadratic1(a,b,c):
    D = b * b - 4*a * c
    sqroot = D**0.5
    root1 = (-b + sqroot) / 2*a
    root2 = (-b - sqroot) / 2*a
    return root1,root2

#taking values from user
a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))
print(quadratic1( a, b, c ))