class Solution(object):
    def cal(self, s, n):
        p = -1
        a = 0
        i = 0
        s += '+'
        operation = 1
        while i < n:
            if s[i] != '+' and s[i] != '-':
                if p < 0:
                    p = i
            else:
                if operation == 1:
                    a += int(s[p: i])
                else:
                    a -= int(s[p: i])
                if s[i] == '+':
                    operation = 1
                else:
                    operation = 0
                p = -1
            i += 1
        return a
    def cal2(self, s, n):
        p = -1
        a = 1
        i = 0
        s += '*'
        operation = 1
        while i < n:
            if s[i] != '*' and s[i] != '/':
                if p < 0:
                    p = i
            else:
                if operation == 1:
                    a *= int(s[p: i])
                else:
                    a //= int(s[p: i])
                if s[i] == '*':
                    operation = 1
                else:
                    operation = 0
                p = -1
            i += 1
        return a
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ','')
        s += '+'
        p = 0
        i = 0
        n = len(s)
        flag = 1
        while i < n:
            if (s[i] == '*' or s[i] == '/') and flag == 1:
                flag = 0
            elif s[i] == '+' or s[i] == '-':
                if not flag:
                    r = str(self.cal2(s[p:i], i-p+1))
                    s = s[:p] + r + s[i:]
                    n = n + len(r) - i + p
                    i = p + len(r) - 1
                    flag = 1
                else:
                    p = i+1
            i += 1
        return self.cal(s[0:-1], len(s))

solution = Solution()
s = '3/2'
print(solution.calculate(s))



