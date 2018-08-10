class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        h = {}
        for candy in candies:
            if candy not in h:
                h[candy] = 0
            h[candy] += 1
        kinds = list(h.keys())
        kinds.sort(key=lambda x: h[x], reverse=True)
        budget = 0
        answer = 0
        i = 0
        n = len(kinds)
        while i < n and h[kinds[i]] > 1:
            answer += 1
            budget += (h[kinds[i]] - 2)
            i += 1
        if budget >= n-i:
            return answer + (n-i)
        else:
            answer += budget
            answer += (n-i-budget)//2
            return answer
print(Solution().distributeCandies([1,1,2,3]))