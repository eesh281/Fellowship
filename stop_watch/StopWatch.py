#importing time module
import time

#taking the instance to start from user
start = input("press enter to start the timer")
print("timer on")

#taking current time from system
begin=time.time()

endtimer=input("press enter to end the timer")

#taking end time from system
end=time.time()
#finding time elapsed
elapsed=end-begin

#converting it into int
elapsed=int(elapsed)

#printing elapsed seconds
print("The time elapsed is",elapsed,"seconds")
