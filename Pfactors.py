def Prime_Factor(num):
    div=2
    pfact_list=[]
    while(num>1):
        while num%div==0:
            pfact_list.append(div)
            num=num/div

        div+=1
    return (pfact_list)


num = int(input("enter number: "))
print(Prime_Factor(num))
