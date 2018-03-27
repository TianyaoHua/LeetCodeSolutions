class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        m = len(matrix[0])
        for element in matrix:
            element.append(float('inf'))
        matrix.append([float('inf')]*m)
        if target<matrix[0][0]:
            return False
        i = 0
        j = n-1
        p = n//2
        while not (matrix[p][0] <= target and matrix[p+1][0]>target):
            if matrix[p][0] > target:
                j = p
                p = (i+p) >> 1
            else:
                i = p
                p = ((p+j) >> 1) + 1
        i = 0
        j = m-1
        x = m//2
        while not (matrix[p][x] <= target and matrix[p][x+1]>=target):
            if matrix[p][x] < target:
                i = x
                x = ((x+j) >> 1) + 1
            else:
                j = x
                x = (x+i) >> 1
        if matrix[p][x] == target or matrix[p][x+1] == target:
            return True
        else:
            return False

if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,3,5]]
    print(solution.searchMatrix(matrix,5))