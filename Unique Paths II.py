class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        table = [[0 for i in range(n)] for i in range(m)]
        table[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    table[i][j] = 0
                elif i > 0 and j > 0:
                    table[i][j] = table[i - 1][j] + table[i][j - 1]
                elif i == 0 and j > 0:
                    table[i][j] = table[i][j-1]
                elif i > 0 and j == 0:
                    table[i][j] = table[i-1][j]
        return table[m-1][n-1]

if __name__ == "__main__":
    solution = Solution()
    obstacleGrid=[[0,0]]
    answer = solution.uniquePathsWithObstacles(obstacleGrid)
    print(answer)
