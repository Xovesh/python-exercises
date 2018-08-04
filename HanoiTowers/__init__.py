import Hanoi
import time

start_time = time.time()
Hanoi.Hanoi(int(input("Put a number: ")))
print("Time used")
print("--- %s seconds ---" % (time.time() - start_time))
