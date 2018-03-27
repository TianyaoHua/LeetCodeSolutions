# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def travelsal(self, node, solution):
        if node:
            solution.append(node.val)
            self.travelsal(node.left)
            self.travelsal(node.right)
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        solution = []
        self.travelsal(root, solution)