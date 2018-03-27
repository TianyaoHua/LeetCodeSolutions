class Solution(object):
    def win(self, nums, i, j, dict, s):
        if (i, j) in dict:
            return dict[(i, j)]
        if i == j:
            return nums[i]
        answer = max(nums[i] + s[j+1]-s[i+1]-self.win(nums,i+1, j, dict, s), nums[j]+s[j]-s[i]-self.win(nums, i, j-1, dict, s))
        dict[(i,j)] = answer
        return answer
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = {}
        s = [0]
        for i in range(0, len(nums)):
            s.append(s[-1]+nums[i])
        add = self.win(nums,0,len(nums)-1,dict,s)
        print(dict)
        print(add)
        print(add >= s[-1]-add)

Solution().PredictTheWinner([1, 5, 2])
