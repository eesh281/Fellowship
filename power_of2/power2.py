#*********************************************************************************************************
#@purpose    :to print table of power of 2
#@file name  :power2.py
#@author name:Gursheesh Kour
#*******************************************************************************************************

#method to print table of power of 2
def power_of_2( num ):
    res_list = []
    i = 0
    while( i <= num ):
        res_list.append( 2**i )
        i += 1
    return res_list

#printing return value of function
print( power_of_2 )

