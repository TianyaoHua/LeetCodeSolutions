class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        k = len(primes)
        indices = [0 for i in range(k)]
        num = [1]
        for i in range(n-1):
            m = float('inf')
            for j in range(k):
                index_j = indices[j]
                while num[index_j]*primes[j] <= num[-1]:
                    index_j += 1
                m = min(m, num[index_j]*primes[j])
                indices[j] = index_j
            num.append(m)
        return num[-1]

solution = Solution()
print(solution.nthSuperUglyNumber(12,[2, 7, 13, 19]))

