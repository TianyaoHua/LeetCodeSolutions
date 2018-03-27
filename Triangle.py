class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        for i in range(1, n):
            triangle[i][0] += triangle[i-1][0]
            triangle[i][i] += triangle[i-1][i-1]
            for j in range(1, i):
                triangle[i][j] = min(triangle[i][j] + triangle[i-1][j-1],triangle[i][j] + triangle[i-1][j])
        return min(triangle[n-1])


solution = Solution()
triangle = [
     [-1],
    [2,3],
   [1,-1,-3]
]
print(solution.minimumTotal(triangle))