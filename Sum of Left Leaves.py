# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Q = [root]
        answer = 0
        while Q:
            u = Q.pop()
            if u.left:
                Q.append(u.left)
                if not (u.left.left or u.left.right):
                    answer += u.left.val
            if u.right:
                Q.append(u.right)
        return answer
