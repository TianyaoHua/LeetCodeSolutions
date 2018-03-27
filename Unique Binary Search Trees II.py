# Definition for a binary tree node.
import copy
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def insert(self, root, z):
        y = None
        x = root
        while x:
            y = x
            if z.val > x.val:
                x = x.right
            else:
                x = x.left
        if not y:
            root = z
        elif z.val < y.val:
            y.left = z
        else:
            y.right = z
        return root

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n < 1:
            return []
        table = [[[] for i in range(n)] for j in range(n)]
        for i in range(1, n+1):
            root = TreeNode(i)
            table[i-1][i-1].append(root)
        for l in range(1, n):
            for i in range(n-l):
                j = i + l
                for k in range(i+1, j):
                    root = TreeNode(k+1)
                    for m in range(len(table[i][k-1])):
                        for p in range(len(table[k+1][j])):
                            root_k = copy.deepcopy(root)
                            root_k.left = table[i][k-1][m]
                            root_k.right = table[k+1][j][p]
                            table[i][j].append(root_k)
                root = TreeNode(i+1)
                for m in range(len(table[i+1][j])):
                    root_i = copy.deepcopy(root)
                    root_i.right = table[i+1][j][m]
                    table[i][j].append(root_i)
                root = TreeNode(j+1)
                for m in range(len(table[i][j-1])):
                    root_j = copy.deepcopy(root)
                    root_j.left = table[i][j-1][m]
                    table[i][j].append(root_j)
        return table[0][n-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.generateTrees(4))



