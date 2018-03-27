class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i= 0
        j = x
        p = x >> 1
        while not p*p <= x < (p+1)*(p+1):
            if p*p > x:
                j = p
                p = (i+p) >> 1
            else:
                i = p
                p = ((p+j) >> 1) + 1
        return p

if __name__ == "__main__":
    solution = Solution()
    print(solution.mySqrt(1))