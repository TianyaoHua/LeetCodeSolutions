class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        i = 1
        p_a = 0
        p_b = n - 1
        while p_b-p_a > 0:
            nums_p_a = nums[p_a]
            flag = (nums_p_a == val)
            nums[p_a] = flag*nums[p_b] + (not flag)*nums_p_a
            p_b -= flag
            p_a += not flag
        # while p_b-p_a > 0:
        #     if nums[p_a] == val:
        #         nums[p_a] = nums[p_b]
        #         p_b -= 1
        #     else:
        #         p_a += 1
        return (nums[p_b] == val) * p_b + (nums[p_b] != val) * (p_b + 1)

if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,3,3,4,5,6,7,8,3]
    val = 3
    answer = solution.removeElement(nums,val)
    print (answer)
    print (nums)