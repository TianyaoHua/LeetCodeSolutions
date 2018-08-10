class Solution(object):
    def triangle(self, nums, i):
        answer = 0
        prev = i - 1
        j = 0
        while (j < prev):
            k = prev
            while k > j and nums[j] + nums[k] > nums[i]:
                    k -= 1
            if (k > j):
                answer += (i - 1 - k) + (prev-k)*(prev-k - 1)//2 + (prev - k)*(i-prev)
            else:
                answer += (i - 1 - k) + (prev-k - 1)*(prev-k - 2)//2 + (prev-k-1)*(i-prev)
            prev = k
            j += 1
        return answer

    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) < 3:
            return 0
        else:
            answer = 0
            for i in range(2, len(nums)):
                answer += self.triangle(nums, i)
        return answer

print(Solution().triangleNumber([1,2,3,4,5,6]))
