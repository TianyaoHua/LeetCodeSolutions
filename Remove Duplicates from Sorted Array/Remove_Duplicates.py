class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        i = 1
        true_l = n
        p_current = 1
        p_available = 1
        p_probe = 0
        last_valid_value = nums[0]
        lock = 0
        while p_current < n:
            if nums[p_current] == last_valid_value:
                lock = 1
                p_probe = p_current + 1
                while p_probe < n and nums[p_probe] == nums[p_current]:
                    p_probe += 1
                if p_probe < n:
                    last_valid_value = nums[p_probe]
                    nums[p_available] = last_valid_value
                    p_available += 1
                    p_current = p_probe + 1
                else:
                    p_current += 1

                # for p_probe in range(p_current+1,n):
                #     if nums[p_probe] > nums[p_current]:
                #         last_valid_value = nums[p_probe]
                #         nums[p_available] = last_valid_value
                #         p_available += 1
                #         p_current = p_probe
                #         break
                # p_current += 1
            else:
                last_valid_value = nums[p_current]
                nums[p_available] = last_valid_value
                p_current += 1
                p_available = (not lock) * p_current + lock * (p_available + 1)
        return p_available
if __name__ == "__main__":
    solution =Solution()
    nums = [1,1]
    length = solution.removeDuplicates(nums)
    print(length,nums)
