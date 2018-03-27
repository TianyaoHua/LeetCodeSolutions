class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        dict = {nums[i]:i for i in range(n)}
        answer = [-1 for i in range(len(findNums))]
        for i in range(len(findNums)):
            number = findNums[i]
            index = dict[number]+1
            while index < n and nums[index] <= number:
                index += 1
            if index < n:
                answer[i] = index
        return answer