class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        d1 = {}
        for c in s1:
            if c not in d1:
                d1[c] = 0
            d1[c] += 1
        n = len(s1)
        d2 = {}
        for c in s2[:n]:
            if c not in d2:
                d2[c] = 0
            d2[c] += 1
        i = 0
        j = n-1
        length_2 = len(s2)
        while j < length_2-1:
            if d1 == d2:
                return True
            d2[s2[i]] -= 1
            if d2[s2[i]] == 0:
                d2.pop(s2[i])
            i += 1
            j += 1
            if s2[j] not in d2:
                d2[s2[j]] = 0
            d2[s2[j]] += 1
        return d1 == d2
print(Solution().checkInclusion("ab", "e"))