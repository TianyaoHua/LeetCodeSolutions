class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        minv = 1
        maxv = n
        diff = 2
        direction = 1
        while minv != maxv:
            if direction == 1:
                if (maxv - minv) % diff == 0:
                    maxv -= diff >> 1
                minv += diff >> 1
                direction = 0
            elif direction == 0:
                if (maxv - minv) % diff == 0:
                    minv += diff >> 1
                maxv -= diff >> 1
                direction = 1
            diff = diff << 1
        return minv

solution = Solution()
print(solution.lastRemaining(1054))