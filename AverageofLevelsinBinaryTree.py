# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        Q = [root]
        answer = []
        while Q:
            n = len(Q)
            s = 0
            for i in range(n):
                u = Q.pop(0)
                s += u.val
                if u.left:
                    Q.append(u.left)
                if u.right:
                    Q.append(u.right)
            answer.append(s/n)
        return answer