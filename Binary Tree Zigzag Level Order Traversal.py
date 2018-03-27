class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        Q = [root]
        t = []
        flag = True
        while Q:
            n = len(Q)
            for i in range(n):
                u = Q[0]
                Q.remove(Q[0])
                if u:
                    Q.append(u.left)
                    Q.append(u.right)
            v =[node.val for node in Q if node]
            if v:
                if flag:
                    t.append(v)
                    flag = not flag
                else:
                    t.append(v[::-1])
                    flag = not flag
        return t