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
        return table[0]

solution = Solution()
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict=["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(solution.wordBreak(s,wordDict))