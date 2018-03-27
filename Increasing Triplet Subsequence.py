class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        one = float('inf')
        two = float('inf')
        for i in nums:
            if i > two:
                return True
            elif i > one:
                two = min(two, i)
            else:
                one = min(one, i)
        return False


solution = Solution()
nums = [5,1,5,5,2,5,4]
print(solution.increasingTriplet(nums))