# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def value(self, node, dict):
        if not node:
            return 0
        elif node in dict:
            return dict[node]
        else:
            money1 = self.value(node.lert, dict) + self.value(node.right ,dict)
            money2 = node.val
            if node.left:
                money2 += (self.value(node.left.left, dict) + self.value(node.left.right, dict))
            if node.right:
                money2 += (self.value(node.right.left, dict) + self.value(node.right.right, dict))
            money = max(money1, money2)
            dict.update({node: money})
            return money
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.value(root, {})