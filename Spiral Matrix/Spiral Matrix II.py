class Solution(object):
    def generateMatrix(self, n):
        matrix = [[-1 for i in range(n)] for i in range(n)]
        L = n*n
        direction = 1
        i = 0
        j = 0
        length = 0
        while length < L:
            while i < n and j < n and matrix[i][j] == -1:
                matrix[i][j] = length+1
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
        return matrix

if __name__ == "__main__":
    solution = Solution()
    print(solution.generateMatrix(3))


