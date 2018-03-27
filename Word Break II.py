class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        h = {i: [] for i in range(n)}
        for word in wordDict:
            index = s.find(word)
            bias = 0
            while index > -1:
                h[index + bias].append(word)
                bias = index + bias + 1
                index = s[bias:].find(word)
        table = [False for i in range(n+1)]
        table[n] = True
        for i in range(n-1, -1, -1):
            answer = False
            for word in h[i]:
                answer = answer or (table[i+len(word)])
            table[i] = answer
        if table[0]:
            table = [[] for i in range(n+1)]
            table[n] = ['']
            for i in range(n-1, -1, -1):
                for word in h[i]:
                    for sub_solution in table[i+len(word)]:
                        table[i].append(word + ' ' + sub_solution)
            for i in range(len(table[0])):
                table[0][i] = table[0][i][:-1]
            return table[0]
        else:
            return []
solution = Solution()
s = "catsanddog"
dict = ["cat"]
print(solution.wordBreak(s, dict))