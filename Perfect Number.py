class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        bound = int(num**0.5)+1
        s = 1
        for i in range(2, bound):
            if num%i == 0:
                s += i
                s += num//i
        return s == num

print(Solution().checkPerfectNumber(6))