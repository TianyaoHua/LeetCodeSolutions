class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        m = len(matrix[0])
        answer = []
        i, j,direction = 0, 0, [-1, 1]
        while 0 <= i < n and 0 <= j < m:
            answer.append(matrix[i][j])
            i, j = i + direction[0],j + direction[1]
            if i >= n:
                i -= 1
                j += 2
                direction[0], direction[1] = -direction[0], -direction[1]
            elif i < 0:
                i = 0
                if j >= m:
                    i += 1
                    j -= 1
                direction[0], direction[1] = -direction[0], -direction[1]
            elif j < 0:
                j += 1
                if i >= n:
                    i -=1
                    j += 1
                direction[0], direction[1] = -direction[0], -direction[1]
            elif j >= m:
                j -= 1
                i += 2
                direction[0], direction[1] = -direction[0], -direction[1]
        return answer

print(Solution().findDiagonalOrder([[1,2]]))