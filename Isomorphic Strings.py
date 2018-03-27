class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n1 = len(s)
        n2 = len(t)
        if n1 != n2:
            return False
        else:
            map1 = {}
            map2 = {}
            for i in range(n1):
                if s[i] not in map1 and t[i] not in map2:
                    map1.update({s[i]: t[i]})
                    map2.update({t[i]: s[i]})
                elif s[i] not in map1 or t[i] not in map2 or map1[s[i]] != t[i] or map2[t[i]] != s[i]:
                    return False
            return True

solution = Solution()
s = 'bb'
t = 'ab'
print(solution.isIsomorphic(s, t))