# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def walk(self, node, dict):
        if node:
            if node.val not in dict:
                dict[node.val] = 0
            dict[node.val] += 1
            self.walk(node.left, dict)
            self.walk(node.right,dict)

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dict = {}
        self.walk(root, dict)
        answer = []
        max_frequency = 0
        for key in dict:
            if dict[key] > max_frequency:
                max_frequency = dict[key]
                answer = [key]
            elif dict[key] == max_frequency:
                answer.append(key)
        return answer