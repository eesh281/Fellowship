#*********************************************************************************************************
#@purpose    : to calcute distance between to origin from two points x,y
#@file name  :distance.py
#@author name:Gursheesh Kour
#*******************************************************************************************************

#method to calculate the distance
def distance_( x, y ):
    dis = ( x * x + y * y )** 0.5
    return dis

#taking values from user
x=int(input("enter x: "))
y=int(input("enter y: "))

print(distance_( x, y ))