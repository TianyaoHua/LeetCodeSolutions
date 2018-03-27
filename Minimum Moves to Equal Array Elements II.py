class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        n = len(nums)
        x = s//n +[0, 1][s/n-s//n >=0.5]
        return sum([abs(i-x) for i in nums])

print(Solution().minMoves2([1,0,0,8,6]))