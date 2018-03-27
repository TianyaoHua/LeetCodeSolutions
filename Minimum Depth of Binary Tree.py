class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Q = [root]
        h = 0
        while Q:
            n = len(Q)
            for i in range(n):
                u = Q[0]
                Q.remove(Q[0])
                if u:
                    Q.append(u.left)
                    Q.append(u.right)
                if not(u.left or u.right):
                    return h