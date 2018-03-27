class Solution(object):
    def remove1digit(self,nums):
        n = len(nums)
        if not n:
            return nums
        i = 0
        while i < n-1 and nums[i] <= nums[i+1]:
            i += 1
        if i < n-1:
            nums = nums[0:i] + nums[i+1:]
        else:
            nums = nums[0:-1]
        i = 0
        while i < n-1 and nums[i] == '0':
            i += 1
        nums = nums[i:]
        return nums

    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        for _ in range(k):
            num = self.remove1digit(num)
        if num:
            return int(num)
        else:
            return 0

solution = Solution()
print(solution.removeKdigits("10",2))