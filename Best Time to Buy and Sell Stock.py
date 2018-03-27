class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        diff = [0]
        for i in range(1, n):
            diff.append(prices[i]-prices[i-1])
        t = [0 for i in range(n)]
        t[-1] = diff[-1]
        for i in range(n-2, -1, -1):
            if diff[i] + t[i+1] > diff[i]:
                t[i] = diff[i] + t[i+1]
            else:
                t[i] = diff[i]
        return max(t)

solution = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(solution.maxProfit(prices))


