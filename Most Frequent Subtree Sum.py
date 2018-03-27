class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def treesum(self, node, dict):
        if node:
            subtreesum = node.val + self.treesum(node.left,dict) + self.treesum(node.right,dict)
            if subtreesum not in dict:
                dict[subtreesum] = 0
            dict[subtreesum] += 1
            return subtreesum
        else:
            return 0

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dict = {}
        self.treesum(root, dict)
        answer = []
        max_frequency = 0
        for key in dict:
            if dict[key] > max_frequency:
                answer = [key]
                max_frequency = dict[key]
            elif dict[key] == max_frequency:
                answer.append(key)
        return answer