class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0])
        s = -float('inf')
        left = [0 for i in range(m)]
        right = [m for i in range(m)]
        height = [0 for i in range(m)]
        for i in range(n):
            c_left = 0
            c_right = m
            for j in range(m):
                if matrix[i][j] == '1':
                    height[j] = height[j] + 1
                    left[j] = max(left[j], c_left)
                else:
                    height[j] = 0
                    left[j] = 0
                    c_left = j + 1
            for j in range(m-1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], c_right)
                else:
                    right[j] = m
                    c_right = j
            for j in range(m):
                s = max(s, (min(height[j], right[j] - left[j]))**2)
        return s


solution = Solution()
matrix = [["0","1","0","1","0","0"],["0","0","1","1","0","1"]]
print(solution.maximalSquare(matrix))