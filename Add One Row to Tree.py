# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            v = TreeNode(v)
            v.right = root
            return v
        h = 1
        Q = [root]
        while Q and h < d-1:
            h += 1
            l = len(Q)
            for i in range(l):
                u = Q.pop()
                if u.left:
                    Q.append(u.left)
                if u.right:
                    Q.append(u.right)
        for u in Q:
            v1 = TreeNode(v)
            v2 = TreeNode(v)
            v1.left = u.left
            v2.right = u.right
            u.left = v1
            u.right = v2
        return root