class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        Q = [root]
        answer = []
        while Q:
            n = len(Q)
            for i in range(n):
                u = Q.pop(0)
                if u.left:
                    Q.append(u.left)
                if u.right:
                    Q.append(u.right)
            answer.append(u.val)
        return answer