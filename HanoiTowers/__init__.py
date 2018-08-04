import Hanoi
import time

start_time = time.time()
a = Hanoi.Hanoi(15)
print("--- %s seconds ---" % (time.time() - start_time))
