from HanoiTowers import Hanoi
import time

start_time = time.time()
Hanoi.Hanoi(15)
print("Time used")
print("--- %s seconds ---" % (time.time() - start_time))
