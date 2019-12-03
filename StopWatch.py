import time

start=input("press enter to start the timer")
print("timer on")
begin=time.time()
endtimer=input("press enter to end the timer")
end=time.time()
elapsed=end-begin
elapsed=int(elapsed)
print("The time elapsed is",elapsed,"seconds")
