import itertools
class Solution(object):
    def DFS(self, array, answer,track):
        n = len(array)
        if n == 1:
            answer.append(array[0])
        else:
            low = max(1, track - 2)
            for i in range(low, n, 2):
                if array[i] == '-':
                    self.DFS((array[0:i - 1] + [array[i - 1] - array[i + 1]] + array[i + 2:]), answer, i)
                elif array[i] == '+':
                    self.DFS((array[0:i - 1] + [array[i - 1] + array[i + 1]] + array[i + 2:]), answer, i)
                else:
                    self.DFS((array[0:i - 1] + [array[i - 1] * array[i + 1]] + array[i + 2:]), answer, i)



    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        p = 0
        array = []
        for i in range(len(input)):
            if input[i] == '-' or input[i] == '+' or input[i] == '*':
                array.append(int(input[p:i]))
                array.append(input[i])
                p = i+1
        array.append(int(input[p:]))
        answer = []
        self.DFS(array, answer, 0)
        return answer

solution = Solution()
input='2-1-1'
print(solution.diffWaysToCompute(input))