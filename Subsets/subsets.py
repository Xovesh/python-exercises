def subsets(original, subset, i):
    if i == len(original):
        print(subset)
    else:
        subset[i] = None
        subsets(original, subset, i + 1)
        subset[i] = original[i]
        subsets(original, subset, i + 1)