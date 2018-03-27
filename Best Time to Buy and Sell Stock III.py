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
        t_right = [0 for i in range(n)]
        t_max_right = [0 for i in range(n)]
        t_right[-1] = diff[-1]
        t_max_right[-1] = diff[-1]
        for i in range(n-2, -1, -1):
            if diff[i] + t_right[i+1] > diff[i]:
                t_right[i] = diff[i] + t_right[i+1]
            else:
                t_right[i] = diff[i]
            if t_right[i] > t_max_right[i+1]:
                t_max_right[i] = t_right[i]
            else:
                t_max_right[i] = t_max_right[i+1]
        t_left = [0 for i in range(n)]
        t_max_left = [0 for i in range(n)]
        t_left[0] = 0
        t_max_left[0] = 0
        for i in range(1, n):
            if diff[i] + t_left[i-1] > diff[i]:
                t_left[i] = diff[i] + t_left[i-1]
            else:
                t_left[i] = diff[i]
            if t_left[i] > t_max_left[i-1]:
                t_max_left[i] = t_left[i]
            else:
                t_max_left[i] = t_max_left[i-1]
        profit = max(t_max_left[-1], t_max_right[0])
        for i in range(0, n-1):
            if profit < t_max_right[i+1] + t_max_left[i]:
                profit = t_max_right[i+1] + t_max_left[i]
        return profit


solution = Solution()
prices = [2,1,2,0,1]
print(solution.maxProfit(prices))