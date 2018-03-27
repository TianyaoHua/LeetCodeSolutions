class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        stack = [nums[-1]]
        answer = [-1 for i in range(n)]
        for i in range(n-1):
            if nums[i] > stack[0]:
                stack.insert(0, nums[i])
        if len(stack) > 1:
            answer[-1] = stack[-2]
        for i in range(n-2,-1,-1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            if not stack:
                answer[i] = -1
            else:
                answer[i] = stack[-1]
            stack.append(nums[i])
        return answer

print(Solution().nextGreaterElements([1,2,1]))