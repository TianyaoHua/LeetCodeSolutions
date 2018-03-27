class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = []
        if n <= 2:
            return 0
        else:
            for i in range(2, n):
                upper = int(i**0.5)
                j = 0
                p = len(primes)
                while j < p and primes[j] <= upper and i%primes[j]:
                    j += 1
                if j >= p or primes[j] > upper:
                    primes.append(i)
            return len(primes)


solution = Solution()
print(solution.countPrimes(1500000))
