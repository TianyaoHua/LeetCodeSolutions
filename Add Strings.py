class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        n1 = len(num1)
        n2 = len(num2)
        if n1 < n2:
            num1, num2 = num2, num1
        n = min(n1, n2)
        m = max(n1, n2)
        carry = 0
        answer = ''
        for i in range(n):
            s = int(num1[i]) + int(num2[i]) + carry
            if s >= 10:
                s -= 10
                carry = 1
            else:
                carry = 0
            answer = (str(s)) + answer
        i += 1
        while carry != 0 and i < m:
            s = int(num1[i]) + carry
            if s >= 10:
                s -= 10
                carry = 1
            else:
                carry = 0
            answer = str(s) + answer
            i += 1
        if carry != 0:
            answer = str(carry) + answer
        else:
            answer = num1[i:][::-1] + answer
        return answer

solution = Solution()
print(solution.addStrings("123456789",
"987654321"))