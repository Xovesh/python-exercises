def binarysearch(array, number):
    start = 0
    final = len(array)-1
    while start <= final:
        mid = int((start + final)/2)
        if array[mid] == number:
            return mid
        elif array[mid] < number:
            start = mid + 1
        elif array[mid] > number:
            final = mid - 1


def linearsearch(numbersarray, numbertosearch):
    for k in range(0, len(numbersarray)):
        if numbersarray[k] == numbertosearch:
            return k
    return None

