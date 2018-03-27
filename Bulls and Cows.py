class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        a = []
        b = []
        n = len(secret)
        bull = 0
        cow = 0
        for i in range(n):
            if secret[i] == guess[i]:
                bull += 1
            else:
                a.append(int(secret[i]))
                b.append(int(guess[i]))
        a.sort()
        b.sort()
        i = 0
        j = 0
        n = len(a)
        while i < n and j < n:
            if a[i] == b[j]:
                cow += 1
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1
        return str(bull)+'A' + str(cow) + 'B'

solution = Solution()
secret = '1807'
guess = '7810'
print(solution.getHint(secret, guess))