class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def topological_sort(self, root):
        Q = [root]
        s = []
        while Q:
            u = Q.pop(0)
            if u.left:
                Q.append(u.left)
            if u.right:
                Q.append(u.right)
            s.append(u)
        return s

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s = self.topological_sort(root)
        n = len(s)
        d = {}
        for i in range(n-1, -1, -1):
            max_path = s[i].val
            if s[i].left and d[s[i].left] + s[i].val > max_path:
                max_path = d[s[i].left] + s[i].val
            if s[i].right and d[s[i].right] + s[i].val > max_path:
                max_path = d[s[i].right] + s[i].val
            d.update({s[i]: max_path})
        u_d = {}
        for i in range(n-1, -1, -1):
            max_path = d[s[i]]
            if s[i].left and s[i].right and s[i].val + d[s[i].left] + d[s[i].right] > max_path:
                max_path = s[i].val + d[s[i].left] + d[s[i].right]
            u_d.update({s[i]: max_path})

        return max(u_d.values())



