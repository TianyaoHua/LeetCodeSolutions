class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        k = {0:1}
        for i in range(min(nums), target+1):
            c = 0
            for n in nums:
                if i-n in k:
                    c += k[i-n]
            k.update({i:c})
        return k[target]


solution = Solution()
print(solution.combinationSum4([9],3))