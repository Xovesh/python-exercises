from Trees import TreeNode, Mirror, TreeSearch

magictree = TreeNode.TreeNode("A")
magictree.left = TreeNode.TreeNode("B")
magictree.right = TreeNode.TreeNode("C")
magictree.left.left = TreeNode.TreeNode("D")
magictree.left.right = TreeNode.TreeNode("E")
magictree.left.left.left = TreeNode.TreeNode("H")
magictree.left.left.right = TreeNode.TreeNode("I")
magictree.left.right.right = TreeNode.TreeNode("J")
magictree.right.left = TreeNode.TreeNode("F")
magictree.right.right = TreeNode.TreeNode("G")

print(TreeSearch.TreeSearch.breadthfirstsearch(magictree))
a = Mirror.mirror(magictree)
print(TreeSearch.TreeSearch.breadthfirstsearch(a))
print(Mirror.ismirror(magictree, a))
