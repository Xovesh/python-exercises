from Trees import TreeNode
def spread(tree):
    if tree is None:
        return None
    else:
        return copy(tree, tree.val)

def copy(tree, number):
    if tree is None:
        return None
    else:
        newtree = TreeNode.TreeNode(number)
        newtree.left = copy(tree.left, number)
        newtree.right = copy(tree.right, number)
        return newtree

