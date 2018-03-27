class Solution(object):
    def half_ceil(self, number):
        return int(number/2) + number%2

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for i in range(self.half_ceil(N)):
            for j in range(i, N-i-1):
                temp = matrix[N-1-j][i]
                matrix[N-1-j][i] = matrix[N-1-i][N-1-j]
                matrix[N-1-i][N-1-j] = matrix[j][N-1-i]
                matrix[j][N-1-i] = matrix[i][j]
                matrix[i][j] = temp
        return matrix

if __name__=="__main__":
    solution = Solution()
    array =  []
    print(array)
    answer = solution.rotate(array)
    print(answer)
