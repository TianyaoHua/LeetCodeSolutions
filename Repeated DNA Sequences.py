class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        h = {}
        for i in range(len(s)):
            if s[i:i+10] not in h:
                h.update({s[i:i+10]: 0})
            h[s[i:i+10]] += 1
        answer = []
        for a in h:
            if h[a] > 1:
                answer.append(a)
        return answer

solution = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(solution.findRepeatedDnaSequences(s))