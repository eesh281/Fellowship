def leap_year(year):

    if(year<1582):
        return False
    if(year%400==0 or (year%4==0 and year%100!=0)):
        return True
    else:
        return False
year=int(input("Input the year you want to check: "))
if(leap_year(year)==True):
         print('leap year')
else:
         print('not a leap year')

