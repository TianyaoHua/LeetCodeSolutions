class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        r = []
        while n > 26:
            R = n % 26
            if R:
                r.append(R)
                n = n//26
            else:
                r.append(26)
                n = n//26 - 1
        r.append(n)
        answer =''
        for i in range(len(r)-1, -1, -1):
            answer += chr(65 + r[i] -1 )
        return answer

solution = Solution()
n = 99999
print(solution.convertToTitle(n))