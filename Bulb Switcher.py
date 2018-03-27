class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        bulbs = [1]
        primes = []
        factor = [{1:1}]
        if n <= 1:
            return n
        for i in range(2, n+1):
            isPrime = 1
            for prime in primes:
                if i % prime == 0:
                    isPrime = 0
                    factor.append(factor[i//prime-1].copy())
                    if prime in factor[-1]:
                        factor[-1][prime] += 1
                    else:
                        factor[-1].update({prime: 1})
                    bulbs.append(bulbs[i//prime-1]//(factor[-1][prime])*(factor[-1][prime]+1))
                    break
            if isPrime:
                primes.append(i)
                factor.append({1:1,i:1})
                bulbs.append(2)
        return bulbs[-1]


solution = Solution()
print(solution.bulbSwitch(99999))