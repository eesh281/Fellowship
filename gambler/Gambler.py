import random

def Gambler1(stake,goal,num):
    wins=0
    bets=0
    loss=0
    for i in range(0,num+1):
        cash=stake
        while (cash>0 and cash<goal):
            bets+=1
            if random.randint(0,1)>0.5:
                cash+=1
            elif random.randint(0,1)<0.5:
                cash-=1
            if cash==goal:
                 wins+=1
            else:
                 loss+=1
    return loss,wins
stake=int(input("enter stake: "))
goal=int(input("enter goal: "))
num=int(input("enter number of times: "))
loss,wins = Gambler1(stake,goal,num)
print("number of wins",wins)
print("percentage of wins= ", 100*(wins/(wins+loss)))
print("percentage of losses= ", 100*(loss/(wins+loss)))