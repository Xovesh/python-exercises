def prefix(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    elif tree1 is None and tree2 != None:
        return True
    elif tree1 is not None and tree2 is None:
        return False
    else:
        if tree1.val != tree2.val:
            return False
        else:
            return prefix(tree1.left, tree2.left) and prefix(tree1.right, tree2.right)
