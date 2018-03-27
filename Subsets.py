class Solution(object):
    def dfs(self, remains,  visited, n, k, solution):
        if n < k:
            solution.append(visited)
            ln = len(remains)
            lv = len(visited)
            for i in range(ln):
                temp = visited[:]
                temp.append(remains[i])
                self.dfs(remains[i+1:], temp, n+1, k, solution)
        else:
            solution.append(visited)
    def dfs_2(self, remains, visited, n, k, solution):
        if n < k:
            ln = len(remains)
            for i in range(ln):
                temp = visited[:]
                temp.remove(remains[i])
                self.dfs_2(remains[i+1:], temp, n+1, k, solution)
        else:
            solution.append(visited)
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        remains = [i+1 for i in range(n)]
        solution = []
        self.dfs(remains, [], 0, k, solution)
        return solution


if __name__ == "__main__":
    solution = Solution()
    answer = solution.combine(3,3)
    print(answer)