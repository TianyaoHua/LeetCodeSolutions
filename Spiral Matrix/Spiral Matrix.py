class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if not m:
            return []
        n = len(matrix[0])
        L = n*m
        direction = 1
        corner = [0,n-1]
        i = 0
        j = 0
        answer = []
        length = 0
        while length < L:
            while i < m and j < n and matrix[i][j] != 'v':
                answer.append(matrix[i][j])
                matrix[i][j] = 'v'
                length += 1
                if direction == 1:
                    j += 1
                elif direction == 2:
                    i += 1
                elif direction == 3:
                    j -= 1
                else:
                    i -= 1
            if direction == 1:
                j -= 1
                i += 1
                direction = 2
            elif direction == 2:
                i -= 1
                j -= 1
                direction = 3
            elif direction == 3:
                j += 1
                i -= 1
                direction = 4
            else:
                i += 1
                j += 1
                direction = 1
        return answer

if __name__ == "__main__":
    solution = Solution()
    matrix = []
    print(solution.spiralOrder(matrix))


