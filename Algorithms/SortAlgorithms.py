# quicksort average performance O(n log n)
def quicksort(nlist):
    quicksorthelper(nlist, 0, len(nlist) - 1)
    return nlist


def quicksorthelper(nlist, first, last):
    if first < last:
        split = splitlist(nlist, first, last)
        quicksorthelper(nlist, first, split - 1)
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


# mergetsort average performance O(n log n)
def mergesort(nlist):
    if len(nlist) <= 1:
        return nlist

    mid = int(len(nlist) / 2)
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


# merge sort linked list implementation average performance O(n log n)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def sortList(head):
    if head is None or head.next is None:
        return head

    middle = getmiddle(head)
    nextpoint = middle.next
    middle.next = None

    left = sortList(head)
    right = sortList(nextpoint)
    return mergesorthelper(left, right)


def mergesorthelper(left, right):
    ordered = ListNode(-1)
    s = ordered
    while left is not None and right is not None:
        if left.val > right.val:
            ordered.next = ListNode(right.val)
            right = right.next
        else:
            ordered.next = ListNode(left.val)
            left = left.next
        ordered = ordered.next

    if left is not None:
        ordered.next = left
    else:
        ordered.next = right
    return s.next


def getmiddle(node):
    if node is None or node.next is None:
        return node

    current = node.next
    previous = node.next

    while current.next is not None:
        current = current.next
        if current.next is not None:
            previous = previous.next
            current = current.next

    return previous


# bubblesort average performance O(n^2)
def bubblesort(nlist):
    for i in range(0, len(nlist) - 1):
        for j in range(0, len(nlist) - 1):
            if nlist[j] > nlist[j + 1]:
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
    return nlist


# insertionsort average performance O(n^2)
def insertionsort(nlist):
    for i in range(1, len(nlist)):
        border = i - 1
        while nlist[border] > nlist[border + 1] and border > -1:
            nlist[border], nlist[border + 1] = nlist[border + 1], nlist[border]
            border -= 1
    return nlist
