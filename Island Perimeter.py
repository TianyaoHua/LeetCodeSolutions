class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        answer = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if i-1 < 0 or grid[i-1][j]==0:
                        answer += 1
                    if i+1 >= n or grid[i+1][j] == 0:
                        answer += 1
                    if j - 1 < 0 or grid[i][j-1] == 0:
                        answer += 1
                    if j+1 >= m or grid[i][j+1] == 0:
                        answer += 1
        return answer

print(Solution().islandPerimeter([[1]]))