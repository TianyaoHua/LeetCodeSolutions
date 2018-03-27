class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if not matrix[i][j]:
                    matrix[i][j] = '0'
                    for k in range(m):
                        matrix[i][k] = bool(matrix[i][k])*'0'
                    for k in range(n):
                        matrix[k][j] = bool(matrix[k][j])*'0'
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '0':
                    matrix[i][j] =0
        return matrix

if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,2,3],[2,3,0],[4,5,6]]
    print(solution.setZeroes(matrix))

