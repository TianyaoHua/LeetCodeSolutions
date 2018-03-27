class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Q = [root]
        while Q:
            n = len(Q)
            left = Q[0].val
            for i in range(n):
                u = Q.pop(0)
                if u.left:
                    Q.append(u.left)
                if u.right:
                    Q.append(u.right)
        return left
