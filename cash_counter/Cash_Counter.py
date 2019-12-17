# *********************************************************************************************************************************************
# @purpose :Implement Cash_Counter.py list Using LinkedList
# @file    :Cash_Counter.py
# @author  :GursheeshKour
# *********************************************************************************************************************************************

from util.utility import Queue  

#creating a method for cash counter
def cash_counter():
    y = int(input("enter the total number of times you want to deposit or withdraw :"))
    for i in range(y):
        x = int(input("For Deposit enter: 1 and For Withdraw enter2:"))

        if x == 1:

            #creating a method to deposit
            def deposit_withdrawl():
                balance = 0
                num = int(input("enter the number of times to deposit money"))
                for j in range(num):
                    amount = eval(input("enter the amount"))
                    balance += amount
                    print("total balance is :", balance)
                    #creating an object of imported class
                    q = Queue()
                    q.enqueue(balance)
                    q.display()
                return balance
            #storing the return value of the respective method in result
            result = deposit_withdrawl()

        elif x == 2:
            print("available balance is", result)
            withdr = eval(input("enter the amount to withdraw"))
            result -= withdr
            print("balance left is :", result)


#creating an object of imported class
q = Queue()
cash_counter()
