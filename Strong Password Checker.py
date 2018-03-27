import itertools
class Solution(object):
    def statistic(self, s):
        lowercase = 0
        uppercase = 0
        digits = 0
        others = 0
        repeats = []
        n = len(s)
        repeating = 1
        for i in range(n):
            if 'a' <= s[i] <= 'z':
                lowercase += 1
            elif 'A' <= s[i] <= 'Z':
                uppercase += 1
            elif '0' <= s[i] <= '9':
                digits += 1
            else:
                others += 1
            if i > 0 and s[i] == s[i - 1]:
                repeating += 1
            else:
                if repeating >= 3:
                    repeats.append(repeating)
                repeating = 1
        if repeating >=3:
            repeats.append(repeating)
        return lowercase, uppercase, digits, repeats

    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = 0
        n = len(s)
        lowercase, uppercase, digits, repeats = self.statistic(s)
        if n > 20 and repeats:
            repeats.sort(key=lambda x: x % 3)
            delete = n-20
            while delete > 0:
                repeats[0] -= 1
                if repeats[0] % 3 == 2:
                    a = repeats.pop(0)
                    repeats.append(a)
                answer += 1
                delete -= 1
                n -= 1
        for row in repeats:
            while n < 6 and row >= 3:
                if lowercase == 0:
                    lowercase += 1
                    n += 1
                    answer += 1
                elif uppercase == 0:
                    uppercase += 1
                    n += 1
                    answer += 1
                elif digits == 0:
                    digits += 1
                    n += 1
                    answer += 1
                else:
                    n += 1
                    answer += 1
                row = row//2 + row % 2
            while 6 <= n <= 20 and row >=3:
                if not lowercase:
                    lowercase += 1
                elif not uppercase:
                    uppercase += 1
                elif not digits:
                    digits += 1
                answer += 1
                row -= 3
        if uppercase == 0:
            if n < 6:
                n += 1
            answer += 1
        if lowercase == 0:
            if n < 6:
                n += 1
            answer += 1
        if digits == 0:
            if n<6:
                n+=1
            answer += 1
        if n < 6:
            answer += (6-n)
        if n > 20:
            answer += (n-20)
        return answer
solution = Solution()
print(solution.strongPasswordChecker('AAAAAABBBBBB123456789a'))