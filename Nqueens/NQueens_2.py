from copy import deepcopy

class Solution(object):
    def dfs(self, space, visited, n, N, answer):
        if n == N:
            a_solution = []
            for position in visited:
                a_solution.append('.'*(position[1])+'Q'+'.'*(N-1-position[1]))
            answer.append(a_solution)
        else:
            for i in range(len(space[0])):
                temp_space = deepcopy(space)
            for i in range(N):
                if space[n][i]:
                    temp = visited[:]
                    temp_space = deepcopy(space)
                    visited.append([n,i])
                    for j in range(N):
                        space[n][j] = 0
                    for j in range(n, N):
                        space[j][i] = 0
                    j = n+1
                    k = i+1
                    while j < N and k < N:
                        space[j][k] = 0
                        j += 1
                        k += 1
                    j = n+1
                    k = i-1
                    while j < N and k > -1:
                        space[j][k] = 0
                        j += 1
                        k -= 1
                    self.dfs(space, visited, n+1, N, answer)
                    visited = temp[:]
                    space = deepcopy(temp_space)


    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        space = []
        for i in range(n):
            space.append([])
            for j in range(n):
                space[i].append(1)
        answer = []
        #positions = []
        self.dfs(space, [], 0, n, answer)
        # answer_lists = []
        # for position in positions:
        #     answer = []
        #     for element in position:
        #         answer.append('.'*(element[1])+'Q'+'.'*(n-1-element[1]))
        #     answer_lists.append(answer)
        return answer

if __name__ == "__main__":
    solution = Solution()
    answer = solution.solveNQueens(9)
    print(answer)
    print(len(answer))

