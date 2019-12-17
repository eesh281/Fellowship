#*********************************************************************************************************
#@purpose    : to determine whether an year is leap or not
#@file name  :leap_year1.py
#@author name:Gursheesh Kour
#*******************************************************************************************************

#method to find whether a year is leap or not
def leap_year(year):

    if(year<1582):
        return False
    if(year%400 == 0 or ( year % 4 == 0 and year % 100 != 0 )):
        return True
    else:
        return False

#taking year from user
year=int(input("Input the year you want to check: "))

if(leap_year(year)==True):
         print('leap year')
else:
         print('not a leap year')

