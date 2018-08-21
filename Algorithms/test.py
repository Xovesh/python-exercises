import random
from Algorithms import SortAlgorithms
import time


def randomarraynumbers():
    array = []
    for i in range(0, 100):
        array.append(random.randrange(0, 1000, 1))

    return array


def checksort(arr):
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

def checkall():
    k = time.time()
    j = SortAlgorithms.quicksort(randomarraynumbers())
    print("Time for sorting (quick sort): " + str(time.time() - k))
    print("Checking correcting sort: " + str(checksort(j)))
    k = time.time()
    j = SortAlgorithms.insertionsort(randomarraynumbers())
    print("Time for sorting (insertion sort): " + str(time.time()-k))
    print("Checking correcting sort: " + str(checksort(j)))
    k = time.time()
    j = SortAlgorithms.bubblesort(randomarraynumbers())
    print("Time for sorting (bubble sort): " + str(time.time()-k))
    print("Checking correcting sort: " + str(checksort(j)))
    k = time.time()
    j = SortAlgorithms.mergesort(randomarraynumbers())
    print("Time for sorting (merge sort): " + str(time.time() - k))
    print("Checking correcting sort: " + str(checksort(j)))


checkall()

