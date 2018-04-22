# Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some
# characters of the given string.
# If there are more than one possible results, return the longest word with the smallest lexicographical order.
# If there is no possible result, return the empty string.
class Solution(object):
    def subsequnce(self, a, b):
        na = len(a)
        nb = len(b)
        i, j = 0, 0
        while i < na and j < nb:
            if b[j] == a[i]:
                i += 1
                j += 1
            else:
                j += 1
        return i == na
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort(key=lambda x: len(x))
        i, n = 0, len(d)
        limit = 0
        answer = ''
        while i < n and len(d[i]) >= limit:
            w = d[i]
            if len(w) <= len(s) and self.subsequnce(w, s):
                if len(w) > len(answer) or (len(w) == len(answer) and w < answer):
                    answer = w
                    limit = len(w)
            i += 1
        return answer

print(Solution().findLongestWord(s = "abpcplea", d = ["ale","apple","monkey","plea"]))


