class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=1)
        n = len(citations)
        i = 0
        while i < n and citations[i] > i:
            i += 1
        if i < n:
            return max(i, citations[i])
        else:
            return n

solution = Solution()
citations = [8,8,8,8,8,8]
print(solution.hIndex(citations))
