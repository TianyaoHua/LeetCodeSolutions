class Solution:
    def core(self, s, i, record):
        if i in record:
            return record[i]
        elif i == len(s):
            return 1
        else:
            answer = 0
            if s[i] == '0':
                answer = 0
            elif '3' <= s[i] <= '9':
                answer += self.core(s, i+1, record)
                answer %= 1e9+7
            elif '1' <= s[i] <= '2':
                answer += self.core(s, i+1, record)
                answer %= 1e9 + 7
                if i+1 < len(s):
                    if s[i+1] != '*' and 10 < int(s[i:i+2]) <= 26:
                        answer += self.core(s, i+2, record)
                        answer %= 1e9 + 7
                    elif s[i+1] == '*':
                        if s[i] == '1':
                            answer += 9*self.core(s, i+2, record)
                            answer %= 1e9 + 7
                        else:
                            answer += 6*self.core(s, i+2, record)
                            answer %= 1e9 + 7
            else:
                answer += 9*self.core(s, i+1, record)
                answer %= 1e9 + 7
                if i+1 < len(s):
                    if '0' <= s[i+1] <= '6':
                        answer += 2*self.core(s, i+2, record)
                        answer %= 1e9 + 7
                    elif '7' <= s[i+1] <= '9':
                        answer += self.core(s, i+2, record)
                        answer %= 1e9 + 7
                    else:
                        answer += 15*self.core(s, i+2, record)
                        answer %= 1e9 + 7
            record[i] = answer
            return answer

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = [0]*(len(s)+1)
        table[-1] = 1
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                table[i] = 0
            elif '3' <= s[i] <= '9':
                table[i] += table[i+1]
                table[i] %= int(1e9+7)
            elif '1' <= s[i] <= '2':
                table[i] += table[i+1]
                table[i] %= int(1e9+7)
                if i+1 < len(s):
                    if s[i+1] != '*' and 10 <= int(s[i:i+2]) <= 26:
                        table[i] += table[i+2]
                        table[i] %= int(1e9+7)
                    elif s[i+1] == '*':
                        if s[i] == '1':
                            table[i] += 9*table[i+2]
                            table[i] %= int(1e9+7)
                        else:
                            table[i] += 6*table[i+2]
                            table[i] %= int(1e9+7)
            else:
                table[i] += 9*table[i+1]
                table[i] %= int(1e9+7)
                if i+1 < len(s):
                    if '0' <= s[i+1] <= '6':
                        table[i] += 2*table[i+2]
                        table[i] %= int(1e9+7)
                    elif '7' <= s[i+1] <= '9':
                        table[i] += table[i+2]
                        table[i] %= int(1e9+7)
                    else:
                        table[i] += 15*table[i+2]
                        table[i] %= int(1e9+7)
        return table[0]

print(Solution().numDecodings('10*1'))
