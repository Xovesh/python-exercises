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

