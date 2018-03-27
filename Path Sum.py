class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        Q = [root]
        d = {root: root.val}
        s = []
        while Q:
            u = Q[0]
            if u.left:
                d.update({u.left: d[u]+u.left.val})
                Q.append(u.left)
            if u.right:
                d.update({u.right: d[u] + u.right.val})
                Q.append(u.right)
            if not (u.left or u.right):
                s.append(d[u])
        return sum in s