class Solution(object):
    def digits(self, num):
        d = []
        if not num:
            return [0]
        while num > 0:
            d.append((num % 10)**2)
            num = num // 10
        return d[::-1]


    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while n not in s:
            s.update({n})
            d = self.digits(n)
            n = sum(d)
        return n == 1

solution = Solution()
n = 8
print(solution.isHappy(n))
