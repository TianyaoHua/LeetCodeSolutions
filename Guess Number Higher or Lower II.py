class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = [[0 for i in range(n)] for j in range(n)]
        for l in range(1, n):
            for i in range(n-l):
                j = i+l
                c = 1000000
                for k in range(i+1, j):
                    c = min(c, k+1 + max(table[i][k-1],table[k+1][j]))
                c = min(c, i+1+table[i+1][j],j+1+table[i][j-1])
                table[i][j] = c
        return table[0][n-1]


solution = Solution()
print(solution.getMoneyAmount(1))
