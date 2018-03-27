class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer =[1]
        n = len(nums)
        for i in range(1, n):
            answer.append(answer[i-1]*nums[i-1])
        p_product = nums[-1]
        for i in range(n-2, -1, -1):
            answer[i] *= p_product
            p_product = nums[i]*p_product
        return answer


solution = Solution()
nums=[1]
print(solution.productExceptSelf(nums))