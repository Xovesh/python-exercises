from Trees import TreeNode, Prefix

magictree = TreeNode.TreeNode("A")
magictree.left = TreeNode.TreeNode("B")
magictree.right = TreeNode.TreeNode("C")
magictree.left.right = TreeNode.TreeNode("E")
magictree.right.left = TreeNode.TreeNode("F")
magictree.right.right = TreeNode.TreeNode("G")

magictree2 = TreeNode.TreeNode("A")
magictree2.left = TreeNode.TreeNode("B")
magictree2.right = TreeNode.TreeNode("C")
magictree2.left.left = TreeNode.TreeNode("D")
magictree2.left.right = TreeNode.TreeNode("E")
magictree2.left.left.left = TreeNode.TreeNode("H")
magictree2.left.left.right = TreeNode.TreeNode("I")
magictree2.left.right.right = TreeNode.TreeNode("J")
magictree2.right.left = TreeNode.TreeNode("F")
magictree2.right.right = TreeNode.TreeNode("G")

print(Prefix.prefix(magictree, magictree2))
