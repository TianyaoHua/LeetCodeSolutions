# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        Q = [root]
        while Q:
            u = Q.pop(0)
            temp = u.left
            u.left = u.right
            u.right = temp
            if u.left:
                Q.append(u.left)
            if u.right:
                Q.append(u.right)
        return root