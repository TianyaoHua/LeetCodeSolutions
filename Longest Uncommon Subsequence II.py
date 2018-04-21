# Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.
# A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.
# The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.
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

    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        dict = {}
        unique = {}
        for s in strs:
            if len(s) not in dict:
                dict[len(s)] = {s}
                unique[s] = 1
            else:
                dict[len(s)].add(s)
                if s in unique:
                    unique[s] = 0
                else:
                    unique[s] = 1
        lengths = list(dict.keys())
        lengths.sort(reverse=True)
        for i in range(len(lengths)):
            l = lengths[i]
            for s in dict[l]:
                if unique[s] == 1:
                    flag = 1
                    j = i -1
                    while j > -1 and flag == 1:
                        for longer_s in dict[lengths[j]]:
                            if self.subsequnce(s, longer_s):
                                flag = 0
                                break
                        j -= 1
                    if flag == 1:
                        return l
        return -1

print(Solution().findLUSlength(["aabbcc", "aabbcc","cb","abc"]))
###beat 98.2%