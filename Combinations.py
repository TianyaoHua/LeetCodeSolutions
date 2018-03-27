class Solution(object):
    def dfs(self, remains,  visited, n, k, solution):
        if n < k:
            ln = len(remains)
            lv = len(visited)
            for i in range(ln):
                visited.append(remains[i])
                self.dfs(remains[i+1:], visited, n+1, k, solution)
                visited = visited[0:lv]
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
        if k <= n//2:
            self.dfs(remains, [], 0, k, solution)
        else:
            self.dfs_2(remains, remains, 0, n-k, solution)
        return solution


if __name__ == "__main__":
    solution = Solution()
    answer = solution.combine(20,0)
    print(answer)
