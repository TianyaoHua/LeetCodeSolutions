class Solution(object):
    def dfs(self, candidates, n_candidates, visited, target, solutions, s_sum):
        if s_sum == target:
            solutions.append(visited)
        elif s_sum < target:
            i = 0
            while i < n_candidates:
                element = candidates[i]
                visited_append = visited + [element]
                s_sum_append = s_sum + element
                self.dfs(candidates[i:], n_candidates-i, visited_append, target, solutions, s_sum_append)
                i += 1

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        solutions = []
        candidates.sort()
        if len(candidates) > 0:
            solutions = []
            self.dfs(candidates, len(candidates),[], target, solutions, 0)
        return solutions


