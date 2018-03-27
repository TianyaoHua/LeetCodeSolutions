class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        u = [1]
        i = 0
        j = 0
        k = 0
        for m in range(n-1):
            last = u[-1]
            while u[i]*2 <= last:
                i += 1
            while u[j]*3 <= last:
                j += 1
            while u[k]*5 <= last:
                k += 1
            u.append(min(u[i]*2, u[j]*3, u[k]*5))
        return u[-1]

solution = Solution()
print(solution.nthUglyNumber(1690))