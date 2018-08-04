import Hanoi
import time

start_time = time.time()
Hanoi.Hanoi(int(input("Introduce a number: ")))
print("Time used")
print("--- %s seconds ---" % (time.time() - start_time))
