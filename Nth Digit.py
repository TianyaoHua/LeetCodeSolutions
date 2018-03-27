class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        x = 9
        y = 0
        while x < n:
            y = x
            i += 1
            x += i*9*(10**(i-1))
        position = (n-y) % i
        index = (n - y) // i + bool(position != 0)
        return str((10**(i-1)) + (index-1))[position-1]


solution = Solution()
print(solution.findNthDigit(3))