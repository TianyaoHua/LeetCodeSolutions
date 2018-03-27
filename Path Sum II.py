class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        Q = [root]
        d = {root: root.val}
        p = {root: None}
        s = []
        while Q:
            u = Q[0]
            Q.remove(u)
            if u.left:
                d.update({u.left: d[u]+u.left.val})
                p.update({u.left: u})
                Q.append(u.left)
            if u.right:
                d.update({u.right: d[u] + u.right.val})
                p.update({u.ritht: u})
                Q.append(u.right)
            if not (u.left or u.right) and d[u] == sum:
                s.append(u)
        solution = []
        for leaf in s:
            answer = []
            node = leaf
            while node:
                answer.append(node.val)
                node = p[node]
            solution.append(answer[::-1])
