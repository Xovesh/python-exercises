from HanoiTowers import Hanoi
import time

start_time = time.time()
Hanoi.Hanoi(10)
print("Time used")
print("--- %s seconds ---" % (time.time() - start_time))
