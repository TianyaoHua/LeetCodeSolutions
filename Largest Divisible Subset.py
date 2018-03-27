class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        table=[1 for i in range(len(nums))]
        aux = [i for i in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(i-1,-1,-1):
                if  table[i] < table[j]+1 and nums[i]%nums[j] == 0:
                    table[i] = table[j] + 1
                    aux[i]=j
        index = table.index(max(table))
        answer = [nums[index]]
        while index > aux[index]:
            index = aux[index]
            answer.append(nums[index])
        return answer

solution = Solution()
nums=[1,2,4,8]
print(solution.largestDivisibleSubset(nums))