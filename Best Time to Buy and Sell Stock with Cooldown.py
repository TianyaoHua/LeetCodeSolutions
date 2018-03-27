class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        differ = [0] + [prices[i] - prices[i-1] for i in range(1, len(prices))]
        n = len(differ)
        add = [0 for i in range(n)]
        exclude = [0 for i in range(n)]
        add[1] = differ[1]
        for i in range(2, n):
            exclude[i] = max(exclude[i-1], add[i-1])
            add[i] = max(add[i-1] + differ[i], exclude[i-2]+differ[i])
        return max(add[-1], exclude[-1])

solution = Solution()
print(solution.maxProfit([123,32,4134,5245,134,3,14,311,34,5145,14,534,5,353,134]))