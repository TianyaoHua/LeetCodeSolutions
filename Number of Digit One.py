class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        l = len(s)
        base = 1
        basic = 0
        sum_1 = 0
        for i in range(l-1, -1, -1):
            sum_1 += int(s[i])*basic
            if int(s[i]) > 1:
                sum_1 += base
            if i > 0 and s[i-1] == '1':
                sum_1 += int(s[i:])+1
            basic = basic * 10 + base
            base *= 10
        return sum_1 + int(s[-1] == '1')

solution = Solution()
print(solution.countDigitOne(2))