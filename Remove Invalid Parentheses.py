class Solution(object):
    def isValid(self, s):
        n = 0
        for i in s:
            if i == '(':
                n += 1
            elif i == ')':
                n -= 1
                if n < 0:
                    return False
        return n == 0

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        Q = {s}
        answer = set()
        found = False
        while not found and Q:
            for u in Q:
                if self.isValid(u):
                    answer.add(u)
                    found = True
            Q = {u[0:i] + u[i+1:] for u in Q for i in range(len(u))}
        return list(answer)


solution = Solution()
s = ')(((((((('
print(solution.removeInvalidParentheses(s))