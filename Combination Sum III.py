from itertools import combinations
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        answer = []
        permutation = list(combinations(range(1,10), k))
        for p in permutation:
            if sum(p) == n:
                answer.append(p)
        return answer
