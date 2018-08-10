class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def merge(self, t1, t2):
        if t2.left:
            if t1.left:
                t1.left.val += t2.left.val
                self.merge(t1.left, t2.left)
            else:
                t1.left = t2.left
        if t2.right:
            if t1.right:
                t1.right.val += t2.right.val
                self.merge(t1.right, t2.right)
            else:
                t1.right = t2.right
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        elif not t2:
            return t1
        else:
            t1.val += t2.val
            self.merge(t1,t2)
            return t1
