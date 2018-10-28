def spread(tree):
    if tree is None:
        return None
    else:
        return copy(tree, tree.val)

def copy(tree, number):
    if tree is None:
        return None
    else:
        tree.val = number
        tree.left = copy(tree.left, number)
        tree.right = copy(tree.right, number)
        return tree

