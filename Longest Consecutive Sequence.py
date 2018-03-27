class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        for i in nums:
            if i not in h:
                if i-1 in h and i+1 in h:
                    length = h[i-1] + h[i+1] + 1
                    h.update({i: length})
                    h[i-1-h[i-1]+1] = length
                    h[i+1+h[i+1]-1] = length
                elif i-1 not in h and i+1 not in h:
                    h.update({i: 1})
                elif i-1 in h and i+1 not in h:
                    length = h[i-1] + 1
                    h.update({i: length})
                    h[i - 1 - h[i - 1] + 1] = length
                else:
                    length = h[i+1] + 1
                    h.update({i: length})
                    h[i + 1 + h[i + 1] - 1] = length
        return max(h.values())

solution = Solution()
nums = [1, 3, 5, 2, 4]
print(solution.longestConsecutive(nums))

