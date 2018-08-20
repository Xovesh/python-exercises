def quicksort(nlist):
    quicksorthelper(nlist, 0, len(nlist)-1)
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
