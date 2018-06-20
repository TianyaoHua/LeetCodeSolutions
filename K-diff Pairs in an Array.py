class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        table = {}
        answer = 0
        for n in nums:
            if n not in table:
                table[n] = 0
            table[n] += 1
        if k == 0:
            for key in table.keys():
                answer += table[key] > 1
        else:
            for key in table.keys():
                answer += (key + k) in table
                answer += (key - k) in table
        return answer
