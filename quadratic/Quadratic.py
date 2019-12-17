def Quadratic1(a,b,c):
    D = b * b - 4*a * c
    sqroot = D**0.5
    root1 = (-b + sqroot) / 2*a
    root2 = (-b - sqroot) / 2*a
    return root1,root2

a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))
print(Quadratic1(a,b,c))