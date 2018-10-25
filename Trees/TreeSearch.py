class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None # TreeNode Type
        self.right = None # TreeNode Type

class TreeSearch:

    @ staticmethod
    def breadthfirstsearch(tree):
        # for this algorithm we need a queue, i'm going to use a list to ease it
        # dequeue as [].pop(0)
        # enqueue as [].append(s)
        queue = []
        result = ""
        # enqueue the root
        queue.append(tree)

        while queue:
            # dequeue the first in the queue
            x = queue.pop(0)

            # enqueue the left and right of x to the queue
            if x is not None:
                result += x.val
                queue.append(x.left)
                queue.append(x.right)

        return result

    @ staticmethod
    def depthfirstsearchpreorder(tree):
        # for this algorithm we need a stack, i'm going to use a list to ease it
        # pop as [].pop()
        # push as [].append(s)
        stack = []
        result = ""
        # push the root
        stack.append(tree)

        while stack:
            # pop the top element of the stack
            x = stack.pop()

            # push first the right and then the left
            if x is not None:
                result += x.val
                stack.append(x.right)
                stack.append(x.left)

        return result

# check the github picture to understand better this tree.
magictree = TreeNode("A")
magictree.left = TreeNode("B")
magictree.right = TreeNode("C")
magictree.left.left = TreeNode("D")
magictree.left.right = TreeNode("E")
magictree.left.left.left = TreeNode("H")
magictree.left.left.right = TreeNode("I")
magictree.left.right.right = TreeNode("J")
magictree.right.left = TreeNode("F")
magictree.right.right = TreeNode("G")

print(TreeSearch.breadthfirstsearch(magictree))
print(TreeSearch.depthfirstsearchpreorder(magictree))
