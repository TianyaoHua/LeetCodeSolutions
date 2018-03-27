class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        d_p = {}
        for c in p:
            if c not in d_p:
                d_p.update({c:0})
            d_p[c] += 1
        n = len(p)
        m = len(s)
        if m<n:
            return 0
        d_s = {}
        answer = []
        for c in s[0:n]:
            if c not in d_s:
                d_s.update({c:0})
            d_s[c] += 1
        i = n-1
        while i < m-1:
            if d_p == d_s:
                answer.append(i-n+1)
            d_s[s[i-n+1]] -= 1
            if d_s[s[i-n+1]] == 0:
                d_s.pop(s[i-n+1])
            i += 1
            if s[i] not in d_s:
                d_s.update({s[i]:0})
            d_s[s[i]] += 1
        if d_p == d_s:
            answer.append(i - n + 1)
        return answer
s = "abab"
p = "ab"
print(Solution().findAnagrams(s,p))