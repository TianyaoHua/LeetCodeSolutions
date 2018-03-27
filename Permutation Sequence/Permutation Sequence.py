class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        lookup = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6:720, 7: 5040, 8: 40320, 9: 362880}
        numbers = [i for i in range(1, n+1)]
        s = ''
        for i in range(n-1,-1,-1):
            rank = k//lookup.get(i)+int(k % lookup.get(i) != 0)
            c = numbers[rank-1]
            numbers.remove(c)
            s = s + str(c)
            k = k - lookup.get(i)*(rank-1)
        return s

if __name__ == "__main__":
    solution = Solution()
    print(solution.getPermutation(3,6))


