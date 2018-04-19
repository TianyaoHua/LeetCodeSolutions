# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        answers = []
        Q = [root]
        while Q:
            n = len(Q)
            max_value = -float('inf')
            for _ in range(n):
                u = Q.pop(0)
                max_value = max(max_value, u.val)
                if u.left:
                    Q.append(u.left)
                if u.right:
                    Q.append(u.right)
            answers.append(max_value)
        return answers