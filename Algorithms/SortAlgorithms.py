# average performance O(n log n)
def quicksort(nlist):
    quicksorthelper(nlist, 0, len(nlist) - 1)
    return nlist

def quicksorthelper(nlist, first, last):
    if first < last:
        split = splitlist(nlist, first, last)
        quicksorthelper(nlist, first, split-1)
        quicksorthelper(nlist, split + 1, last)

def splitlist(nlist, first, last):
    pivot = nlist[last]
    left = first
    border = first

    for i in range(left, last):
        if nlist[i] < pivot:
            nlist[i], nlist[border] = nlist[border], nlist[i]
            border += 1
    nlist[last], nlist[border] = nlist[border], nlist[last]
    return border

# average performance O(n log n)
def mergesort(nlist):
    if len(nlist) <= 1:
        return nlist

    mid = int(len(nlist)/2)
    left = nlist[:mid]
    right = nlist[mid:]

    left = mergesort(left)
    right = mergesort(right)
    return mergehelp(left, right)

def mergehelp(left, right):
    result = []
    leftindex, rightindex = 0, 0
    while leftindex < len(left) and rightindex < len(right):
        if left[leftindex] <= right[rightindex]:
            result.append(left[leftindex])
            leftindex += 1
        else:
            result.append(right[rightindex])
            rightindex += 1

    result += left[leftindex:]
    result += right[rightindex:]
    return result

# average performance O(n^2)
def bubblesort(nlist):
    for i in range(0, len(nlist)-1):
        for j in range(0, len(nlist)-1):
            if nlist[j] > nlist[j+1]:
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
    return nlist

# average performance O(n^2)
def insertionsort(nlist):
    for i in range(1, len(nlist)):
        border = i-1
        while nlist[border] > nlist[border+1] and border > -1:
            nlist[border], nlist[border+1] = nlist[border+1], nlist[border]
            border -= 1
    return nlist
