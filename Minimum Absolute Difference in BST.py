class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def f(self, node):
        max_left_v = max_right_v = - float('inf')
        min_left_v = min_right_v = float('inf')
        left_d = right_d = float('inf')
        if node.left:
            [max_left_v, min_left_v, left_d] = self.f(node.left)
        if node.right:
            [max_right_v, min_right_v, right_d] = self.f(node.right)
        min_v = min(node.val, min_left_v, min_right_v)
        max_v = max(node.val, max_left_v, max_right_v)
        current_d = min(left_d, right_d, (node.val - max_left_v), (min_right_v - node.val))
        return max_v, min_v, current_d


    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.f(root)
