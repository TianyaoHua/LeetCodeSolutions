class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderwalk(self, node, mistake, order):
        if node:
            self.inorderwalk(node.left, mistake, order)
            if order[0].val >= node.val:
                mistake.append(order[0])
                mistake.append(node)
            order[0] = node
            self.inorderwalk(node.right, mistake, order)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        mistake = []
        tail = TreeNode(-float('inf'))
        order = [tail]
        self.inorderwalk(root, mistake, order)
        if len(mistake) == 2:
            temp = mistake[0].val
            mistake[0].val = mistake[1].val
            mistake[1].val = temp
        else:
            temp = mistake[0].val
            mistake[0].val = mistake[3].val
            mistake[3].val = temp
        return mistake

root = TreeNode(0)
left = TreeNode(1)

root.left = left
solution = Solution()
solution.isValidBST(root)
