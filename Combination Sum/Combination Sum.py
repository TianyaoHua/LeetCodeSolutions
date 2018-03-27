class Solution(object):
    def dfs(self, candidates, visited, n, N, routes):
        if n == 0:
            routes.append(visited)
        elif n > 0:
            for i in range(len(candidates)):
                visited.append(candidates[i])
                self.dfs(candidates[i:], visited, n-1, N, routes)
                visited = visited[0: N-n]


    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        solutions = []
        if len(candidates) > 0:
            candidates.sort()
            upper_n = int(target/candidates[0])
            lower_n = int(target/candidates[-1])
            for n in range(lower_n, upper_n + 1):
                routes = []
                self.dfs(candidates, [],n,n, routes)
                for element in routes:
                    if sum(element) == target:
                        solutions.append(element)
        return solutions