import random
from Algorithm import SortAlgorithm
import time


def randomarraynumbers():
    array = []
    for i in range(0, 800000):
        array.append(random.randrange(0, 1000, 1))

    return array


def checksort(arr):
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True


k = time.time()
s = randomarraynumbers()
j = SortAlgorithm.quicksort(s)
print(time.time()-k)
print(checksort(j))
