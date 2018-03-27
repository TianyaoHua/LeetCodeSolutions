class Solution(object):
    def divide_conquer(self, nums, i, j):
        if j - i == 0:
            return 0
        if j - i == 1:
            return int(nums[i] > 2*nums[j])
        p = (i+j)//2
        left, right = sorted(nums[i:p+1]), sorted(nums[p+1:j+1])
        m, n, l_left, l_right, temp, answer = 0, 0, p-i+1,j-p,0,0
        while m < l_left and n < l_right:
            if 2*right[n] < left[m]:
                temp += 1
                n += 1
            else:
                answer += (l_left-m)*temp
                temp = 0
                m += 1
        answer += (l_left-m)*temp
        return answer + self.divide_conquer(nums, i, p) + self.divide_conquer(nums,p+1,j)


    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return self.divide_conquer(nums, 0, n-1)

print(Solution().reversePairs([233,2000000001,234,2000000006,235,2000000003,236,2000000007,237,2000000002,2000000005,233,233,233,233,233,2000000004]))