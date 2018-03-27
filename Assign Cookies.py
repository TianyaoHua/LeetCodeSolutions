class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        [n,m,i,j]=[len(g),len(s),0,0]
        answer = 0
        while i < n and j < m:
            if s[j] >= g[i]:
                answer += 1
                j += 1
                i += 1
            else:
                j += 1
        return answer