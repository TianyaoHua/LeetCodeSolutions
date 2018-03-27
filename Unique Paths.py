class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        table  = [[0 for i in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    table[i][j] = 1
                else:
                    table[i][j] = table[i-1][j] + table[i][j-1]
        return table[m-1][n-1]

if __name__ == "__main__":
    solution = Solution()
    answer = solution.uniquePaths(3,3)
    print(answer)
