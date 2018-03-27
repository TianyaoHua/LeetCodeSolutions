class Solution(object):
    def core(self, x, n):
        if -0.00001< x < 0.00001:
            return 0
        elif x > 9223372036854775808:
            return float('inf')
        elif x < -9223372036854775808:
            return -float('inf')
        else:
            if n == 1:
                return x
            elif n == 0:
                return 1
            else:
                return self.myPow(x,int(n/2))*self.myPow(x,n-int(n/2))

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        # if n >= 0:
        #     return self.core(x, n)
        # else:
        #     return 1/self.core(x, -n)
        s = 1
        for i in range(n):
            s = s * x
            if -0.000001 < s < 0.000001:
                return 0
        return s

if __name__ == "__main__":
    solution = Solution()
    answer = solution.myPow(0.001, 1231231231230)
    print(answer)