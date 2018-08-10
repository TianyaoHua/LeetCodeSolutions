class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def height(self, node, h):
        if node:
            d1 = self.height(node.left, h)
            d2 = self.height(node.right, h)
            d = max(d1, d2) + 1
            if d not in h:
                h[d] = []
            h[d].append(node)
            return d
        else:
            return 0

    def isequal(self, s, t):
        Q1 = [s]
        Q2 = [t]
        while Q1:
            if not Q2:
                return False
            u1 = Q1.pop()
            u2 = Q2.pop()
            if u1.val != u2.val:
                return False
            if u1.left:
                Q1.append(u1.left)
            if u1.right:
                Q1.append(u1.right)
            if u2.left:
                Q2.append(u2.left)
            if u2.right:
                Q2.append(u2.right)
        return bool(Q2)

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        h = {}
        _ = self.height(s, h)
        dt = self.height(t, {})
        for node in h[dt]:
            if self.isequal(node, t):
                return True
        return False


