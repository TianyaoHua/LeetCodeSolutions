class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        table = [[0 for i in range(n)] for i in range(m)]
        table[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    table[i][j] = min(table[i - 1][j] + grid[i][j], table[i][j-1]+grid[i][j])
                elif i == 0 and j > 0:
                    table[i][j] = table[i][j-1] + grid[i][j]
                elif i > 0 and j == 0:
                    table[i][j] = table[i-1][j] + grid[i][j]
        return table[m-1][n-1]

if __name__ == "__main__":
    solution = Solution()
    grid=[[1,3,1],[1,5,1],[4,2,1]]
    answer = solution.minPathSum(grid)
    print(answer)
