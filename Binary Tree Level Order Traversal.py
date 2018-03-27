# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        Q = [root]
        t = []
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
                t.append(v)
        return t