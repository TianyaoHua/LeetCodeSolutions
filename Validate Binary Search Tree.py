
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderwalk(self, node, order):
        if node:
            self.inorderwalk(node.left, order)
            order.append(node.val)
            self.inorderwalk(node.right,order)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        order = []
        self.inorderwalk(root, order)
        n = len(order)
        for i in range(1, n):
            if order[i] <= order[i-1]:
                return False
        return True


root = TreeNode(1)
left = TreeNode(1)
right = TreeNode(3)
root.left = left
root.right = right
solution = Solution()
solution.isValidBST(root)