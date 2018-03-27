class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        scores = [[nums[i], i] for i in range(len(nums))]
        scores.sort(key=lambda x:x[0],reverse=1)
        answer = ['' for i in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                answer[scores[i][1]] = "Gold Medal"
            elif i == 1:
                answer[scores[i][1]] = "Silver Medal"
            elif i == 2:
                answer[scores[i][1]] = "Bronze Medal"
            else:
                answer[scores[i][1]] = str(i+1)
        return answer

print(Solution().findRelativeRanks([5,4,3,2,1]))