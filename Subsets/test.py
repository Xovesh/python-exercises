from Subsets.subsets import *
original = [1, 2, 3]
subset = []
for i in original:
    subset.append(None)
subsets(original, subset, 0)