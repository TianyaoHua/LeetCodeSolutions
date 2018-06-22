# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def f(self, node):
        if node:
            tilt_left, sum_left = self.f(node.left)
            tilt_right, sum_right = self.f(node.right)
            return tilt_left+tilt_right+abs(sum_left-sum_right), sum_left+sum_right+node.val
        else:
            return 0, 0
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        answer, _ = self.f(root)
        return answer


