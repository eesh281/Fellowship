#*********************************************************************************************************
#@purpose    :to print table of power of 2
#@file name  :power2.py
#@author name:Gursheesh Kour
#*******************************************************************************************************

#method to find prime factors to a number
def prime_factor_( num ):
    div = 2
    pfact_list = []
    while( num>1 ):
        while num % div == 0:
            pfact_list.append( div )
            num = num/div

        div += 1
    return ( pfact_list )

#taking input from user
num = int( input( "enter number: " ))

print( prime_factor_( num ))
