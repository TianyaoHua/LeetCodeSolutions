class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        a = [[Profits[i], Capital[i]] for i in range(len(Profits))]
        while k > 0:
            candidate = list(filter(lambda x: x[1] <= W, a))
            if not candidate:
                return W
            optimal = max(candidate)
            W += optimal[0]
            a.remove(optimal)
            k -= 1
        return W


print(Solution().findMaximizedCapital(2,0,[1,2,3],[0,1,1]))