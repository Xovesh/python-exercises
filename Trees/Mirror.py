from Trees import TreeNode
def mirror(tree):
    if tree is None:
        return None
    else:
        mirrortree = TreeNode.TreeNode(tree.val)
        mirrortree.left = mirror(tree.right)
        mirrortree.right = mirror(tree.left)
        return mirrortree

def ismirror(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    elif tree1 is None and tree2 is not None:
        return False
    elif tree1 is not None and tree2 is None:
        return False
    else:
        if tree1.val == tree2.val:
            return ismirror(tree1.left, tree2.right) and ismirror(tree1.right, tree2.left)
        else:
            return False
