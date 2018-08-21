import random
from Algorithms import SortAlgorithms
import time

# creates an array with j random numbers
def randomarraynumbers(j):
    array = []
    for i in range(0, j):
        array.append(random.randrange(0, 1000, 1))

    return array

# checks if an array is sort correctly
def checksort(arr):
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

# checks some sorting algorithms
def checkall(n):
    totaltime = 0
    k = time.time()
    j = SortAlgorithms.quicksort(randomarraynumbers(n))
    print("Time for sorting (quick sort): " + str(time.time() - k))
    print("Checking correcting sort: " + str(checksort(j)))
    totaltime += time.time() - k
    k = time.time()
    j = SortAlgorithms.insertionsort(randomarraynumbers(n))
    print("Time for sorting (insertion sort): " + str(time.time()-k))
    print("Checking correcting sort: " + str(checksort(j)))
    totaltime += time.time() - k
    k = time.time()
    j = SortAlgorithms.bubblesort(randomarraynumbers(n))
    print("Time for sorting (bubble sort): " + str(time.time()-k))
    print("Checking correcting sort: " + str(checksort(j)))
    totaltime += time.time() - k
    k = time.time()
    j = SortAlgorithms.mergesort(randomarraynumbers(n))
    print("Time for sorting (merge sort): " + str(time.time() - k))
    print("Checking correcting sort: " + str(checksort(j)))
    totaltime += time.time() - k
    return totaltime


print("Total time spended: " + str(checkall(10000)))
