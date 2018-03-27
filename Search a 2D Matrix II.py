class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        i = 0
        while i < n and not matrix[i][0] <= target <= matrix[i][-1]:
            i += 1
        return i < n and target in matrix[i]

solution = Solution()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(solution.searchMatrix(matrix,target))