# Definition for a binary tree node.
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n < 1:
            return []
        table = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            table[i][i] = 1
        for l in range(1, n):
            for i in range(n-l):
                j = i + l
                c = 0
                for k in range(i+1, j):
                    c += table[i][k-1]*table[k+1][j]
                c += table[i+1][j]
                c += table[i][j-1]
                table[i][j] = c
        return table[0][n-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.generateTrees(10))



