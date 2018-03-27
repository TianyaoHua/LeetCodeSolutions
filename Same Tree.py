# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        Q = [root]
        while Q:
            n = len(Q)
            for i in range(n):
                u = Q[0]
                Q.remove(Q[0])
                if u:
                    Q.append(u.left)
                    Q.append(u.right)
            v =[]
            for node in Q:
                if node:
                    v.append(node.val)
                else:
                    v.append(None)
            if v[::-1] != v:
                return False
        return True
