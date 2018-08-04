def subsets(original, subset, i):
    if i == len(original):
        print(subset)
    else:
        subset[i] = None
        subsets(original, subset, i + 1)
        subset[i] = original[i]
        subsets(original, subset, i + 1)


original = [1, 2, 3]
subset = []
for i in original:
    subset.append(None)
subsets(original, subset, 0)
