#*********************************************************************************************************
#@purpose    : to simulate a game of gamble
#@file name  :gambler.py
#@author name:Gursheesh Kour
#*******************************************************************************************************

#importing random module
import random

#method to stimulate a gamble
def Gambler1(stake,goal,num):
    wins = 0
    bets = 0
    loss = 0
    for _ in range( 0, num + 1 ):
        cash = stake
        while ( cash > 0 and cash < goal ):
            bets += 1
            if random.randint( 0, 1 ) > 0.5:
                cash += 1
            elif random.randint( 0, 1 ) < 0.5:
                cash -= 1
            if cash==goal:
                 wins += 1
            else:
                 loss += 1
    return loss,wins

#taking stake,goal and number from user 
stake=int(input("enter stake: "))
goal=int(input("enter goal: "))
num=int(input("enter number of times: "))

loss,wins = Gambler1( stake, goal, num )

print("number of wins", wins )
print("percentage of wins= ", 100*(wins/(wins+loss)))
print("percentage of losses= ", 100*(loss/(wins+loss)))