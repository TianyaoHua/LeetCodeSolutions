# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Q = [root]
        s = 0
        n = {root: root.val}
        while Q:
            u = Q.pop(0)
            if u.left:
                n.update({u.left: n[u]*10 + u.left.val})
                Q.append(u.left)
            if u.right:
                n.update({u.right: n[u]*10 + u.right.val})
                Q.append(u.right)
            if not (u.left or u.right):
                s += n[u]
        return s

