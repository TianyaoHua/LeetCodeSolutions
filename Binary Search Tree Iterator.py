# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def inorder_walk(self, node, order):
        if node:
            self.inorder_walk(node.left, order)
            order.append(node.val)
            self.inorder_walk(node.right, order)

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.order = []
        self.inorder_walk(root, self.order)
        self.index = 0
        self.n = len(self.order)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < self.n

    def next(self):
        """
        :rtype: int
        """
        answer = self.order[self.index]
        self.index += 1
        return answer

root = TreeNode(1)
i = BSTIterator(root)
print(i.next())
