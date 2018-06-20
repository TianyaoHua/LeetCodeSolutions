class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def f(self, node, outer):
        if node:
            right_sum = self.f(node.right, outer)
            node.val += (outer + right_sum)
            left_sum = self.f(node.left, node.val)
            return left_sum + node.val - outer
        else:
            return 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.f(root, 0)
        return root