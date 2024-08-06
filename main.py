#Count timer program in Python
import time

my_time=int(input("Enter the time in seconds: "))

for x in range(my_time,0,-1):
    seconds = x%60
    minutes=int(x/60)%60
    hours=int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1) #After each iteration we will sleep for one second
print("Time is up")