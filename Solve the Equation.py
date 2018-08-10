class Solution:
    def sparse(self, expression):
        expression = expression.split('+')
        n = 0
        c = 0
        for s in expression:
            s = s.split('-')
            for i in range(len(s)):
                if s[i].isdecimal():
                    if i == 0:
                        n += int(s[i])
                    else:
                        n -= int(s[i])
                else:
                    if i == 0:
                        if s[i][0:-1] == '':
                            c += 1
                        else:
                            c += int(s[i][0:-1])
                    else:
                        if s[i][0:-1] == '':
                            c -= 1
                        else:
                            c -= int(s[i][0:-1])
        return [n, c]
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        [left, right] = equation.split('=')
        if left[0] == '-':
            left = '0'+left
        if right[0] == '-':
            right = '0' + right
        [nl, cl] = self.sparse(left)
        [nr, cr] = self.sparse(right)
        c = cl - cr
        n = nr - nl
        if c != 0:
            return "x=" + str(n/c)
        else:
            if n == 0:
                return "Infinite solutions"
            else:
                return "No solution"

print(Solution().solveEquation("-x=1"))