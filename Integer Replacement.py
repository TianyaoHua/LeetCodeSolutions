class Solution(object):
    def times(self, n, dict):
        if n in dict:
            return dict[n]
        if n%2 == 0:
            t = 1 + self.times(n//2, dict)
        else:
            t = min(self.times((n+1)//2, dict)+2, self.times((n-1),dict)+1)
        dict.update({n:t})
        return t
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.times(n,{1:0})


solution = Solution()
print(solution.integerReplacement(10000))